# Baseline: the arrangement this strand is compared against

Step 5 of the review. It names the baseline, says what it measured, and says how the strand would be compared. The facts about the arrangement are the maintainer's practice, written down for this review. Keys are in the [bibliography](../bibliography.md).

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/baseline.md)

## B1, one lead with a central check

**B1** is the arrangement named in [multi-agent-teams baseline](../multi-agent-teams/baseline.md): one coordinating session, workers that return results, and a check the lead runs on each result.

| Part | What B1 does | Quantity | Recorded |
|---|---|---|---|
| Raters | one rater per result, from one family | rho | no |
| Batches | jobs run in waves of several at once | batch regret | no |
| Passes | the lead re-reads a result and corrects it | lambda | no |
| Links | a result passes from worker to lead | error per link | no |

## Compared with the best found

The best found is the central check of Kim 2025, which B1 matches in kind. The proofs add three things B1 does not record: a second rater from another family, the batch factor, and lambda.

## How the strand would be measured against B1

- Record, for a month of work, the four quantities of [review](review.md) from the exchange logs and the checks' output.
- Compare a second rater from another family against the same rater twice, on the same items, by rho.
- The review is finished: B1 is named, and the comparison is the four counts.
