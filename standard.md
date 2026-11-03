# The agents standard

What handing work from one agent to another shares, as far as the evidence goes. It covers the task file the lead writes, the result file the worker returns, and the checks the lead runs on it. It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/standard.md), the standard for any reader: read that one first. This page adds only what several agents change, since the reader of a task is a worker that knows nothing else.

The evidence is one review of 35 sources and one small run on the brief ([evidence](evidence/README.md), [experiments](experiments/README.md)). It is a first pass, not a result.

Grades mean what they mean in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/standard.md#grades). Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Brief: what a task file holds

| Principle | Claim | Grade |
|---|---|---|
| [Escalate on a failed check](principles/brief/escalate-on-a-failed-check.md) | a task file says what happens when its check fails, by default a stronger worker or the lead, never an unchecked retry. | measured for cascades that try a cheaper model first and stop when a scorer accepts, on three datasets and three public benchmarks; convention for writing the rule into the task file |
| [List the checks](principles/brief/list-the-checks.md) | a task file lists the checks that will judge the result, as commands, under four headings in a fixed order: Task, Decided, To find and Checks. | convention for the four parts: one company advises them about its own system, with no ablation. Supported with caveat for listing the checks, from one run of one task and one small model |
| [Say why it is handed over](principles/brief/say-why-handed-over.md) | a task file says why this work leaves the lead, with the lead doing it alone as the default. | measured for the size and the sign of the gain depending on the task; convention for writing the reason into the task file |

### Result: what comes back

| Principle | Claim | Grade |
|---|---|---|
| [Keep the result untouched](principles/result/keep-the-result-untouched.md) | the result file stays as the worker wrote it, and the lead's verdict is written in another file that links it. | convention for the arrangement; the reason it rests on, that verification fails when it is left to the producer, is measured descriptively (Cemri 2025) |
| [Run the checks at the lead](principles/result/run-the-checks-at-the-lead.md) | the lead runs the listed checks on every result before using it, at the centre, not delegated to the workers. | measured for a central check containing error amplification, in one controlled study of model systems; convention for the same rule between a lead and a worker |

<!-- principles:end -->

## Where the evidence is

Every principle links its review in [evidence/](evidence/README.md), and every work cited is listed once in the [bibliography](evidence/bibliography.md).
