# Against: evidence that cuts the other way

Evidence against a claim of [review](review.md), kept beside it. Keys are in the [bibliography](../bibliography.md).

**Shape:** [against](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/against.md)

## Agreement may not apply to models

- The theorem needs a common prior and exact updating. A model rater is neither in a proved sense.
- Agreement is not accuracy: two raters can agree on a wrong answer, which is the case of rho near 1.

## The effective number is a mean, not a vote

- n_eff holds for an average of scores with equal variance and equal correlation. Real raters differ in both.
- For votes, correlation can also help: Ladha 1992 and Berg 1993 study when dependence lowers or keeps the majority's edge. The abstracts read here do not give the conditions.

## The batch bound has assumptions

- Desautels 2014 needs a Gaussian-process payoff. A hand-over of work to agents is not one.
- The result is a bounded factor, so it does not say that batches are free, only that the factor does not grow with B.

## The contraction model is a toy

- A constant lambda is assumed. An audit pass that finds the easy errors first would have a lambda that falls.
- Errors may not be independent of the pass: a pass can add errors, which the floor term eps covers only if eps is constant.

## Limits of this pass

- Five of 11 sources were located and not read. Five more were read in the abstract only.
- No source measures rho between model raters, lambda, or error per link. The review is theory plus one measured count.
