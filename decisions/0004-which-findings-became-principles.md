# 0004: Five findings became principles, the rest stayed findings

**Decision:** A finding of the review became a principle when it graded measured or supported with caveat and a program can check how a task or result file follows it; the others stayed findings.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/shapes/decision-record.md).

## Context

- The extension contract asks for one principle file per rule, each with a grade and a check ([extending](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/extending.md)). The standard's `principle-coverage` check fails a principle whose Check line names no registered check.
- The review graded most findings convention or measured on a model benchmark. The brief test added one small result.
- The shape these principles serve is the [exchange](../shapes/exchange.md): a task file, a result file, and a verdict elsewhere.

## Decision

Five findings became principles, in two groups.

- Brief: [list the checks](../principles/brief/list-the-checks.md) (the brief test, supported with caveat), [say why it is handed over](../principles/brief/say-why-handed-over.md) (Kim 2025, measured), and [escalate on a failed check](../principles/brief/escalate-on-a-failed-check.md) (Chen 2023b, measured).
- Result: [run the checks at the lead](../principles/result/run-the-checks-at-the-lead.md) (Kim 2025, measured), and [keep the result untouched](../principles/result/keep-the-result-untouched.md) (convention, resting on Cemri 2025).
- Each names a check of its own in `checks/local/`: `task-headings`, `task-decided` (for two principles), `task-checks` and `exchange-pairs`.

These stayed findings:

- Vaccaro 2024: a person with a model lost to the better of the two on decision tasks. It describes one person and one system, not a lead and a worker.
- Bernstein 2002 and the economics of teams: theory about models, with no file a program can check.
- Kapoor 2024: benchmarks that omit cost mislead. It says how to read a result, not how to write a task.
- The brief convention alone (objective, format, tools, boundaries): convention, with no ablation. It stays a part of the shape, not a principle with a grade of its own.
- Incentives and counts of duplicated work: open, with no source.

## Consequences

- **Good:** every principle has a program behind it, with unit tests that CI runs.
- **Good:** the grade of a principle is the review's, never higher; the one new grade is for the brief test, labelled supported with caveat with its limits.
- **Bad:** the checks read form only. They find a missing "If the check fails" line, not a poor plan.
- **Bad:** most grades rest on one study of model systems, and the brief test is one task, one model and ten runs.
- **To keep it true:** a principle moves its grade only with a cited source, and a new finding of measured grade is listed here as a principle or as a finding that stayed.

## See also

[Decisions](README.md); [the review](../evidence/multi-agent-teams/review.md); [the standard card](../standard.md); [decision 0003](0003-the-brief-is-tested-on-one-small-task.md).
