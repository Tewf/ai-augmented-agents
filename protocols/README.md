# Protocols

Procedures for a lead that runs many exchanges: which tier takes a task, in what order jobs run, and how a cap is spent. Each page follows the topic shape and links the exchange it extends.

## Contents

| Topic | Summary |
|---|---|
| [The maestro protocol](maestro.md) | tiers cheapest first, jobs in the waves their dependencies allow, a cap spent by gain per cost |
| [schedule.py](schedule.py) | prints the critical path, the waves, the jobs that ran late, and the order by gain per cost from a jobs file |
| [jobs.toml](jobs.toml) | the jobs of the maintainer's two days, with dependencies and cost estimates |

## See also

[The front page](../README.md); [the exchange shape](../shapes/exchange.md).
