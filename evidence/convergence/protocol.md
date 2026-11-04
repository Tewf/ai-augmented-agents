# Protocol: how the pool was built

A first pass, run on 2026-11-04 by one reviewer. Terms are in [frame](frame.md); the pool is in [sources](sources.md). The method is the multivocal review of Garousi 2019, cut to a first pass.

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

## 1. Why grey literature

Garousi 2019, Table 4, seven questions. The answer to the question on volume decides the rest.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | no: each claim is a theorem or a proof |
| 2 | Lack of volume or quality of evidence? | yes for models as raters, no for the theory |
| 3 | Context important? | yes: a model rater is not a juror |
| 4 | Corroborate research with practice? | no practice source found that measures it |
| 5 | Challenge practice with research, or the reverse? | not in this pass |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | not searched |

No grey search was run. This is stated, not hidden.

## 2. Questions

Q1 to Q5 of [frame](frame.md).

## 3. Existing reviews

- Found: a survey of language-model agent systems and a taxonomy of their failures, both already in [multi-agent-teams](../multi-agent-teams/README.md).
- Not found: a review that treats raters, rounds, batches and passes together for models.

## 4. Formal search

Counts are from OpenAlex, field title and abstract, sorted by citations, on 2026-11-04, with no key and no account. The five top results of each string were screened.

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | agreement theorem common knowledge | 93 | nnynn |
| F2 | jury theorem correlated votes | 24 | yynny |
| F3 | batch Bayesian optimization regret | 39 | ynynn |
| F4 | language models correlated errors judges | 99 | nnnnn |
| F5 | multi-agent debate majority voting language models | 38 | nnnnn |
| F6 | iterative refinement self-correction language models contraction | 1 | n |

Title lookups, each a search of one known work, on the same date.

| Id | Work looked for | Result |
|---|---|---|
| L1 | Aumann, Agreeing to disagree | found, 1976 |
| L2 | Geanakoplos and Polemarchakis, We can't disagree forever | found, 1982 |
| L3 | Ladha, jury theorem and correlated votes | found, 1992 |
| L4 | Berg, dependency among jurors | found, 1993 |
| L5 | Kaniovski, aggregation of correlated votes | found, online 2008 |
| L6 | Desautels, parallelizing exploration-exploitation | found, preprint 2012 |
| L7 | Kandasamy, parallel Thompson sampling | found on arXiv, 2017 |
| L8 | Marschak and Radner, teams | found as reviews of the book; the scan is linked in the bibliography |

- F4 and F5 returned no relevant work: the query is wrong or the literature is not indexed under these words. This is not a finding that nothing exists.
- arXiv was queried by identifier for three preprints, to read their abstracts.

## 5. Grey search

None. See section 1.

## 6. Stopping rule

Effort bounded: the five claims were fixed before the search, and each string was stopped after 5 results. A claim is searched until its named source is verified.

## 7. Selection

- Include: a theorem or study named for one of the five claims, or a measure of correlation between model raters.
- Exclude: works on one application, such as pain research, filters or law.

## 8. Quality of grey sources

Not applicable: no grey source is in the pool. Garousi 2019, Table 7, would apply with a threshold of 10 of 20.

## 9. Extraction and synthesis

Per source: the claim, and how far it was read. A statement read only in an abstract or known as the textbook statement is marked secondary. Synthesis is by strand A to E.

## 10. Not searched, and limits

- Not searched: Google Scholar, Scopus, Web of Science, SSRN, forums, and the grey literature on model judges.
- Not read in full: all formal sources except the abstracts; their bounds are secondary.
- One reviewer, no second rater, no forward search. A second rater from a different model family than the first would be needed before any score is trusted (reason in [review](review.md), strand B).
- No work was found that measures rho between model raters. This is a gap of this pass.
- No identity was sent to any service.
