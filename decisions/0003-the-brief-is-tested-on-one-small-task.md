# 0003: The brief is tested on one small task first

**Decision:** The review's finding that the brief has a convention and no test is answered by a small run: one task with a checkable answer, three briefs, ten runs each, judged by a program.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The review found a brief convention (objective, output format, tools, boundaries) advised by one company about its own system, and no study that removes a field.
- A test needs an answer a program can check. Parsing the scope table every repository of this family opens with has one.
- The free tier of a small hosted model costs nothing, so thirty calls are affordable. A larger or paid run is not.

## Decision

- The task, arms, judge and limits are in the [protocol](../experiments/brief-test/protocol.md). The code is [run.py](../experiments/brief-test/run.py), with its own tests.
- The three arms are no brief, the convention brief, and the convention plus the checks the answer is judged by.
- The judge is a program. A model never decides a pass.
- The model tier is named ("a small hosted model"), not the product.

## Consequences

- First result ([results](../experiments/brief-test/results.md)): 0 of 10 passed with no brief, 0 of 10 with the convention, 5 of 10 with the checks added. No arm asked a question.
- The convention alone did not help on this task. Its failures cluster on two cases it never stated: a blank header cell and an empty cell. The gain came from listing the checks.
- **Bad:** one task, one model, ten runs, and the full arm is shown the cases it is judged by. The result is a first data point, not a measure of the effect.
- A later run varies the task or the model, or removes one field of the convention at a time.

## See also

[Decisions](README.md); [the protocol](../experiments/brief-test/protocol.md); [the review's finding on the brief](../evidence/multi-agent-teams/review.md).
