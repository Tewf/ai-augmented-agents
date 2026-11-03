"""Schedule: read jobs.toml and print the critical path, the parallel waves and a spend order.

jobs.toml holds one table per job under [jobs.<name>] with
  after = ["other", ...]   the jobs that must finish first (default none)
  weight = 1               the job's length in the unit chosen for the file (default 1: one wave)
  cost = 150               the estimate of what the job spends (default 0), in one unit for the whole file
  gain = 3                 the maintainer's estimate of what the job is worth (optional)
  taken = 4                the wave the job was actually run in (optional), for the comparison
The caller owns the units. Every number is an estimate until the quantities are recorded (protocols/maestro.md).

Run: python3 protocols/schedule.py protocols/jobs.toml [--rank] [--cap N] [--compare]
Time O(jobs + dependencies) for the path and waves; O(jobs squared) for the capped order.
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path


class ScheduleError(ValueError):
    """The file is not a schedule: an unknown dependency, a cycle, a negative number."""


def load(path: Path) -> dict[str, dict]:
    with open(path, "rb") as handle:
        return parse(tomllib.load(handle))


def parse(data: dict) -> dict[str, dict]:
    jobs = {}
    for name, row in data.get("jobs", {}).items():
        job = {"after": list(row.get("after", [])), "weight": row.get("weight", 1), "cost": row.get("cost", 0),
               "gain": row.get("gain"), "taken": row.get("taken")}
        for key in ("weight", "cost"):
            if not isinstance(job[key], (int, float)) or job[key] < 0:
                raise ScheduleError(f"{name}: {key} must be a number, zero or more")
        jobs[name] = job
    if not jobs:
        raise ScheduleError("no jobs")
    for name, job in jobs.items():
        for before in job["after"]:
            if before not in jobs:
                raise ScheduleError(f"{name}: waits for '{before}', which is not a job")
    order(jobs)
    return jobs


def order(jobs: dict[str, dict]) -> list[str]:
    """The jobs with every job after the jobs it waits for; raises on a cycle."""
    done: list[str] = []
    state: dict[str, int] = {}

    def visit(name: str, trail: list[str]) -> None:
        if state.get(name) == 2:
            return
        if state.get(name) == 1:
            raise ScheduleError("cycle: " + " -> ".join(trail[trail.index(name):] + [name]))
        state[name] = 1
        for before in sorted(jobs[name]["after"]):
            visit(before, trail + [name])
        state[name] = 2
        done.append(name)

    for name in sorted(jobs):
        visit(name, [])
    return done


def times(jobs: dict[str, dict]) -> dict[str, tuple[float, float]]:
    """Earliest (start, finish) of each job with unlimited workers."""
    when: dict[str, tuple[float, float]] = {}
    for name in order(jobs):
        start = max((when[b][1] for b in jobs[name]["after"]), default=0)
        when[name] = (start, start + jobs[name]["weight"])
    return when


def critical_path(jobs: dict[str, dict]) -> tuple[list[str], float]:
    """The longest chain of dependent jobs and its length: no schedule is shorter (Kelley 1959)."""
    when = times(jobs)
    end = max(sorted(when), key=lambda n: when[n][1])
    path = [end]
    while jobs[path[-1]]["after"]:
        path.append(max(sorted(jobs[path[-1]]["after"]), key=lambda n: when[n][1]))
    return path[::-1], when[end][1]


def waves(jobs: dict[str, dict]) -> list[list[str]]:
    """Wave k holds the jobs whose longest chain of predecessors has k jobs: all start together, none waits needlessly."""
    level: dict[str, int] = {}
    for name in order(jobs):
        level[name] = 1 + max((level[b] for b in jobs[name]["after"]), default=-1)
    return [sorted(n for n in level if level[n] == k) for k in range(max(level.values()) + 1)]


def ratio(job: dict) -> float:
    """Expected gain per unit of cost; a job with no gain estimate ranks last, a free job with a gain first."""
    if job["gain"] is None:
        return float("-inf")
    return float("inf") if job["cost"] == 0 and job["gain"] > 0 else job["gain"] / job["cost"] if job["cost"] else 0.0


def spend_order(jobs: dict[str, dict], cap: float | None = None) -> tuple[list[str], list[str]]:
    """Run order by gain per cost among the jobs whose predecessors are chosen; with a cap, jobs that no longer fit are left out.

    Returns (chosen, left out). A job with no gain estimate is never chosen: the order is only as good as the estimates.
    """
    chosen: list[str] = []
    spent = 0.0
    while True:
        ready = [n for n in sorted(jobs) if n not in chosen and jobs[n]["gain"] is not None
                 and all(b in chosen for b in jobs[n]["after"])
                 and (cap is None or spent + jobs[n]["cost"] <= cap)]
        if not ready:
            break
        best = max(ready, key=lambda n: ratio(jobs[n]))
        chosen.append(best)
        spent += jobs[best]["cost"]
    return chosen, [n for n in sorted(jobs) if n not in chosen]


def compare(jobs: dict[str, dict]) -> list[tuple[str, int, int]]:
    """(job, wave taken, earliest wave) for each job that ran later than it could."""
    level = {n: k + 1 for k, wave in enumerate(waves(jobs)) for n in wave}
    return [(n, jobs[n]["taken"], level[n]) for n in sorted(jobs)
            if jobs[n]["taken"] is not None and jobs[n]["taken"] > level[n]]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("file", type=Path)
    parser.add_argument("--rank", action="store_true", help="print the order by expected gain per cost")
    parser.add_argument("--cap", type=float, help="with --rank, stop at this total cost")
    parser.add_argument("--compare", action="store_true", help="print the jobs that ran later than the first wave they could")
    args = parser.parse_args(argv)
    try:
        jobs = load(args.file)
    except (OSError, tomllib.TOMLDecodeError, ScheduleError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    path, length = critical_path(jobs)
    print(f"critical path ({length:g}): " + " -> ".join(path))
    for k, wave in enumerate(waves(jobs), 1):
        print(f"wave {k}: " + ", ".join(wave))
    if args.compare:
        late = compare(jobs)
        used = max((j["taken"] for j in jobs.values() if j["taken"] is not None), default=0)
        print(f"waves taken: {used}; waves needed: {len(waves(jobs))}; jobs run late: {len(late)}")
        for name, taken, first in late:
            print(f"  {name}: wave {taken}, could start in wave {first}")
    if args.rank:
        chosen, left = spend_order(jobs, args.cap)
        print("order by gain per cost: " + (", ".join(chosen) or "none (no job has a gain estimate)"))
        if left:
            print("not chosen: " + ", ".join(left))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
