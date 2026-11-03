# List the checks

**Claim:** a task file lists the checks that will judge the result, as commands, under four headings in a fixed order: Task, Decided, To find and Checks.

- **Grade:** convention for the four parts: one company advises them about its own system, with no ablation. Supported with caveat for listing the checks, from one run of one task and one small model.
- **Evidence:** [the review](../../evidence/multi-agent-teams/review.md), strand E (Anthropic 2025 advises an objective, an output format, tools and boundaries). [The brief test](../../experiments/brief-test/results.md) passed 0, 0 and 5 runs of 10 across its three arms, and [decision 0003](../../decisions/0003-the-brief-is-tested-on-one-small-task.md) records why it was run.
- **Check:** `task-headings` (exact): the four headings are present, in order, and none is empty; whether the checks are the right ones is judgment.
- **Reader styles:** none.

## What it asks

- Write the task as four headings. Task says what to do. Decided says what the worker must not reopen. To find says what to return. Checks lists how the result is judged.
- Under Checks, list each check as a command or a test the lead will run, then the cases it covers.
- Write the checks before the work leaves, not after the result arrives.

## Why

- In the brief test the convention alone did not help: all 10 runs of that arm failed on the empty cell, a case the convention never stated.
- Listing the checks was the one change that moved the pass rate, to 5 runs of 10.
- A check stated in advance is also the lead's own acceptance rule, so it cannot bend to the result ([run the checks at the lead](../result/run-the-checks-at-the-lead.md)).

## Where it stops

- It does not show the convention helps: no study removes one field at a time (the review's finding 3).
- The full arm saw the cases it was judged by, so it measures how well a model follows a list, not how well it generalises.
- Listing the checks asks the lead to know them first. Where nobody can say what right looks like, the work is not ready to hand over.
