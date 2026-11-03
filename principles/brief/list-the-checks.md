# List the checks

**Claim:** a task file lists the checks that will judge the result, as commands, under four headings in a fixed order: Task, Decided, To find and Checks.

- **Grade:** convention for the four parts: one company advises them about its own system, with no ablation. Listing the checks as the lead's acceptance rule is a convention. As a way to raise a worker's pass rate on cases the brief never named, not supported: 29 of 60 hidden passes against 30 of 60 without the list, over three tasks and two tiers.
- **Evidence:** [the review](../../evidence/multi-agent-teams/review.md), strand E (Anthropic 2025 advises an objective, an output format, tools and boundaries). [The brief test](../../experiments/brief-test/results.md) passed 0, 0 and 5 runs of 10 across its three arms in round one. [Round two](../../experiments/brief-test/results-2.md) judged 180 calls on hidden cases and found no gain from the list; [decision 0005](../../decisions/0005-listing-the-checks-is-not-a-gain-on-unseen-cases.md) records the change of grade.
- **Check:** `task-headings` (exact): the four headings are present, in order, and none is empty; whether the checks are the right ones is judgment.
- **Reader styles:** none.

## What it asks

- Write the task as four headings. Task says what to do. Decided says what the worker must not reopen. To find says what to return. Checks lists how the result is judged.
- Under Checks, list each check as a command or a test the lead will run, then the cases it covers.
- Write the checks before the work leaves, not after the result arrives.

## Why

- In round one the convention alone did not help, and listing the checks moved the pass rate to 5 runs of 10.
- In round two the Decided lines moved the hidden pass rate from 0 of 60 to 30 of 60. Adding the list left it at 29 of 60, and raised the visible pass from 38 to 42 of 60.
- Round one's gain was following a list: rescored on hidden cases, its full arm passes 1 run of 10.
- A check stated in advance is also the lead's own acceptance rule, so it cannot bend to the result ([run the checks at the lead](../result/run-the-checks-at-the-lead.md)).

## Where it stops

- It does not show the convention helps: no study removes one field at a time (the review's finding 3).
- On the shown cases the list adds 4 passes of 60, inside the noise of ten runs per cell. The cases the models missed were stated in Decided, not in the list.
- Listing the checks asks the lead to know them first. Where nobody can say what right looks like, the work is not ready to hand over.
