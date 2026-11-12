# 0007: Convergence stays a finding until its four quantities are counted

**Decision:** The five convergence results are kept as findings in the evidence, and none becomes a principle, because only the central check is measured and that one already is a principle.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/shapes/decision-record.md).

## Context

- The review [convergence](../evidence/convergence/README.md) states five results: agreement by rounds, correlated raters, batch regret, [contraction](../evidence/convergence/frame.md) of audit passes, and the central check.
- The rule of [decision 0004](0004-which-findings-became-principles.md) sets when a finding becomes a principle.
- Four of the five are theorems or arithmetic. Only the central check has a count (Kim 2025).
- One claim was first stated as "batch regret grows with the batch". Its two sources say the regret exceeds the sequential one by a factor independent of the batch size, under assumptions. The sources win, and the review says so.

## Decision

- Measured: error amplification 17.2 times without a central check and 4.4 times with it (Kim 2025). It is the ground of [run the checks at the lead](../principles/result/run-the-checks-at-the-lead.md), so no new principle is added.
- Theory, not measured: agreement by rounds, the effective number n / (1 + (n - 1) rho), the batch bound, and the geometric fall of errors at the rate 1 - lambda.
- Four quantities are named to measure: rho between raters of one model family, batch regret against sequential, lambda per audit pass, and error per link.
- No line is added to the standard card. The evidence README links the review.

## Consequences

- **Good:** no claim is stronger than its evidence, and the quantities to count are written before the counting.
- **Bad:** the rule that a second rater come from another model family rests on a derivation, graded convention, with no measured rho.
- When a log holds enough items with an [exact check](../evidence/convergence/frame.md), count the four quantities. A measured rho or lambda is the grade that lets a principle be written.

## See also

[Decisions](README.md); [the review](../evidence/convergence/README.md).
