"""Run the brief test: one task, three briefs, ten runs each, judged by a program.

Usage: BRIEF_TEST_COMMAND=<command> python3 run.py [--runs 10] [--only-report]

BRIEF_TEST_COMMAND is a command that takes the prompt as its one argument and prints the model's reply.
Nothing but the arm varies between runs. Each call is appended to results.jsonl as it ends, so a stopped
run resumes where it was. The table is written to results.md.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results.jsonl"
REPORT = HERE / "results.md"
ARMS = ("none", "convention", "full")

TASK = "Write a Python function that parses a Markdown scope table and lists its \"in\" rows, and tests for it."

CONVENTION = """Task: write a Python function and its tests.

What is decided:
- The function is `scope_in_rows(markdown: str) -> list[str]`, in Python 3, standard library only.
- The scope table is the table whose header row has "What" as its second cell. Other tables are ignored.
- A row counts as "in" when its first cell, with spaces stripped, is exactly `in`.

What is to be found: the second cell ("What") of each "in" row, stripped, in order of appearance.

Output shape: one Python code block holding the function and its unit tests. No prose outside the block."""

CHECKS = """
The function will be judged by these checks, each a unit test:
1. A scope table with in and out rows returns the "What" cells of the in rows, in order.
2. Text with no table returns [], and so does empty text.
3. A table with only out rows returns [].
4. Cells padded with spaces, or rows written without spaces (`|in|x|y|`), are read the same way.
5. Only the exact cell `in` counts: `In`, `inside` and `index` do not.
6. Another table (header `| Name | Value |`) with an `in` row is ignored.
7. Markup in a cell, such as `**bold**` or a link, is returned unchanged.
8. The separator row, including alignment colons (`|:--|:-:|--:|`), is never returned.
9. An empty "What" cell in an in row is returned as an empty string.
10. Lines ending in CRLF work, and so does a table with no final newline.
11. The result is a list of str."""


def prompt_for(arm):
    if arm == "none":
        return TASK
    if arm == "convention":
        return CONVENTION
    if arm == "full":
        return CONVENTION + "\n" + CHECKS
    raise ValueError(arm)


FENCE = re.compile(r"```(?:python|py)?[ \t]*\n(.*?)```", re.S)


def extract_code(reply):
    """The python code blocks of a reply, joined; empty if there is none."""
    return "\n\n".join(b.strip("\n") for b in FENCE.findall(reply))


def count_questions(reply):
    """Clarifying questions: lines outside code blocks that end with a question mark."""
    prose = FENCE.sub("", reply)
    return sum(1 for ln in prose.splitlines() if ln.rstrip().rstrip("*_)\"'").endswith("?"))


def judge(code, timeout=20):
    """Run the judge's tests against the code. Returns (passed, detail)."""
    if not code.strip():
        return False, "no code"
    with tempfile.TemporaryDirectory() as tmp:
        cand = Path(tmp) / "candidate.py"
        cand.write_text(code, encoding="utf-8")
        env = dict(os.environ, CANDIDATE=str(cand))
        try:
            p = subprocess.run([sys.executable, "-I", str(HERE / "judge_tests.py")], env=env, cwd=tmp,
                               capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return False, "timeout"
    if p.returncode == 0:
        return True, "ok"
    last = [ln for ln in p.stderr.strip().splitlines() if ln.strip()]
    return False, (last[-1] if last else "failed")[:200]


def failing_tests(code, timeout=20):
    """Names of the judge's tests that fail on the code; empty if it does not import or none fails."""
    if not code.strip():
        return []
    with tempfile.TemporaryDirectory() as tmp:
        cand = Path(tmp) / "candidate.py"
        cand.write_text(code, encoding="utf-8")
        env = dict(os.environ, CANDIDATE=str(cand))
        try:
            p = subprocess.run([sys.executable, "-I", str(HERE / "judge_tests.py"), "-v"], env=env, cwd=tmp,
                               capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return []
    return re.findall(r"^(test_\w+) \(.*?\) \.\.\. (?:FAIL|ERROR)$", p.stderr, re.M)


def ask(prompt, command, timeout=100):
    """One call; one retry after a failure. Returns (reply, error)."""
    err = ""
    for _ in range(2):
        try:
            p = subprocess.run([command, prompt], capture_output=True, text=True, timeout=timeout,
                               stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            err = "timeout"
            continue
        if p.returncode == 0 and p.stdout.strip():
            return p.stdout, ""
        err = (p.stderr.strip().splitlines() or ["empty reply"])[-1][:200]
    return "", err


def load():
    if not RESULTS.exists():
        return []
    return [json.loads(ln) for ln in RESULTS.read_text(encoding="utf-8").splitlines() if ln.strip()]


def summarize(rows):
    """Per arm: calls, errors, passes, pass rate, questions."""
    out = {}
    for arm in ARMS:
        rs = [r for r in rows if r["arm"] == arm]
        ok = [r for r in rs if not r["error"]]
        passes = sum(1 for r in ok if r["passed"])
        qs = [r["questions"] for r in ok]
        out[arm] = {
            "calls": len(rs), "errors": len(rs) - len(ok), "valid": len(ok), "passes": passes,
            "rate": (passes / len(ok)) if ok else None,
            "questions": sum(qs), "asked": sum(1 for q in qs if q > 0),
            "no_code": sum(1 for r in ok if r["detail"] == "no code"),
        }
    return out


INTRO = """# Results: the brief test

Thirty calls to a small hosted model, ten per arm, one task, judged by the program in [judge_tests.py](judge_tests.py). Written by [run.py](run.py) from [results.jsonl](results.jsonl). What was run and what it cannot say are in the [protocol](protocol.md).

## Pass rate and questions

"""

LABEL = {"none": "no brief", "convention": "convention brief", "full": "full brief"}


def table(summary):
    lines = ["| Arm | Valid runs | Passed | Pass rate | Replies with a question | Questions asked | No code |",
             "|---|---|---|---|---|---|---|"]
    for arm in ARMS:
        s = summary[arm]
        rate = "n/a" if s["rate"] is None else f"{s['rate']:.0%}"
        lines.append(f"| {LABEL[arm]} | {s['valid']} | {s['passes']} | {rate} | {s['asked']} | {s['questions']} | {s['no_code']} |")
    return "\n".join(lines)


def write_report(rows):
    s = summarize(rows)
    details = {}
    for r in rows:
        if not r["error"] and not r["passed"]:
            details.setdefault(r["arm"], {}).setdefault(r["detail"], 0)
            details[r["arm"]][r["detail"]] += 1
    lines = ["## Why a run failed", "", "| Arm | Why a run failed | Runs |", "|---|---|---|"]
    for arm in ARMS:
        for d, n in sorted(details.get(arm, {}).items(), key=lambda kv: -kv[1]):
            lines.append(f"| {LABEL[arm]} | `{d.replace('|', '/')}` | {n} |")
    if len(lines) == 4:
        lines.append("| none | no failed run | 0 |")
    per_test = {arm: {} for arm in ARMS}
    for r in rows:
        if not r["error"] and not r["passed"]:
            for t in failing_tests(extract_code(r["reply"])):
                per_test[r["arm"]][t] = per_test[r["arm"]].get(t, 0) + 1
    tl = ["## Which tests failed", "", "A run counts under each test it fails, when its code imports. A run that does not import counts under no test.", "", "| Arm | Test failed | Runs |", "|---|---|---|"]
    for arm in ARMS:
        for t, n in sorted(per_test[arm].items(), key=lambda kv: (-kv[1], kv[0])):
            tl.append(f"| {LABEL[arm]} | `{t}` | {n} |")
    if len(tl) == 6:
        tl.append("| none | no test failed after an import | 0 |")
    REPORT.write_text(INTRO + table(s) + "\n\n" + "\n".join(lines) + "\n\n" + "\n".join(tl) + "\n", encoding="utf-8")
    return s


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=10)
    ap.add_argument("--only-report", action="store_true")
    a = ap.parse_args(argv)
    if not a.only_report:
        command = os.environ.get("BRIEF_TEST_COMMAND")
        if not command:
            sys.exit("set BRIEF_TEST_COMMAND to a command that takes the prompt as one argument")
        done = {(r["arm"], r["run"]) for r in load() if not r["error"]}
        for run in range(1, a.runs + 1):
            for arm in ARMS:
                if (arm, run) in done:
                    continue
                reply, err = ask(prompt_for(arm), command)
                code = extract_code(reply)
                passed, detail = judge(code) if not err else (False, err)
                row = {"arm": arm, "run": run, "error": err, "passed": passed, "detail": detail,
                       "questions": count_questions(reply), "reply": reply}
                with RESULTS.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(row) + "\n")
                print(arm, run, "pass" if passed else "fail", detail, flush=True)
    # a retried call that finally worked supersedes its earlier error rows
    rows = {}
    for r in load():
        rows[(r["arm"], r["run"])] = r
    write_report(list(rows.values()))


if __name__ == "__main__":
    main()
