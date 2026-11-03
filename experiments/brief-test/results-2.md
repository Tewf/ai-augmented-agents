# Results: the brief test, round two

Calls to two model tiers, ten per cell, judged by hidden tests no arm saw; the visible tests are scored beside. Written by [run2.py](run2.py) from [results-2.jsonl](results-2.jsonl). What was run and what it cannot say are in the [protocol](protocol-2.md).

## Pooled over tasks and tiers

| Arm | Hidden pass | Visible pass | Replies with a question |
|---|---|---|---|
| no brief | 0/60 (0%) | 0/60 (0%) | 1 |
| convention brief | 30/60 (50%) | 38/60 (63%) | 0 |
| full brief | 29/60 (48%) | 42/60 (70%) | 1 |

## By tier

| Tier | no brief | convention brief | full brief |
|---|---|---|---|
| small hosted model | 0/30 (0%) | 8/30 (27%) | 8/30 (27%) |
| claude-haiku-5-5 | 0/30 (0%) | 22/30 (73%) | 21/30 (70%) |

## By task

| Task | no brief | convention brief | full brief |
|---|---|---|---|
| scope | 0/20 (0%) | 10/20 (50%) | 8/20 (40%) |
| changelog | 0/20 (0%) | 17/20 (85%) | 18/20 (90%) |
| llms | 0/20 (0%) | 3/20 (15%) | 3/20 (15%) |

## Every cell, hidden pass (visible pass)

| Tier | Task | no brief | convention brief | full brief |
|---|---|---|---|---|
| small hosted model | scope | 0/10 (0) | 0/10 (0) | 0/10 (2) |
| small hosted model | changelog | 0/10 (0) | 8/10 (9) | 8/10 (8) |
| small hosted model | llms | 0/10 (0) | 0/10 (1) | 0/10 (5) |
| claude-haiku-5-5 | scope | 0/10 (0) | 10/10 (10) | 8/10 (8) |
| claude-haiku-5-5 | changelog | 0/10 (0) | 9/10 (10) | 10/10 (10) |
| claude-haiku-5-5 | llms | 0/10 (0) | 3/10 (8) | 3/10 (9) |

## Round one beside

Round one's thirty replies (task scope, the small hosted model), judged by the visible tests as then, and rescored on the hidden tests of this round. The visible column reproduces [results.md](results.md).

| Arm | Visible pass (round one) | Hidden pass (rescored) |
|---|---|---|
| no brief | 0/10 | 0/10 |
| convention brief | 0/10 | 0/10 |
| full brief | 5/10 | 1/10 |

Calls recorded: 180; left as errors: 0.
