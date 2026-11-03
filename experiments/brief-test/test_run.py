"""Tests of run.py: the parts that are code, with no network. Run with: python3 -m unittest test_run"""
import unittest

import run

REFERENCE = (run.HERE / "reference.py").read_text(encoding="utf-8")


class Prompts(unittest.TestCase):
    def test_arms_nest(self):
        self.assertIn(run.TASK.split(",")[0], run.TASK)
        self.assertTrue(run.prompt_for("full").startswith(run.prompt_for("convention")))
        self.assertGreater(len(run.prompt_for("convention")), len(run.prompt_for("none")))

    def test_none_has_no_function_name(self):
        self.assertNotIn("scope_in_rows", run.prompt_for("none"))
        self.assertIn("scope_in_rows", run.prompt_for("convention"))

    def test_only_full_lists_checks(self):
        self.assertNotIn("judged by", run.prompt_for("convention"))
        self.assertIn("judged by", run.prompt_for("full"))

    def test_unknown_arm(self):
        with self.assertRaises(ValueError):
            run.prompt_for("other")


class Extraction(unittest.TestCase):
    def test_joins_blocks(self):
        reply = "Here:\n```python\nx = 1\n```\nand\n```python\ny = 2\n```\n"
        self.assertEqual(run.extract_code(reply), "x = 1\n\ny = 2")

    def test_no_block(self):
        self.assertEqual(run.extract_code("no code"), "")

    def test_questions_outside_code_only(self):
        reply = "Which dialect?\nAnd what about empty rows?\n```python\n# is this a question?\nx = 1\n```\nDone."
        self.assertEqual(run.count_questions(reply), 2)

    def test_no_question(self):
        self.assertEqual(run.count_questions("```python\nx = 1\n```"), 0)


class Judge(unittest.TestCase):
    def test_reference_passes(self):
        self.assertEqual(run.judge(REFERENCE), (True, "ok"))

    def test_empty_fails(self):
        self.assertEqual(run.judge(""), (False, "no code"))

    def test_wrong_function_fails(self):
        passed, _ = run.judge("def scope_in_rows(markdown):\n    return []\n")
        self.assertFalse(passed)

    def test_wrong_name_fails(self):
        passed, _ = run.judge(REFERENCE.replace("scope_in_rows", "other_name"))
        self.assertFalse(passed)

    def test_hang_times_out(self):
        passed, detail = run.judge("while True:\n    pass\n", timeout=2)
        self.assertEqual((passed, detail), (False, "timeout"))

    def test_candidate_main_guard_not_run(self):
        passed, _ = run.judge(REFERENCE + "\nif __name__ == '__main__':\n    raise SystemExit(3)\n")
        self.assertTrue(passed)


class FailingTests(unittest.TestCase):
    def test_names_the_failing_test(self):
        code = "def scope_in_rows(markdown):\n    return []\n"
        names = run.failing_tests(code)
        self.assertIn("test_lists_in_rows_in_order", names)
        self.assertNotIn("test_no_table", names)

    def test_none_for_reference(self):
        self.assertEqual(run.failing_tests(REFERENCE), [])

    def test_empty(self):
        self.assertEqual(run.failing_tests(""), [])


class Summary(unittest.TestCase):
    def test_rates_and_errors(self):
        rows = [
            {"arm": "none", "run": 1, "error": "", "passed": False, "detail": "no code", "questions": 2},
            {"arm": "none", "run": 2, "error": "", "passed": True, "detail": "ok", "questions": 0},
            {"arm": "none", "run": 3, "error": "timeout", "passed": False, "detail": "timeout", "questions": 0},
        ]
        s = run.summarize(rows)["none"]
        self.assertEqual((s["calls"], s["errors"], s["valid"], s["passes"]), (3, 1, 2, 1))
        self.assertEqual((s["rate"], s["questions"], s["asked"], s["no_code"]), (0.5, 2, 1, 1))
        self.assertIsNone(run.summarize(rows)["full"]["rate"])


if __name__ == "__main__":
    unittest.main()
