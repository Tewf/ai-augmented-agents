# Review: five results, and four quantities to measure

Step 2 of the review. It states the five results as claims with their sources, says which part of each is proved and which is measured, and names the four quantities to measure. Keys are in the [bibliography](../bibliography.md); a number read only in an abstract is marked (secondary).

**Shape:** [review](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/review.md)

## 0. Existing reviews

- None for this strand. The nearest are the surveys of language-model agent systems in [multi-agent-teams](../multi-agent-teams/README.md); none states these results.

## A. Rounds of exchange reach agreement (Q1)

- **Agreement theorem**: if two people have the same prior and their posteriors for an event are common knowledge, the posteriors are equal (Aumann 1976, abstract, which states the theorem). Grade: derived.
- **Rounds**: when two agents announce their posteriors in turn, they reach agreement after finitely many announcements, in a finite model (Geanakoplos 1982, secondary: the source was located, not read). Grade: derived.
- **What it needs**: a common prior, common knowledge of the posteriors, and exact updating. Raters of one model family share training, which may stand in for a common prior. No source tests that. Open.

## B. Correlated raters are worth fewer raters (Q2)

- **Jury theorem with correlated votes**: Condorcet's theorem, that a majority beats one member, is generalised to votes that are correlated (Ladha 1992, abstract). Dependence among jurors changes the result (Berg 1993, Kaniovski 2010; both located only). Grade: derived.
- **Effective number**, derived here for the mean of n scores with equal error variance and pairwise error correlation rho:

  n_eff = n / (1 + (n - 1) rho)

  The variance of the mean is sigma squared times (1 + (n - 1) rho) / n. So n correlated raters are worth n_eff independent ones. They are never worth more than 1 / rho. Grade: derived; arithmetic, no data.

| n | rho | n_eff |
|---|---|---|
| 5 | 0 | 5.00 |
| 5 | 0.2 | 2.78 |
| 5 | 0.5 | 1.67 |
| 5 | 1 | 1.00 |

- **Scope**: the formula is for an average of scores. For a majority of yes or no votes the same direction holds, but the exact result is in the jury papers, not this formula.
- **The rule that follows**: a second rater should come from a different model family than the first, since rho is then lower. This is a design rule from the derivation, graded convention. No measure of rho between model families was found.

## C. Batches cost regret against going one by one (Q3)

- **A batch is a delayed sequence**: in a round, B choices are made before any of the B results is seen.
- **Bound**: the cumulative regret of the batch algorithm exceeds the sequential one by a constant factor independent of the batch size B (Desautels 2014, abstract, secondary). The result needs a Gaussian-process payoff and an initial set of observations.
- **Parallel Thompson sampling**: n evaluations over M workers are essentially equivalent to n in sequence, and asynchronous workers do better under a time limit (Kandasamy 2018, abstract, secondary).
- **A correction of the claim as first stated**: regret does not grow with the batch size in these two results; it grows by a bounded factor, and the cost is hidden in the assumptions. The first statement was "grows with the batch". The papers say a bounded constant. The sources win. Whether this holds for agents that hand work in batches is not measured.

## D. A lead that corrects a fraction per pass is a contraction (Q4)

- **Error model**: let e(k) be the errors left after pass k. A pass corrects a fraction lambda of them, so e(k+1) = (1 - lambda) e(k) and e(k) = (1 - lambda)^k e(0). For any lambda above 0 the errors fall geometrically.
- **With fresh errors**: if each pass adds eps new errors before it corrects, the errors settle at eps (1 - lambda) / lambda. A small lambda leaves a large floor.
- **An exact check resets**: a program that decides an item with no error sets the errors on what it covers to zero, and does not depend on lambda. Grade: derived; the model is arithmetic, and lambda is not measured.
- **Without an outside signal**: a model correcting its own reasoning did not reliably improve it (Huang 2024, abstract, secondary). That is the case of a lambda near 0 with no exact check.

## E. Who decides what, and the central check (Q5)

- **Team theory**: with a shared goal, the cost is information, so the question is who knows what when each decides (Marschak 1972; located only). Grade: convention.
- **Central check**: errors grew 17.2 times without a central check and 4.4 times with it (Kim 2025, read in full in the earlier review). Grade: measured. This is the one measured result of the five, and it is already a principle: [run the checks at the lead](../../principles/result/run-the-checks-at-the-lead.md).
- **Error per link**: the factor 17.2 against 4.4 is a count over the links of a chain. The per-link rate it implies is not reported.

## Theory and measure

| Claim | What is proved | What is measured |
|---|---|---|
| A. Rounds reach agreement | theorem, with a common prior | nothing for models |
| B. Correlated raters, n_eff | theorem and arithmetic | nothing: rho between model raters not found |
| C. Batch regret | bounded factor, under assumptions | two applications, in the papers (secondary) |
| D. Contraction of passes | arithmetic | nothing: lambda not found |
| E. Central check | none | error amplification 17.2 to 4.4 (Kim 2025) |

## The four quantities to measure

| Quantity | Definition | How it is counted | Needs |
|---|---|---|---|
| rho | correlation of the error indicators of two raters on the same items | items with a known answer from an exact check; raters of one family, then of two | strand B |
| Batch regret against sequential | cost of the same task set run with batch size B against B = 1 | same tasks, same checks, B = 1, 2, 4 | strand C |
| lambda per audit pass | errors removed by a pass divided by errors present before it | errors counted by an exact check before and after each pass | strand D |
| Error per link | share of hand-overs that introduce an error the next link catches | the lead's check log, one row per link | strand E |

Each is a count a program can make from a log. None is measured yet.
