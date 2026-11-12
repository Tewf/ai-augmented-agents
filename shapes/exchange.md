# Shape: exchange

This shape hands one piece of work from one agent to another and gets it back. The pair is the unit: one task, one result, one verdict.

- The lead writes a task file.
- The worker returns a result file.
- The lead's verdict goes in a third place.

## When to use it

- When work leaves the lead for another agent, a cheaper model or a person, and the lead will use what comes back.
- When the answer can be checked by a program, or by a reader who has the task in hand.
- Not for work the lead does itself: if the reason to hand it over is missing, do not hand it over ([say why it is handed over](../principles/brief/say-why-handed-over.md)).
- Not for a conversation: an exchange is one task and one result, not a thread.

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Name | `NN-slug.task.md` and `NN-slug.result.md` in one folder, so the pair is found by its name | the maintainer's practice, written down for the review | convention, untested |
| Task | what the worker does, in a few sentences | objective and output format are advised for a brief (Anthropic 2025) | convention, no ablation |
| Decided | what the worker must not reopen, why the work is handed over, and what happens if its check fails | the gain from several agents is set by the task (Kim 2025); a cascade climbs when a scorer rejects (Chen 2023b) | measured, for both findings; convention for writing them down |
| To find | what the result must contain, and in what shape | output format advised for a brief (Anthropic 2025) | convention, no ablation |
| Checks | the commands the lead runs on the result, each with the cases it covers | listing the checks moved a small model from 0 of 10 to 5 of 10 on one task (brief test) | supported with caveat |
| Result | the worker's reply, as it came | verification is one of three failure groups (Cemri 2025) | convention for keeping it apart |
| Cost line | the last line of the result, `Cost: <n> tokens, <n> dollars, <n> minutes`, so the lead can record what the work spent | the recorded quantities are what an allocation by gain per cost needs ([the maestro protocol](../protocols/maestro.md)) | convention, untested |
| Verdict | the lead's outcome of the checks, in another file that links the result | errors grew 17.2 times without a central check and 4.4 times with one (Kim 2025) | measured, for the central check |

Whether the shape as a whole helps is untested: the [baseline](../evidence/multi-agent-teams/baseline.md) names the arrangement it should be compared with. Each key (Author Year) is listed in the [bibliography](../evidence/bibliography.md).

## The principles it applies

| Part | Principle |
|---|---|
| Checks listed in advance | [list the checks](../principles/brief/list-the-checks.md) |
| The line "Why handed over" | [say why it is handed over](../principles/brief/say-why-handed-over.md) |
| The line "If the check fails" | [escalate on a failed check](../principles/brief/escalate-on-a-failed-check.md) |
| The verdict after the checks are run | [run the checks at the lead](../principles/result/run-the-checks-at-the-lead.md) |
| The result file kept apart from the verdict | [keep the result untouched](../principles/result/keep-the-result-untouched.md) |
| The answer first, the section labels | [overview first](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/document/overview-first.md) |

## The skeleton

The task file, `NN-slug.task.md`:

```markdown
# NN: <the work in one line>

**Shape:** [exchange](https://github.com/Tewf/ai-augmented-agents/blob/master/shapes/exchange.md)

**Result:** `NN-slug.result.md`, in this folder.

## Task

<What the worker does, in a few sentences.>

## Decided

- Why handed over: <what makes this work cheaper or better away from the lead>.
- Worker: <the kind of agent it goes to>.
- If the check fails: <the next step: a retry with the failing case named, a stronger worker, or the lead>.
- <Each choice already made that the worker must not reopen.>

## To find

<What the result must contain, and its shape. End with a line `Cost: <n> tokens, <n> dollars, <n> minutes`.>

## Checks

- Run `<command>` on the result. It passes when <the condition>.
  - <A case the command covers.>
```

The result file, `NN-slug.result.md`, is the worker's reply, saved as it came. It has no skeleton: nothing is added to it, but when the task asks, the reply ends with its Cost line.

The verdict is a line or a row in a file of the lead's, such as a log of results, naming the result file, the commands run and their outcome.

## The rules

1. One task, one result: the pair shares a number and a slug, and sits in one folder.
2. The task opens with the four headings Task, Decided, To find and Checks, in that order, none empty.
3. Decided holds the line "Why handed over" and the line "If the check fails", each with text.
4. Checks lists commands the lead runs. A check no program can run is written as a question for a person, and says so.
5. The checks are written before the work leaves.
6. The result is never edited, and holds no verdict: no section named Verdict, Review, Accepted, Rejected or Decision.
7. The verdict names the result and the checks run on it, and lives in another file.

8. A task that asks for it ends To find with the Cost line, and the result then ends with a line `Cost:` of numbers with units from tokens, points, dollars and minutes, each at most once. The worker states it; the lead may correct it in the verdict, never in the result.

## Worked example

A filled exchange, from the brief test: [the task](examples/01-scope-table.task.md) and [the result](examples/01-scope-table.result.md), a reply saved as it came. The verdict is the passing line of run 3 of the full arm in the [brief test's results](../experiments/brief-test/results.jsonl). It carries the Shape line, so the checks run on it as on any task of yours.
