# Keep the result untouched

**Claim:** the result file stays as the worker wrote it, and the lead's verdict is written in another file that links it.

- **Grade:** convention for the arrangement; the reason it rests on, that verification fails when it is left to the producer, is measured descriptively (Cemri 2025).
- **Evidence:** [the review](../../evidence/multi-agent-teams/review.md) holds that task verification is one of three failure groups, among 14 modes (strand C, Cemri 2025). The [position](../../evidence/multi-agent-teams/position.md) keeps what is known apart from what is done here.
- **Check:** `exchange-pairs` (exact): each result has a task of the same name in its folder, and holds no section named Verdict, Review, Accepted, Rejected or Decision.
- **Reader styles:** none.

## What it asks

- Name the pair `NN-slug.task.md` and `NN-slug.result.md`, in one folder.
- Do not edit the result, and do not append the verdict to it.
- Write the verdict in a file of the lead's, such as a log of verdicts or a results table, that links the result and the checks run on it.

## Why

- A result edited after the fact can no longer be checked against what the worker returned.
- Where the verdict lives apart, the same result can be re-judged by a later check without a trace of an earlier opinion.
- It keeps the worker's output and the lead's judgment as two things, which is the separation the central check needs.

## Where it stops

- No program can tell that a result is untouched; it can only tell that the file holds no section of the lead's.
- A result in a tool's own format may not be a markdown file; the pair rule then applies to the notes beside it.
- The arrangement is the maintainer's convention; no source compares it with a result annotated in place.
