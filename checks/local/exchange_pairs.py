"""Exchange pairs: every task and result file is named NN-slug.task.md or NN-slug.result.md, every result has its
task, and a result holds no verdict.

A result is what the worker returned, kept as it came; the lead's verdict on it is written elsewhere (principle: keep
the result untouched). A run with no error guarantees, over every tracked task and result file:
- the name is a number, a slug of lowercase words and hyphens, then `.task.md` or `.result.md`;
- each result has a task of the same number and slug in the same folder;
- no result holds a heading named in `[exchange] verdict_headings` (Verdict, Review, Accepted, Rejected, Decision).
A task with no result is not an error: it may be waiting. It does not judge that a result is untouched, only that it
carries no section of the lead's own.
Time O(tracked files x size).
"""
from __future__ import annotations

import posixpath
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _exchange import STEM, exchange_files, headings, read, settings  # noqa: E402
from framework.check_api import Finding, matches_any  # noqa: E402

NAME = "exchange-pairs"
EXACT = True


def stem_of(path: str) -> tuple[str, str]:
    """The name without its `.task.md` or `.result.md` ending, and the ending."""
    name = posixpath.basename(path)
    for ending in (".task.md", ".result.md"):
        if name.endswith(ending):
            return name[:-len(ending)], ending
    return name, ""


def check(root: Path, config: dict) -> list[Finding]:
    options = settings(config)
    files = exchange_files(root, config)
    present = set(files)
    forbidden = {title.lower() for title in options["verdict_headings"]}
    findings = []
    for path in files:
        stem, ending = stem_of(path)
        if not STEM.match(stem):
            findings.append(Finding(NAME, path, 1, "the name is not NN-slug: a number, then lowercase words joined by hyphens"))
        if not matches_any(path, options["result_files"]):
            continue
        task = posixpath.join(posixpath.dirname(path), stem + ".task.md")
        if task not in present:
            findings.append(Finding(NAME, path, 1, f"no task of the same name beside it: {posixpath.basename(task)}"))
        text = read(root, path)
        for title, number in [h for level in (1, 2, 3) for h in headings(text, level)]:
            if title.lower() in forbidden:
                findings.append(Finding(NAME, path, number, f"the result holds a section '{title}': write the verdict elsewhere"))
    return findings
