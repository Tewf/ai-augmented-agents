"""Result cost: a result whose task asks for a cost line carries one, and a cost line states numbers.

The cost line is the last line a worker writes, `Cost: 40000 tokens, 0.02 dollars, 6 minutes` (shapes/exchange.md,
rule 8), so the lead can record what the work spent (protocols/maestro.md). A run with no error guarantees, over every
tracked result whose task holds the text `Cost:` under To find:
- the result has a line starting `Cost:`;
- every line starting `Cost:` is a comma-separated list of `number unit`, the unit one of tokens, points, dollars,
  minutes, each at most once.
A result whose task does not ask is not read: results older than the rule stay valid.
Time O(tracked files x size).
"""
from __future__ import annotations

import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _exchange import body, exchange_files, read, settings  # noqa: E402
from framework.check_api import Finding, matches_any  # noqa: E402

NAME = "result-cost"
EXACT = True

UNITS = ("tokens", "points", "dollars", "minutes")
LINE = re.compile(r"^\s*Cost:\s*(.*?)\s*$")
PART = re.compile(r"^(\d+(?:\.\d+)?)\s+(" + "|".join(UNITS) + r")$")


def asks(task_text: str) -> bool:
    lines = body(task_text, "To find") or []
    return any("Cost:" in line for line in lines)


def problem(rest: str) -> str | None:
    """Why a cost line is not one, or None."""
    seen = set()
    for part in [p.strip() for p in rest.split(",")]:
        match = PART.match(part)
        if not match:
            return f"'{part}' is not a number and a unit ({', '.join(UNITS)})"
        if match.group(2) in seen:
            return f"the unit {match.group(2)} appears twice"
        seen.add(match.group(2))
    return None


def check(root: Path, config: dict) -> list[Finding]:
    options = settings(config)
    files = exchange_files(root, config)
    present = set(files)
    findings = []
    for path in files:
        if not matches_any(path, options["result_files"]):
            continue
        task = posixpath.join(posixpath.dirname(path), posixpath.basename(path)[:-len(".result.md")] + ".task.md")
        if task not in present or not asks(read(root, task)):
            continue
        found = [(n, m.group(1)) for n, line in enumerate(read(root, path).splitlines(), 1) if (m := LINE.match(line))]
        if not found:
            findings.append(Finding(NAME, path, 1, "the task asks for a Cost line and the result has none"))
        for number, rest in found:
            reason = problem(rest)
            if reason:
                findings.append(Finding(NAME, path, number, f"the Cost line is malformed: {reason}"))
    return findings
