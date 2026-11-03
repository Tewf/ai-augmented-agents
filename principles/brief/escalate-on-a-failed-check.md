# Escalate on a failed check

**Claim:** a task file says what happens when its check fails, by default a stronger worker or the lead, never an unchecked retry.

- **Grade:** measured for cascades that try a cheaper model first and stop when a scorer accepts, on three datasets and three public benchmarks; convention for writing the rule into the task file.
- **Evidence:** [the review](../../evidence/multi-agent-teams/review.md) holds that a cascade matched the best single model at 98.3%, 73.3% and 59.2% lower cost on three datasets (strand D, Chen 2023b). Routers cut cost by over 2 times in certain cases (Ong 2024, read in part).
- **Check:** `task-decided` (exact): Decided holds a line "If the check fails:" with text after it; whether the next step is sensible is judgment.
- **Reader styles:** none.

## What it asks

- Put a line "If the check fails:" under Decided.
- Name the next step: a retry that adds the failing case, a stronger worker, or the lead.
- Treat the listed checks as the scorer that decides whether to climb.

## Why

- A cascade saves cost because a scorer says when the cheap answer is good enough; without the scorer, there is nothing to escalate on (Chen 2023b).
- A rule written before the work leaves means the lead does not decide under the pull of a result that is nearly right.

## Where it stops

- The cascade studies measure questions with a scorer; they do not price the lead's time to brief and to check.
- A retry that only repeats the call is not escalation: on the brief test, no run asked a question, and the same prompt gave both passes and fails.
- Whether a stronger worker is worth its cost is an open price, not a rule.
