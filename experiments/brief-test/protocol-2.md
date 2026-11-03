# Protocol: the brief test, round two

Written before any call of round two. It answers the limits of [round one](protocol.md): one task, one model, and a full arm judged by the cases it was shown. The numbers will be in [results-2.md](results-2.md).

## Question

Does listing the checks in the brief raise the pass rate on cases the brief never showed, across three tasks and two model tiers?

## What changes from round one

| Round one | Round two |
|---|---|
| one task | three tasks of the same kind: parse a small Markdown shape into a list |
| one model, a small hosted one | two tiers: that same small hosted model, and a small model of another vendor, hosted, paid |
| judged by the cases the full arm was shown | judged by hidden cases no arm sees; the visible cases are scored too, beside |
| thirty calls | 180 calls: 3 tasks, 3 arms, 2 tiers, 10 runs |

## Tasks

| Task | Function | Source of the shape |
|---|---|---|
| scope | `scope_in_rows` | round one's task, kept |
| changelog | `changelog_releases` | release headings of a Keep a Changelog file |
| llms | `llms_links` | link lines of an `llms.txt` file |

The prompts are constants in [tasks2.py](tasks2.py). The arms are those of round one: the task sentence alone (none), the convention with its Decided lines (convention), the convention plus the list of checks (full).

## Two test sets per task

- **Visible:** the cases the list of checks in the full arm names, one line each. Files: [judge_tests.py](judge_tests.py), [changelog_visible.py](tasks/changelog_visible.py), [llms_visible.py](tasks/llms_visible.py).
- **Hidden:** six to eight cases that appear in no prompt. Each follows from the Decided lines alone, so a worker that reads them closely can pass without being told. Files: [scope_hidden.py](tasks/scope_hidden.py), [changelog_hidden.py](tasks/changelog_hidden.py), [llms_hidden.py](tasks/llms_hidden.py).
- The hidden files are in the repository, hidden from the model, not from the reader.

## Judge

A program, never the model.

- **Primary outcome: the hidden pass.** The code blocks of the reply, joined, import without error and pass every hidden case within 20 seconds.
- **Secondary: the visible pass,** by the same rules. The gap between the two, in the full arm, is how much the arm only follows its list.
- Questions are counted as in round one. A reply with no code fails.
- The judge is tested: [test_run2.py](test_run2.py) checks that a reference solution passes both sets, and that empty, wrong, misnamed and hanging code fail.

## Design

- Ten runs per task per arm per tier. Runs are interleaved across tiers, tasks and arms, so drift falls on all cells alike.
- Same sampling settings within a tier. The hosted small model's wrapper sets temperature 0.2; the paid model refuses a temperature (its API reports the parameter as deprecated), so it runs at its default. The tiers therefore differ in sampling as well as in model.
- A failed call is retried once; a call that fails twice is recorded as an error, left out of the rates, and tried again when the run is resumed.
- The paid tier is called with the Messages API through urllib ([claude_call.py](claude_call.py)). Its key is read into the environment of the run only, never printed or stored.
- Every reply and verdict is kept in [results-2.jsonl](results-2.jsonl), written as each call ends.

## Predictions

Written now, so the result can disagree with them.

1. Full beats convention on the hidden set in both tiers, by less than on the visible set.
2. The convention arm beats none on the hidden set, because the function name and rules are given.
3. The paid tier passes more than the small hosted one in every arm.

## What the run cannot say

- **Three tasks of one kind,** parsers for a line-based Markdown shape. It says nothing of design, search or long tasks.
- **Two tiers,** each one model on one day.
- **The hidden cases were written by the author of the visible ones,** who knows which cases a model tends to miss. They are not a random draw of the cases a user might care about.
- **Ten runs per cell** give wide intervals; a gap of one or two runs is noise. A table of 18 cells invites a pattern read into noise, so the pooled rates by arm and by tier are the headline.
- **The arms differ by more than information,** as in round one: the name and the output shape are in the convention arm only.
- **No cost.** Tokens and the time to write a brief are not measured.
- **A pass is not quality.**

## Reproduce

```sh
python3 run2.py            # needs the two commands below; resumes from results-2.jsonl
python3 run2.py --only-report
python3 -m unittest test_run2
```

The hosted small model is reached through a command that takes the prompt as its one argument, set in `BRIEF_TEST_SMALL`; the paid tier through `claude_call.py` with `ANTHROPIC_API_KEY` in the environment.
