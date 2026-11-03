# 01: list the "in" rows of a scope table

**Shape:** [exchange](../exchange.md)

**Result:** `01-scope-table.result.md`, in this folder. This is the brief test's full arm, run 3.

## Task

Write a Python function that parses a Markdown scope table and lists its "in" rows, and unit tests for it.

## Decided

- Why handed over: a program judges the answer, and the worker needs nothing the lead holds beyond this file.
- Worker: a small hosted model.
- If the check fails: ask once more with the failing test named; if it fails again, the lead writes it.
- The function is `scope_in_rows(markdown: str) -> list[str]`, in Python 3, standard library only.
- The scope table is the table whose header row has "What" as its second cell. Other tables are ignored.
- A row counts as "in" when its first cell, with spaces stripped, is exactly `in`.

## To find

The second cell ("What") of each "in" row, stripped, in order of appearance. Return one Python code block holding the function and its unit tests, and no prose outside the block.

## Checks

- Run `CANDIDATE=candidate.py python3 -I judge_tests.py` from `experiments/brief-test/`, with the code block saved as `candidate.py`. It passes when all thirteen tests pass:
  - a scope table with in and out rows returns the "What" cells of the in rows, in order;
  - text with no table returns an empty list, and so does empty text;
  - a table with only out rows returns an empty list;
  - cells padded with spaces, or rows written without spaces, are read the same way;
  - only the exact cell `in` counts: `In`, `inside` and `index` do not;
  - another table with an `in` row is ignored;
  - markup in a cell is returned unchanged;
  - the separator row, with alignment colons, is never returned;
  - an empty "What" cell in an in row is returned as an empty string;
  - lines ending in CRLF work, and so does a table with no final newline;
  - the result is a list of strings.
