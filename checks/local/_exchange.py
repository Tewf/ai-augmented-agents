"""Shared by the exchange checks: which files are tasks and results, and what a task's parts hold.

An exchange is a pair of files, `NN-slug.task.md` and `NN-slug.result.md` (shapes/exchange.md). The settings are in
checks/config.toml under `[exchange]`. This module has no NAME, so the runner loads it and skips it; each check puts
its folder on sys.path to import it.
Time O(size of the files read).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import files_in_scope, matches_any, prose_only, repository_paths

DEFAULTS = {
    "task_files": ["*.task.md"],
    "result_files": ["*.result.md"],
    "headings": ["Task", "Decided", "To find", "Checks"],
    "decided_labels": ["Why handed over", "If the check fails"],
    "verdict_headings": ["Verdict", "Review", "Accepted", "Rejected", "Decision"],
}
STEM = re.compile(r"^\d{2,}-[a-z0-9]+(?:-[a-z0-9]+)*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ITEM = re.compile(r"^(?:[-*+]|\d+[.)])\s+(.*)$")
COMMAND = re.compile(r"`[^`\n]+`")


def settings(config: dict) -> dict:
    return {**DEFAULTS, **config.get("exchange", {})}


def tasks(root: Path, config: dict) -> list[str]:
    """The task files in scope."""
    patterns = settings(config)["task_files"]
    return [path for path in files_in_scope(root, config, {".md"}) if matches_any(path, patterns)]


def exchange_files(root: Path, config: dict) -> list[str]:
    """Every task and result file the repository tracks, in scope or not: a result is kept out of the other checks."""
    patterns = settings(config)["task_files"] + settings(config)["result_files"]
    return [path for path in repository_paths(root) if matches_any(path, patterns)]


def read(root: Path, path: str) -> str:
    return (root / path).read_text(encoding="utf-8", errors="replace")


def headings(text: str, level: int = 2) -> list[tuple[str, int]]:
    """The (title, line) of each heading of the given level, outside fenced code."""
    found = []
    for number, line in enumerate(prose_only(text).splitlines(), 1):
        match = HEADING.match(line)
        if match and len(match.group(1)) == level:
            found.append((match.group(2), number))
    return found


def body(text: str, title: str, level: int = 2) -> list[str] | None:
    """The lines under a heading, up to the next heading of the same or a higher level; None when absent."""
    lines = text.splitlines()
    marks = [(number, len(m.group(1))) for number, line in enumerate(prose_only(text).splitlines(), 1)
             if (m := HEADING.match(line))]
    for number, line in enumerate(prose_only(text).splitlines(), 1):
        match = HEADING.match(line)
        if match and len(match.group(1)) == level and match.group(2).lower() == title.lower():
            stop = next((n for n, depth in marks if n > number and depth <= level), len(lines) + 1)
            return lines[number:stop - 1]
    return None


def top_items(lines: list[str]) -> list[str]:
    """The list items that start at the left margin; indented lines belong to the item above."""
    items = []
    for line in lines:
        match = ITEM.match(line)
        if match:
            items.append(match.group(1))
        elif items and line.startswith((" ", "\t")) and line.strip():
            items[-1] += " " + line.strip()
    return items
