"""Tests of run2.py and tasks2.py: the parts that are code, with no network. Run with: python3 -m unittest test_run2"""
import unittest

import run2
import tasks2


def ref(task):
    return tasks2.REFERENCE[task].read_text(encoding="utf-8")


class Prompts(unittest.TestCase):
    def test_arms_nest(self):
        for t in tasks2.TASKS:
            self.assertTrue(tasks2.prompt_for(t, "full").startswith(tasks2.prompt_for(t, "convention")))
            self.assertGreater(len(tasks2.prompt_for(t, "convention")), len(tasks2.prompt_for(t, "none")))

    def test_only_full_lists_checks(self):
        for t in tasks2.TASKS:
            self.assertNotIn("judged by", tasks2.prompt_for(t, "convention"))
            self.assertIn("judged by", tasks2.prompt_for(t, "full"))

    def test_unknown_arm(self):
        with self.assertRaises(ValueError):
            tasks2.prompt_for("scope", "other")

    def test_hidden_cases_not_in_prompts(self):
        for t in tasks2.TASKS:
            self.assertNotIn("candidate", tasks2.prompt_for(t, "full"))


class Judge(unittest.TestCase):
    def test_reference_passes_both_sets(self):
        for t in tasks2.TASKS:
            code = "```python\n" + ref(t) + "\n```"
            self.assertEqual(run2.judge_both(t, code)[:2], (True, True), t)

    def test_empty_and_wrong_fail(self):
        for t in tasks2.TASKS:
            self.assertEqual(run2.judge_both(t, "no code")[:2], (False, False))
            self.assertEqual(run2.judge_both(t, "```python\ndef nothing():\n    return []\n```")[:2], (False, False))

    def test_hang_times_out(self):
        self.assertEqual(run2.judge_file("while True:\n    pass\n", tasks2.HIDDEN["scope"], timeout=2), (False, "timeout"))

    def test_visible_only_code_fails_hidden(self):
        code = "```python\ndef scope_in_rows(markdown):\n    return ['delegation', 'coordination', 'incentives']\n```"
        h, v, _ = run2.judge_both("scope", code)
        self.assertFalse(h)


class Extraction(unittest.TestCase):
    def test_fence_mentioned_in_code_does_not_end_the_block(self):
        reply = "Here:\n```python\nx = line.startswith(\"```\")\n```\nDone."
        self.assertEqual(run2.extract_code(reply), 'x = line.startswith("```")')

    def test_no_block(self):
        self.assertEqual(run2.extract_code("no code"), "")


class Report(unittest.TestCase):
    def test_rate(self):
        rows = [{"error": "", "hidden": True}, {"error": "", "hidden": False}, {"error": "x", "hidden": False}]
        self.assertEqual(run2.rate(rows), (1, 2))
        self.assertEqual(run2.fmt(1, 2), "1/2 (50%)")


if __name__ == "__main__":
    unittest.main()
