# Results: the brief test

Thirty calls to a small hosted model, ten per arm, one task, judged by the program in [judge_tests.py](judge_tests.py). Written by [run.py](run.py) from [results.jsonl](results.jsonl). What was run and what it cannot say are in the [protocol](protocol.md).

## Pass rate and questions

| Arm | Valid runs | Passed | Pass rate | Replies with a question | Questions asked | No code |
|---|---|---|---|---|---|---|
| no brief | 10 | 0 | 0% | 0 | 0 | 0 |
| convention brief | 10 | 0 | 0% | 0 | 0 | 0 |
| full brief | 10 | 5 | 50% | 0 | 0 | 0 |

## Why a run failed

| Arm | Why a run failed | Runs |
|---|---|---|
| no brief | `AttributeError: module 'candidate' has no attribute 'scope_in_rows'` | 4 |
| no brief | `AssertionError: Test 3 failed: [] != [{'Name': 'input', 'Description': 'data input'}, {'Name': 'inside', 'Description': 'inner data'}]` | 1 |
| no brief | `IndentationError: unindent does not match any outer indentation level` | 1 |
| no brief | `AssertionError: Test failed. Expected [{'Scope': 'Local', 'Description': 'Applies to local scope', 'Status': 'in progress'}, {'Scope': 'Function', 'Description': 'Inside a function', 'Status': 'in sco` | 1 |
| no brief | `SyntaxError: invalid syntax` | 1 |
| no brief | `AssertionError: Expected [{'Scope': 'local', 'Type': 'in', 'Description': 'Local scope'}, {'Scope': 'block', 'Type': 'in', 'Description': 'Block scope'}], got []` | 1 |
| no brief | `AssertionError: Expected [['Domain', 'Users in the domain', 'Active'], ['Local', 'Local users only', 'Inactive'], ['Special', 'Users in special groups', 'Active']], got [['Domain', 'Users in the domai` | 1 |
| convention brief | `FAILED (failures=9)` | 6 |
| convention brief | `FAILED (failures=1)` | 4 |
| full brief | `FAILED (failures=9)` | 5 |

## Which tests failed

A run counts under each test it fails, when its code imports. A run that does not import counts under no test.

| Arm | Test failed | Runs |
|---|---|---|
| convention brief | `test_empty_what_cell_kept_as_empty_string` | 10 |
| convention brief | `test_alignment_separator_not_returned` | 6 |
| convention brief | `test_crlf_lines` | 6 |
| convention brief | `test_exact_match_only` | 6 |
| convention brief | `test_lists_in_rows_in_order` | 6 |
| convention brief | `test_markup_kept_verbatim` | 6 |
| convention brief | `test_no_trailing_newline` | 6 |
| convention brief | `test_other_tables_ignored` | 6 |
| convention brief | `test_whitespace_around_cells` | 6 |
| full brief | `test_alignment_separator_not_returned` | 5 |
| full brief | `test_crlf_lines` | 5 |
| full brief | `test_empty_what_cell_kept_as_empty_string` | 5 |
| full brief | `test_exact_match_only` | 5 |
| full brief | `test_lists_in_rows_in_order` | 5 |
| full brief | `test_markup_kept_verbatim` | 5 |
| full brief | `test_no_trailing_newline` | 5 |
| full brief | `test_other_tables_ignored` | 5 |
| full brief | `test_whitespace_around_cells` | 5 |
