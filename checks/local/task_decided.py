"""Task decided: what is decided in a task says why the work is handed over, and what happens if its check fails.

For each task file, the section Decided holds a labelled line for every label in `[exchange] decided_labels`
(by default "Why handed over" and "If the check fails"), written `Label:` or `**Label:**`, with text after it
(principles: say why it is handed over; escalate on a failed check). A run with no error guarantees the lines exist and
are not empty. It does not judge the reason or that the escalation is sensible.
Time O(task files x size).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _exchange import body, read, settings, tasks  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "task-decided"
EXACT = True


def labelled(lines: list[str], label: str) -> bool:
    """True when a line reads `Label: text`, possibly as a list item or in bold, with text after the colon."""
    pattern = re.compile(rf"^\s*(?:[-*+]\s+)?(?:\*\*)?{re.escape(label)}(?::\*\*|\*\*:|:)\s*(\S.*)$", re.IGNORECASE)
    return any(pattern.match(line) for line in lines)


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in tasks(root, config):
        text = read(root, path)
        lines = body(text, "Decided")
        if lines is None:
            continue   # task-headings reports the missing section
        for label in settings(config)["decided_labels"]:
            if not labelled(lines, label):
                findings.append(Finding(NAME, path, 1, f"Decided has no line '{label}: ...' with text after it"))
    return findings
