"""The three tasks of round two: prompts for the three arms, and the test files that judge them.

Each task has a visible test file, whose cases the full arm lists, and a hidden test file, whose cases no arm sees.
The hidden file is the judge. Every hidden case follows from the Decided lines of the task alone.
The prompts are constants, so the text run is the text read.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS = ("scope", "changelog", "llms")

TASK = {
    "scope": "Write a Python function that parses a Markdown scope table and lists its \"in\" rows, and tests for it.",
    "changelog": "Write a Python function that parses a Markdown changelog and lists its released versions with their dates, and tests for it.",
    "llms": "Write a Python function that parses the link list of an llms.txt file and returns each link with its description, and tests for it.",
}

CONVENTION = {
    "scope": """Task: write a Python function and its tests.

What is decided:
- The function is `scope_in_rows(markdown: str) -> list[str]`, in Python 3, standard library only.
- The scope table is the table whose header row has "What" as its second cell. Other tables are ignored.
- A row counts as "in" when its first cell, with spaces stripped, is exactly `in`.

What is to be found: the second cell ("What") of each "in" row, stripped, in order of appearance.

Output shape: one Python code block holding the function and its unit tests. No prose outside the block.""",
    "changelog": """Task: write a Python function and its tests.

What is decided:
- The function is `changelog_releases(markdown: str) -> list[tuple[str, str]]`, in Python 3, standard library only.
- A release is a line that starts with `## [`, then the version up to the next `]`, then ` - `, then a date written YYYY-MM-DD. Text may follow the date.
- A `## [Unreleased]` line is not a release. A `## [x]` line with no such date is not a release.
- Headings of other levels are ignored. Lines inside a fenced code block (``` fences) are ignored.

What is to be found: the pair (version, date) of each release, as two strings, in order of appearance.

Output shape: one Python code block holding the function and its unit tests. No prose outside the block.""",
    "llms": """Task: write a Python function and its tests.

What is decided:
- The function is `llms_links(text: str) -> list[tuple[str, str, str]]`, in Python 3, standard library only.
- A link line starts, at the first character of the line, with `- [`. Its form is `- [title](url)`, optionally followed by `: description`. The `]` that ends the title must be followed at once by `(`, and the url ends at the first `)`.
- The description is the text after a colon that comes directly after the `)`, stripped. It is "" when there is no such colon.
- Lines of any other shape are ignored, and so are lines inside a fenced code block (``` fences). Only the first link of a line counts.

What is to be found: the triple (title, url, description) of each link line, as three strings, in order of appearance.

Output shape: one Python code block holding the function and its unit tests. No prose outside the block.""",
}

CHECKS = {
    "scope": """
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
11. The result is a list of str.""",
    "changelog": """
The function will be judged by these checks, each a unit test:
1. A changelog with several releases returns their (version, date) pairs, in order.
2. Text with no release heading returns [], and so does empty text.
3. A `## [Unreleased]` heading is skipped.
4. A `## [1.0.0]` heading with no date is skipped.
5. `#` and `###` headings of the same shape are ignored.
6. A release heading inside a fenced code block is ignored.
7. A pre-release version such as `1.0.0-rc.1` is returned whole.
8. Lines ending in CRLF work, and so does text with no final newline.
9. The result is a list of tuples of two str.""",
    "llms": """
The function will be judged by these checks, each a unit test:
1. A link list with descriptions returns the (title, url, description) triples, in order.
2. Text with no link line returns [], and so does empty text.
3. A link with no description gives "" as its description.
4. Headings and prose lines are ignored.
5. Lines that start with `* [` or with spaces before `- [` are ignored.
6. A link line inside a fenced code block is ignored.
7. A description is kept as written, colons inside it included.
8. A line `- [text] no url` is ignored.
9. Lines ending in CRLF work, and so does text with no final newline.
10. The result is a list of tuples of three str.""",
}

VISIBLE = {"scope": HERE / "judge_tests.py", "changelog": HERE / "tasks" / "changelog_visible.py",
           "llms": HERE / "tasks" / "llms_visible.py"}
HIDDEN = {"scope": HERE / "tasks" / "scope_hidden.py", "changelog": HERE / "tasks" / "changelog_hidden.py",
          "llms": HERE / "tasks" / "llms_hidden.py"}
REFERENCE = {t: HERE / "tasks" / f"{t}_reference.py" for t in TASKS}
REFERENCE["scope"] = HERE / "reference.py"

ARMS = ("none", "convention", "full")


def prompt_for(task, arm):
    if arm == "none":
        return TASK[task]
    if arm == "convention":
        return CONVENTION[task]
    if arm == "full":
        return CONVENTION[task] + "\n" + CHECKS[task]
    raise ValueError(arm)
