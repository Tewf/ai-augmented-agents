# Run the checks at the lead

**Claim:** the lead runs the listed checks on every result before using it, at the centre, not delegated to the workers.

- **Grade:** measured for a central check containing error amplification, in one controlled study of model systems; convention for the same rule between a lead and a worker.
- **Evidence:** [the review](../../evidence/multi-agent-teams/review.md), strand C (Kim 2025: errors grew 17.2 times without centralised checking and 4.4 times with it, read) and Cemri 2025 (task verification as one of three failure groups).
- **Check:** `task-checks` (exact, with a warning): at least one check under Checks names a command or file in backticks, so the lead has something to run; a check that names none warns.
- **Reader styles:** none.

## What it asks

- Run each listed command on the result as it came, then write the outcome in the verdict ([keep the result untouched](keep-the-result-untouched.md)).
- Run them at the lead, not by asking the worker whether it passed.
- A check the lead cannot run is a question for a person, and says so.

## Why

- Errors passed between agents grow, and a central check cut the growth from 17.2 times to 4.4 times (Kim 2025).
- Task verification is one of the three groups of failure in 1,600+ traces of seven frameworks (Cemri 2025).
- A program can decide a command's outcome exactly, so the lead need not read the result to know whether it passed.

## Where it stops

- Kim 2025 tested model agents on benchmarks; a lead that runs one command per result is a reading of it, not a replica.
- The check stops what the listed checks can see: in the brief test, the full arm passed the cases it was shown.
- A command can run and still miss the point; the Checks are the lead's best attempt, not a proof.
