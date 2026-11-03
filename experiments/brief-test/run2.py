"""Run round two of the brief test: 3 tasks, 3 arms, 2 tiers, ten runs each, judged by hidden tests.

Usage: python3 run2.py [--runs 10] [--only-report]
Tiers: "small" is the command in BRIEF_TEST_SMALL (default: ask-mistral through bash -lc); "paid" is claude_call.py,
which needs ANTHROPIC_API_KEY in the environment. Each call is appended to results-2.jsonl as it ends; a resumed run
redoes only the calls that failed. The table is written to results-2.md.
"""
import argparse
import ast
import json
import re
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import run
import tasks2

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results-2.jsonl"
REPORT = HERE / "results-2.md"
TIERS = ("small", "paid")
TIER_LABEL = {"small": "small hosted model", "paid": "claude-haiku-5-5"}
ARM_LABEL = {"none": "no brief", "convention": "convention brief", "full": "full brief"}


def call_command(tier, prompt):
    if tier == "paid":
        return [sys.executable, str(HERE / "claude_call.py"), prompt]
    cmd = os.environ.get("BRIEF_TEST_SMALL")
    if cmd:
        return [cmd, prompt]
    return ["bash", "-lc", 'ask-mistral "$1"', "_", prompt]


def ask(tier, prompt, timeout=150):
    """One call, retried once. Returns (reply, error)."""
    err = ""
    for _ in range(2):
        try:
            p = subprocess.run(call_command(tier, prompt), capture_output=True, text=True, timeout=timeout,
                               stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            err = "timeout"
            continue
        if p.returncode == 0 and p.stdout.strip():
            return p.stdout, ""
        err = (p.stderr.strip().splitlines() or ["empty reply"])[-1][:200]
        time.sleep(5)
    return "", err


OPEN = re.compile(r"^```(?:python|py)?[ \t]*$", re.M)
CLOSE = re.compile(r"^```[ \t]*$", re.M)


def extract_code(reply):
    """The python code of a reply. Fences are lines of their own, so a line of code that mentions a fence (the
    tasks parse fenced blocks) does not end the block. If the blocks do not parse, the text from the first
    opening fence to the last closing one is tried as a single block."""
    blocks, pos = [], 0
    while True:
        o = OPEN.search(reply, pos)
        if not o:
            break
        c = CLOSE.search(reply, o.end())
        if not c:
            break
        blocks.append(reply[o.end():c.start()].strip("\n"))
        pos = c.end()
    code = "\n\n".join(blocks)
    try:
        ast.parse(code)
    except SyntaxError:
        o, closes = OPEN.search(reply), list(CLOSE.finditer(reply))
        if o and closes and closes[-1].start() > o.end():
            whole = reply[o.end():closes[-1].start()].strip("\n")
            try:
                ast.parse(whole)
                return whole
            except SyntaxError:
                pass
    return code


def judge_file(code, test_file, timeout=20):
    """Run one test file against the code. Returns (passed, detail)."""
    if not code.strip():
        return False, "no code"
    with tempfile.TemporaryDirectory() as tmp:
        cand = Path(tmp) / "candidate.py"
        cand.write_text(code, encoding="utf-8")
        env = dict(os.environ, CANDIDATE=str(cand))
        env.pop("ANTHROPIC_API_KEY", None)
        try:
            p = subprocess.run([sys.executable, "-I", str(test_file)], env=env, cwd=tmp, capture_output=True,
                               text=True, timeout=timeout, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return False, "timeout"
    if p.returncode == 0:
        return True, "ok"
    last = [ln for ln in p.stderr.strip().splitlines() if ln.strip()]
    return False, (last[-1] if last else "failed")[:200]


def judge_both(task, reply):
    code = extract_code(reply)
    hidden, detail = judge_file(code, tasks2.HIDDEN[task])
    visible, _ = judge_file(code, tasks2.VISIBLE[task])
    return hidden, visible, detail


def load():
    if not RESULTS.exists():
        return []
    rows = {}
    for ln in RESULTS.read_text(encoding="utf-8").splitlines():
        if ln.strip():
            r = json.loads(ln)
            rows[(r["tier"], r["task"], r["arm"], r["run"])] = r  # a later row supersedes an earlier error
    return list(rows.values())


def rate(rows, key="hidden"):
    ok = [r for r in rows if not r["error"]]
    n = sum(1 for r in ok if r[key])
    return n, len(ok)


def fmt(n, d):
    return f"{n}/{d} ({n / d:.0%})" if d else "n/a"


def write_report(rows):
    L = ["# Results: the brief test, round two", "",
         "Calls to two model tiers, ten per cell, judged by hidden tests no arm saw; the visible tests are scored beside. "
         "Written by [run2.py](run2.py) from [results-2.jsonl](results-2.jsonl). What was run and what it cannot say are in the [protocol](protocol-2.md).", ""]
    L += ["## Pooled over tasks and tiers", "", "| Arm | Hidden pass | Visible pass | Replies with a question |", "|---|---|---|---|"]
    for arm in tasks2.ARMS:
        rs = [r for r in rows if r["arm"] == arm]
        ok = [r for r in rs if not r["error"]]
        L.append(f"| {ARM_LABEL[arm]} | {fmt(*rate(rs))} | {fmt(*rate(rs, 'visible'))} | {sum(1 for r in ok if r['questions'])} |")
    L += ["", "## By tier", "", "| Tier | " + " | ".join(ARM_LABEL[a] for a in tasks2.ARMS) + " |", "|---|---|---|---|"]
    for t in TIERS:
        L.append(f"| {TIER_LABEL[t]} | " + " | ".join(fmt(*rate([r for r in rows if r["tier"] == t and r["arm"] == a])) for a in tasks2.ARMS) + " |")
    L += ["", "## By task", "", "| Task | " + " | ".join(ARM_LABEL[a] for a in tasks2.ARMS) + " |", "|---|---|---|---|"]
    for k in tasks2.TASKS:
        L.append(f"| {k} | " + " | ".join(fmt(*rate([r for r in rows if r["task"] == k and r["arm"] == a])) for a in tasks2.ARMS) + " |")
    L += ["", "## Every cell, hidden pass (visible pass)", "", "| Tier | Task | " + " | ".join(ARM_LABEL[a] for a in tasks2.ARMS) + " |", "|---|---|---|---|---|"]
    for t in TIERS:
        for k in tasks2.TASKS:
            cells = []
            for a in tasks2.ARMS:
                rs = [r for r in rows if (r["tier"], r["task"], r["arm"]) == (t, k, a)]
                h, v = rate(rs), rate(rs, "visible")
                cells.append(f"{h[0]}/{h[1]} ({v[0]})")
            L.append(f"| {TIER_LABEL[t]} | {k} | " + " | ".join(cells) + " |")
    L += ["", "## Round one beside", "",
          "Round one's thirty replies (task scope, the small hosted model), judged by the visible tests as then, and rescored on the hidden tests of this round. "
          "The visible column reproduces [results.md](results.md).", "",
          "| Arm | Visible pass (round one) | Hidden pass (rescored) |", "|---|---|---|"]
    old = [json.loads(ln) for ln in (HERE / "results.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip()]
    for arm in tasks2.ARMS:
        rs = [r for r in old if r["arm"] == arm and not r["error"]]
        sc = [judge_both("scope", r["reply"]) for r in rs]
        L.append(f"| {ARM_LABEL[arm]} | {sum(1 for h, v, _ in sc if v)}/{len(rs)} | {sum(1 for h, v, _ in sc if h)}/{len(rs)} |")
    errs = sum(1 for r in rows if r["error"])
    L += ["", f"Calls recorded: {len(rows)}; left as errors: {errs}.", ""]
    REPORT.write_text("\n".join(L), encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=10)
    ap.add_argument("--only-report", action="store_true")
    a = ap.parse_args(argv)
    if not a.only_report:
        done = {(r["tier"], r["task"], r["arm"], r["run"]) for r in load() if not r["error"]}
        for n in range(1, a.runs + 1):
            for tier in TIERS:
                for task in tasks2.TASKS:
                    for arm in tasks2.ARMS:
                        if (tier, task, arm, n) in done:
                            continue
                        reply, err = ask(tier, tasks2.prompt_for(task, arm))
                        hidden, visible, detail = judge_both(task, reply) if not err else (False, False, err)
                        row = {"tier": tier, "task": task, "arm": arm, "run": n, "error": err, "hidden": hidden,
                               "visible": visible, "detail": detail, "questions": run.count_questions(reply), "reply": reply}
                        with RESULTS.open("a", encoding="utf-8") as f:
                            f.write(json.dumps(row) + "\n")
                        print(tier, task, arm, n, "H" if hidden else "-", "V" if visible else "-", err, flush=True)
    write_report(load())


if __name__ == "__main__":
    main()
