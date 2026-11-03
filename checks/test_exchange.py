"""Tests of the exchange checks in checks/local/: each fails where a task or a result breaks its shape and stays
silent where it keeps it.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""),
              REPOSITORY.parent / "standard" / "checks", REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPOSITORY / "checks" / "local" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


headings, decided, commands, pairs, cost = (load("task_headings"), load("task_decided"), load("task_checks"),
                                            load("exchange_pairs"), load("result_cost"))

TASK = """# 01: list the rows

## Task

Write a function.

## Decided

- Why handed over: the answer is checked by a program.
- If the check fails: ask once more with the failing test named, then do it at the lead.

## To find

The rows.

## Checks

- Run `python3 -m unittest judge`; it passes when all tests pass.
  - the first case
"""
RESULT = "```python\ndef f():\n    return 1\n```\n"


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def write(self, path: str, text: str) -> None:
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text(text, encoding="utf-8")

    def run_check(self, module, config=None):
        return module.check(self.root, config or {})


class TaskHeadings(Base):
    def test_a_complete_task_passes(self):
        self.write("01-rows.task.md", TASK)
        self.assertEqual(self.run_check(headings), [])

    def test_a_missing_heading_fails(self):
        self.write("01-rows.task.md", TASK.replace("## To find\n\nThe rows.\n\n", ""))
        self.assertIn("To find", self.run_check(headings)[0].message)

    def test_headings_out_of_order_fail(self):
        self.write("01-rows.task.md", TASK.replace("## Task", "## Swap").replace("## Checks", "## Task").replace("## Swap", "## Checks"))
        self.assertIn("out of order", self.run_check(headings)[0].message)

    def test_an_empty_checks_section_fails(self):
        self.write("01-rows.task.md", TASK.split("## Checks")[0] + "## Checks\n")
        self.assertEqual([f.message for f in self.run_check(headings)], ["nothing under Checks"])

    def test_a_heading_inside_code_is_not_a_heading(self):
        self.write("01-rows.task.md", TASK.replace("## Checks", "```\n## Checks\n```\n"))
        self.assertIn("Checks", self.run_check(headings)[0].message)

    def test_other_files_are_not_tasks(self):
        self.write("notes.md", "# Notes\n")
        self.assertEqual(self.run_check(headings), [])


class TaskDecided(Base):
    def test_both_lines_pass(self):
        self.write("01-rows.task.md", TASK)
        self.assertEqual(self.run_check(decided), [])

    def test_bold_labels_pass(self):
        self.write("01-rows.task.md", TASK.replace("- Why handed over:", "**Why handed over:**").replace("- If the check fails:", "**If the check fails:**"))
        self.assertEqual(self.run_check(decided), [])

    def test_a_missing_line_fails(self):
        self.write("01-rows.task.md", TASK.replace("- If the check fails: ask once more with the failing test named, then do it at the lead.\n", ""))
        self.assertIn("If the check fails", self.run_check(decided)[0].message)

    def test_a_label_with_no_text_fails(self):
        self.write("01-rows.task.md", TASK.replace("the answer is checked by a program.", ""))
        self.assertIn("Why handed over", self.run_check(decided)[0].message)

    def test_a_task_without_decided_is_left_to_headings(self):
        self.write("01-rows.task.md", "# 01\n\n## Task\n\nx\n")
        self.assertEqual(self.run_check(decided), [])


class TaskChecks(Base):
    def test_a_command_passes(self):
        self.write("01-rows.task.md", TASK)
        self.assertEqual(self.run_check(commands), [])

    def test_no_item_fails(self):
        self.write("01-rows.task.md", TASK.split("## Checks")[0] + "## Checks\n\nIt should look right.\n")
        self.assertIn("no item", self.run_check(commands)[0].message)

    def test_items_with_no_command_fail(self):
        self.write("01-rows.task.md", TASK.split("## Checks")[0] + "## Checks\n\n- It reads well.\n")
        self.assertIn("none can be run", self.run_check(commands)[0].message)

    def test_one_item_without_a_command_warns(self):
        self.write("01-rows.task.md", TASK + "- It reads well.\n")
        findings = self.run_check(commands)
        self.assertEqual([f.kind for f in findings], ["warning"])



class ExchangePairs(Base):
    def git_free(self, files):
        for path, text in files.items():
            self.write(path, text)

    def test_a_pair_passes(self):
        self.git_free({"work/01-rows.task.md": TASK, "work/01-rows.result.md": RESULT})
        self.assertEqual(self.run_check(pairs), [])

    def test_a_task_waiting_for_its_result_passes(self):
        self.git_free({"work/01-rows.task.md": TASK})
        self.assertEqual(self.run_check(pairs), [])

    def test_a_result_without_a_task_fails(self):
        self.git_free({"work/02-rows.result.md": RESULT, "work/01-rows.task.md": TASK})
        self.assertIn("no task", self.run_check(pairs)[0].message)

    def test_the_task_must_be_in_the_same_folder(self):
        self.git_free({"a/01-rows.task.md": TASK, "b/01-rows.result.md": RESULT})
        self.assertEqual(len(self.run_check(pairs)), 1)

    def test_a_verdict_in_a_result_fails(self):
        self.git_free({"01-rows.task.md": TASK, "01-rows.result.md": RESULT + "\n## Verdict\n\nAccepted.\n"})
        self.assertIn("Verdict", self.run_check(pairs)[0].message)

    def test_a_verdict_heading_inside_the_worker_code_is_not_one(self):
        self.git_free({"01-rows.task.md": TASK, "01-rows.result.md": "```md\n## Verdict\n```\n"})
        self.assertEqual(self.run_check(pairs), [])

    def test_a_bad_name_fails(self):
        self.git_free({"rows.task.md": TASK, "01_Rows.task.md": TASK})
        self.assertEqual(len(self.run_check(pairs)), 2)

    def test_a_result_is_read_even_when_the_scope_excludes_it(self):
        self.git_free({"01-rows.task.md": TASK, "01-rows.result.md": RESULT + "\n## Review\n"})
        config = {"scope": {"exclude": ["*.result.md"]}}
        self.assertEqual(len(self.run_check(pairs, config)), 1)


ASKING = TASK.replace("The rows.", "The rows. End with a line `Cost: <n> tokens, <n> dollars, <n> minutes`.")


class ResultCost(Base):
    def test_a_result_with_a_cost_line_passes(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT + "Cost: 4000 tokens, 0.02 dollars, 3 minutes\n")
        self.assertEqual(self.run_check(cost), [])

    def test_a_missing_line_fails_when_the_task_asks(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT)
        self.assertIn("none", self.run_check(cost)[0].message)

    def test_a_task_that_does_not_ask_is_not_read(self):
        self.write("01-rows.task.md", TASK)
        self.write("01-rows.result.md", RESULT)
        self.assertEqual(self.run_check(cost), [])

    def test_a_unit_that_is_not_one_fails(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT + "Cost: 4 bananas\n")
        self.assertIn("bananas", self.run_check(cost)[0].message)

    def test_a_number_without_a_unit_fails(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT + "Cost: 4000\n")
        self.assertEqual(len(self.run_check(cost)), 1)

    def test_a_repeated_unit_fails(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT + "Cost: 4 minutes, 5 minutes\n")
        self.assertIn("twice", self.run_check(cost)[0].message)

    def test_the_line_is_read_in_a_result_the_scope_excludes(self):
        self.write("01-rows.task.md", ASKING)
        self.write("01-rows.result.md", RESULT)
        config = {"scope": {"exclude": ["*.result.md"]}}
        self.assertEqual(len(self.run_check(cost, config)), 1)


if __name__ == "__main__":
    unittest.main()
