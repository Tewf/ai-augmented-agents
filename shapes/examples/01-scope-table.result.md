```python
import re
from typing import List

def scope_in_rows(markdown: str) -> List[str]:
    lines = markdown.splitlines()
    in_rows = []
    in_scope_table = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check if this is a table header
        if line.startswith('|') and '|' in line[1:-1]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) >= 2 and cells[1] == 'What':
                in_scope_table = True
                continue

        # If we're in a scope table, check for rows
        if in_scope_table:
            if line.startswith('|') and '|' in line[1:-1]:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if len(cells) >= 2 and cells[0] == 'in':
                    in_rows.append(cells[1])
            elif line.startswith('|') and len(line.split('|')) == 1:
                # Separator row (only pipes), end of table
                in_scope_table = False

    return in_rows

import unittest

class TestScopeInRows(unittest.TestCase):
    def test_scope_table_with_in_and_out_rows(self):
        md = """
| What | Other |
|------|-------|
| in   | x     |
| out  | y     |
| in   | z     |
"""
        self.assertEqual(scope_in_rows(md), ['x', 'z'])

    def test_no_table_returns_empty_list(self):
        self.assertEqual(scope_in_rows("No table here"), [])
        self.assertEqual(scope_in_rows(""), [])

    def test_table_with_only_out_rows(self):
        md = """
| What | Value |
|------|-------|
| out  | a     |
| out  | b     |
"""
        self.assertEqual(scope_in_rows(md), [])

    def test_cells_with_spaces_and_no_spaces(self):
        md = """
| What | X |
|------|---|
|  in  | p |
|in    | q |
| in   | r |
"""
        self.assertEqual(scope_in_rows(md), ['p', 'q', 'r'])

    def test_only_exact_in_matches(self):
        md = """
| What | Value |
|------|-------|
| In   | a     |
| inside| b    |
| index | c    |
| in   | d     |
"""
        self.assertEqual(scope_in_rows(md), ['d'])

    def test_another_table_is_ignored(self):
        md = """
| Name | Value |
|------|-------|
| in   | ignored |
| What | Other |
|------|-------|
| in   | kept    |
"""
        self.assertEqual(scope_in_rows(md), ['kept'])

    def test_markup_in_cells_preserved(self):
        md = """
| What | Description |
|------|-------------|
| in   | **bold**    |
| in   | [link](url) |
| in   | normal      |
"""
        self.assertEqual(scope_in_rows(md), ['**bold**', '[link](url)', 'normal'])

    def test_separator_row_not_returned(self):
        md = """
| What | Value |
|:----:|-------|
| in   | a     |
|------|-------|
| in   | b     |
"""
        self.assertEqual(scope_in_rows(md), ['a'])

    def test_empty_what_cell_returned(self):
        md = """
| What | Value |
|------|-------|
| in   |       |
| in   | x     |
"""
        self.assertEqual(scope_in_rows(md), ['', 'x'])

    def test_crlf_and_no_final_newline(self):
        md = "What|Value\r\n|:--|--:\r\n|in|a\r\n|in|b"
        self.assertEqual(scope_in_rows(md), ['a', 'b'])
        md = "| What | Value |\n|------|-------|\n| in   | a     |\n| in   | b"
        self.assertEqual(scope_in_rows(md), ['a', 'b'])

    def test_result_is_list_of_str(self):
        md = "| What | X |\n|------|---|\n| in   | 1 |"
        result = scope_in_rows(md)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(x, str) for x in result))

if __name__ == '__main__':
    unittest.main()
```
