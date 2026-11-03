# 0005: Listing the checks is not shown to help on cases the brief never named

**Decision:** The principle [list the checks](../principles/brief/list-the-checks.md) keeps its claim as an acceptance rule and loses its claim as a way to raise a worker's pass rate, because round two found no gain on hidden cases.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/shapes/decision-record.md).

## Context

- Round one ([decision 0003](0003-the-brief-is-tested-on-one-small-task.md)) found 5 passes of 10 with the checks listed and 0 without. Its full arm was judged by the cases it was shown.
- Round two ([protocol](../experiments/brief-test/protocol-2.md)) used three tasks, two model tiers, and hidden cases no arm saw. 180 calls, ten per cell. The [results](../experiments/brief-test/results-2.md) are the table.
- The protocol predicted, before any call, that the full arm beats the convention arm on hidden cases.

## Decision

- **Pooled, hidden pass:** no brief 0 of 60, convention brief 30 of 60, full brief 29 of 60.
- **Pooled, visible pass:** 0 of 60, 38 of 60, 42 of 60.
- The prediction failed. Full is level with convention on hidden cases in both tiers (small hosted model 8 and 8 of 30; claude-haiku-5-5 22 and 21 of 30).
- Listing the checks adds 4 passes of 60 on the cases it names. That is inside the noise of ten runs per cell.
- Round one's gain was following a list: rescored on hidden cases, its full arm passes 1 of 10, not 5.
- The Decided lines carry the effect: none to convention is 0 of 60 to 30 of 60. The arms differ in the function name and rules as well, so this does not isolate the convention's parts.
- On the `llms` task the cases failed most were stated in Decided only: text after the link with no colon is not a description (9 of 14 failing runs of the paid tier).
- Of the other predictions, the convention beats no brief, and the paid tier beats the small one in the convention and full arms (73% and 70% against 27%). Both held.
- The grade of the principle falls from "supported with caveat" for listing the checks to "not supported" for a gain on unseen cases; the acceptance-rule reading stays a convention.

## Consequences

- **Good:** the claim now matches what was measured, and the Decided lines are shown to matter.
- **Bad:** the two tiers differ in sampling (the paid model refuses a temperature), the hidden cases were written by the author of the visible ones, and three tasks are of one kind.
- A later run varies the Decided lines one at a time, or uses a task whose checks are not derivable from its Decided lines.
- 14 calls ended in network errors on the first pass and were redone on resume; none is left out of the table.

## See also

[Decisions](README.md); [round two protocol](../experiments/brief-test/protocol-2.md); [results](../experiments/brief-test/results-2.md); [the principle](../principles/brief/list-the-checks.md).
