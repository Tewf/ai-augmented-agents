# Convergence: rounds, raters, batches and passes when several agents work one project

The first pass of the review on how several agents settle on an answer. It states five results as claims with their sources and names four quantities to measure.

- It holds 11 sources, all formal; no grey source.
- Grade: 6 derived (theorems), 2 derived with experiments in their papers, 2 measured, 1 convention. Five were located and not read.
- Only one claim has a measured result: the central check (Kim 2025), already a principle of this repository.
- Where the first statement of a claim disagreed with its sources, the sources won (strand C).

## Files

| File | Role |
|---|---|
| [frame](frame.md) | step 1: the problem in one sentence, the names the field gives it |
| [protocol](protocol.md) | how the pool was built and searched |
| [sources](sources.md) | the flow and one row per work |
| [review](review.md) | step 2: the five claims and the four quantities |
| [state of the art](state-of-the-art.md) | step 3: [best evidence](../multi-agent-teams/state-of-the-art.md) apart from practice most adopted |
| [against](against.md) | the evidence that cuts the other way |
| [position](position.md) | step 4: what is known, what is not, what can be added |
| [baseline](baseline.md) | step 5: the named baseline and how it is compared |
| [bibliography](../bibliography.md) | every work cited, one row each |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Raters with a common prior who announce posteriors in turn reach agreement | derived | review.md A |
| n correlated raters are worth n / (1 + (n - 1) rho) independent ones, at most 1 / rho | derived | review.md B |
| Batch regret exceeds sequential by a constant factor independent of the batch size, under assumptions | derived, secondary | review.md C |
| A lead correcting a fraction lambda per pass leaves errors falling as (1 - lambda) to the power k; an exact check resets them | derived | review.md D |
| A central check cut error amplification from 17.2 to 4.4 times | measured | review.md E |
| No work was found that measures rho, lambda, or error per link for models | not found in this pass | position.md |

## The four quantities

rho between raters of one family; batch regret against sequential; lambda per audit pass; error per link. Definitions and counting are in [review](review.md).

## Named baseline

**B1**, one lead with a central check ([baseline](baseline.md)).

## Status

A first pass. 11 sources, one reviewer, no grey search, no forward search. Five are located and not read. The frame found that the field has no single name for the question; the repository keeps its name.
