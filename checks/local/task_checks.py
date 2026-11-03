"""Task checks: each check a task lists is a command the lead runs, not an opinion.

For each task file, the list items at the left margin under Checks are its checks. A run with no error guarantees
at least one such item, and at least one of them names a command or a file in backticks (principle: run the checks
at the lead). It warns, as a heuristic, for each item that names none, since a check no program runs is judgment.
Indented lines belong to the item above, so a list of the cases the command covers can follow it.
It does not run the commands or judge that they decide the result.
Time O(task files x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _exchange import COMMAND, body, headings, read, tasks, top_items  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "task-checks"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in tasks(root, config):
        text = read(root, path)
        lines = body(text, "Checks")
        if lines is None:
            continue   # task-headings reports the missing section
        line = dict(headings(text)).get("Checks", 1)
        items = top_items(lines)
        if not items:
            findings.append(Finding(NAME, path, line, "Checks lists no item: give each check as a list item", "error"))
        elif not any(COMMAND.search(item) for item in items):
            findings.append(Finding(NAME, path, line, "no check names a command or file in backticks: none can be run", "error"))
        else:
            for item in items:
                if not COMMAND.search(item):
                    findings.append(Finding(NAME, path, line, f"a check names no command: '{item[:50]}'", "warning"))
    return findings
