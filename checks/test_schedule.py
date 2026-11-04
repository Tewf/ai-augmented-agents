"""Tests of protocols/schedule.py and of the result-cost check.

Run: python3 -m unittest discover -s checks -p 'test_*.py'
"""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("schedule_tool", REPOSITORY / "protocols" / "schedule.py")
schedule = importlib.util.module_from_spec(spec)
sys.modules["schedule_tool"] = schedule
spec.loader.exec_module(schedule)


def jobs(**rows):
    return schedule.parse({"jobs": rows})


class Path_(unittest.TestCase):
    def test_a_chain_is_its_own_critical_path(self):
        j = jobs(a={}, b={"after": ["a"]}, c={"after": ["b"]})
        self.assertEqual(schedule.critical_path(j), (["a", "b", "c"], 3))

    def test_the_longer_branch_wins_by_weight(self):
        j = jobs(a={}, fast={"after": ["a"]}, slow={"after": ["a"], "weight": 5}, end={"after": ["fast", "slow"]})
        self.assertEqual(schedule.critical_path(j), (["a", "slow", "end"], 7))

    def test_independent_jobs_share_one_wave(self):
        self.assertEqual(schedule.waves(jobs(a={}, b={}, c={})), [["a", "b", "c"]])

    def test_a_job_waits_for_the_deepest_predecessor(self):
        j = jobs(a={}, b={"after": ["a"]}, c={}, d={"after": ["b", "c"]})
        self.assertEqual(schedule.waves(j), [["a", "c"], ["b"], ["d"]])

    def test_the_waves_equal_the_unit_critical_path(self):
        j = jobs(a={}, b={"after": ["a"]}, c={"after": ["a"]}, d={"after": ["b", "c"]}, e={})
        self.assertEqual(len(schedule.waves(j)), schedule.critical_path(j)[1])


class Errors(unittest.TestCase):
    def test_a_cycle_is_refused(self):
        with self.assertRaisesRegex(schedule.ScheduleError, "cycle"):
            jobs(a={"after": ["b"]}, b={"after": ["a"]})

    def test_an_unknown_dependency_is_refused(self):
        with self.assertRaisesRegex(schedule.ScheduleError, "not a job"):
            jobs(a={"after": ["ghost"]})

    def test_a_negative_cost_is_refused(self):
        with self.assertRaisesRegex(schedule.ScheduleError, "cost"):
            jobs(a={"cost": -1})

    def test_no_jobs_is_refused(self):
        with self.assertRaises(schedule.ScheduleError):
            schedule.parse({})


class Spend(unittest.TestCase):
    def test_the_best_ratio_goes_first(self):
        j = jobs(cheap={"cost": 1, "gain": 1}, dear={"cost": 10, "gain": 5}, best={"cost": 2, "gain": 8})
        self.assertEqual(schedule.spend_order(j)[0], ["best", "cheap", "dear"])

    def test_a_job_waits_for_its_predecessor_even_if_it_ranks_higher(self):
        j = jobs(first={"cost": 10, "gain": 1}, second={"after": ["first"], "cost": 1, "gain": 100})
        self.assertEqual(schedule.spend_order(j)[0], ["first", "second"])

    def test_the_cap_leaves_out_what_no_longer_fits(self):
        j = jobs(a={"cost": 6, "gain": 6}, b={"cost": 5, "gain": 4}, c={"cost": 1, "gain": 1})
        chosen, left = schedule.spend_order(j, cap=7)
        self.assertEqual(chosen, ["a", "c"])
        self.assertEqual(left, ["b"])

    def test_a_job_without_a_gain_is_never_chosen(self):
        chosen, left = schedule.spend_order(jobs(a={"cost": 1}, b={"cost": 1, "gain": 1}))
        self.assertEqual((chosen, left), (["b"], ["a"]))

    def test_a_free_job_with_a_gain_comes_first(self):
        j = jobs(free={"gain": 1}, paid={"cost": 1, "gain": 100})
        self.assertEqual(schedule.spend_order(j)[0][0], "free")


class Compare(unittest.TestCase):
    def test_only_late_jobs_are_listed(self):
        j = jobs(a={"taken": 1}, b={"after": ["a"], "taken": 3}, c={"after": ["a"], "taken": 2}, d={})
        self.assertEqual(schedule.compare(j), [("b", 3, 2)])


class Files(unittest.TestCase):
    def test_the_example_loads_and_every_job_is_in_a_wave(self):
        j = schedule.load(REPOSITORY / "protocols" / "jobs.toml")
        self.assertEqual(sum(len(w) for w in schedule.waves(j)), len(j))

    def test_the_example_critical_path_is_the_design_chain(self):
        path, length = schedule.critical_path(schedule.load(REPOSITORY / "protocols" / "jobs.toml"))
        self.assertEqual((path[0], path[-1], length), ("review-b", "ide-spike-rerun", 7))

    def test_main_reports_a_bad_file_with_status_two(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "jobs.toml"
            bad.write_text("[jobs.a]\nafter = [\"a\"]\n")
            self.assertEqual(schedule.main([str(bad)]), 2)


RECORD = """[[job]]
id = "a"
minutes = 10

[[job]]
id = "b"
depends_on = ["a"]
minutes = 5

[[job]]
id = "c"
"""


class Records(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "jobs.toml"
        self.path.write_text(RECORD)

    def tearDown(self):
        self.dir.cleanup()

    def test_minutes_are_the_weight_and_depends_on_the_wait(self):
        j = schedule.load_records(self.path)
        self.assertEqual((j["b"]["after"], j["a"]["weight"], j["b"]["weight"]), (["a"], 10, 5))
        self.assertEqual(schedule.critical_path(j), (["a", "b"], 15))

    def test_a_job_without_minutes_keeps_the_default_weight(self):
        self.assertEqual(schedule.load_records(self.path)["c"]["weight"], 1)

    def test_the_waves_follow_depends_on(self):
        self.assertEqual(schedule.waves(schedule.load_records(self.path)), [["a", "c"], ["b"]])

    def test_main_accepts_jobs_and_a_row_with_the_replays_fields(self):
        self.path.write_text(RECORD.replace('id = "c"', 'id = "c"\nwave = 0\nkind = "build"\nagents = 1\ntokens_k = 230'))
        self.assertEqual(schedule.main(["--jobs", str(self.path)]), 0)

    def test_an_unknown_dependency_in_a_record_is_refused(self):
        self.path.write_text(RECORD.replace('["a"]', '["ghost"]'))
        self.assertEqual(schedule.main(["--jobs", str(self.path)]), 2)

    def test_two_jobs_with_one_id_are_refused(self):
        with self.assertRaisesRegex(schedule.ScheduleError, "two jobs"):
            schedule.from_records({"job": [{"id": "a"}, {"id": "a"}]})

    def test_a_file_and_jobs_together_are_refused(self):
        with self.assertRaises(SystemExit):
            schedule.main([str(self.path), "--jobs", str(self.path)])


if __name__ == "__main__":
    unittest.main()
