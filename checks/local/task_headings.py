"""Task headings: a task file holds the four parts of the brief, in order, each with something under it.

A task file is a document the settings `[exchange] task_files` name. A run with no error guarantees, for each:
- the headings Task, Decided, To find and Checks are all present at level 2, in that order (principle: list the
  checks);
- each has at least one line of text beneath it, so the Checks heading is not left empty.
It does not judge that the Checks are the ones the result needs, or that the Task is clear.
Time O(task files x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _exchange import body, headings, read, settings, tasks  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "task-headings"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    wanted = settings(config)["headings"]
    findings = []
    for path in tasks(root, config):
        text = read(root, path)
        found = {title.lower(): number for title, number in headings(text)}
        missing = [name for name in wanted if name.lower() not in found]
        if missing:
            findings.append(Finding(NAME, path, 1, f"a task lacks the heading {', '.join(missing)}"))
            continue
        lines = [found[name.lower()] for name in wanted]
        if lines != sorted(lines):
            findings.append(Finding(NAME, path, lines[0], f"the headings are out of order: expected {', '.join(wanted)}"))
        for name in wanted:
            if not any(line.strip() for line in body(text, name) or []):
                findings.append(Finding(NAME, path, found[name.lower()], f"nothing under {name}"))
    return findings
