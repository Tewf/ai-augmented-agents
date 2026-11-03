# Protocol: does the brief matter for a small model

Step 5 follow-up of the [review](../../evidence/multi-agent-teams/README.md), finding 3: the brief has a convention and no test. This file says what is run, how it is judged, and what the run cannot show. The numbers are in [results.md](results.md).

## Question

For a small hosted model given one task with a checkable answer, does adding a brief change how often the answer passes, and how often the model asks instead of answering?

## Task

One sentence, the same in all arms: write a Python function that parses a Markdown scope table and lists its "in" rows, and tests for it. The table is the one every repository of this family opens with (columns: blank, What, Why).

## Arms

| Arm | The model receives | Grade of the idea |
|---|---|---|
| none | the task sentence alone | the control |
| convention | task, what is decided, what is to be found, output shape | the convention the review found, advised by one company about its own system |
| full | the convention plus the eleven checks the answer will be judged by | the convention plus a stated oracle |

The prompts are in [run.py](run.py), as constants, so the text run is the text read.

## Design

- Ten runs per arm, thirty calls. The arm is the only thing that varies: same model, same sampling settings, same task.
- Runs are interleaved by arm, so a drift in the service over the session falls on all arms alike.
- The model is a small hosted model, the free tier of its vendor. Its sampling is not seeded by us, so the ten runs of an arm are ten draws.
- A failed call is retried once. A call that fails twice is recorded as an error and left out of the rates.

## Judge

A program, never the model.

- **Pass:** the code blocks of the reply, joined, import without error and `scope_in_rows` passes all thirteen tests of [judge_tests.py](judge_tests.py), within 20 seconds. A reply with no code block fails.
- **A model's own tests count against it:** if they sit at the top level of the code and fail, the import fails. This is a choice: code that ships a failing test is not a pass.
- **Questions:** lines of the reply, outside code blocks, that end with a question mark. A heuristic: it counts a rhetorical question and misses a request without a mark.
- **The judge itself is tested:** [test_run.py](test_run.py) checks that a reference solution passes, that empty, wrong, misnamed and hanging code fail, and that the counts are right.

## What the run cannot say

- **One task, one model, one day.** The size of the effect on another task or model is not measured.
- **The arms differ by more than information.** The function name and the output shape are in the convention arm only, so the none arm can fail on a name the task never gave. That is the point of a brief, and it also means the arms measure a name as much as a quality.
- **The full brief gives the judge's cases.** The full arm is judged by the checks it was shown, so it measures how well a model follows a list, not how well it generalises. The eleven lines of the list cover the thirteen tests: the two empty-input tests share a line, as do the two newline tests.
- **Ten runs per arm** give wide intervals; a gap of one or two runs is noise.
- **No cost.** Tokens and the time to write a brief were not measured, so this does not answer when delegating pays.
- **A pass is not quality.** The tests check behaviour on small inputs, not style or robustness.

## Reproduce

```sh
BRIEF_TEST_COMMAND=<a command taking the prompt as one argument and printing the reply> python3 run.py
python3 -m unittest test_run
```

`results.jsonl` holds every reply and verdict; `python3 run.py --only-report` rebuilds [results.md](results.md) from it.
