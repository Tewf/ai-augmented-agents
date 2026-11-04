# Frame: what the field calls several agents settling on one answer

Step 1 of the review, read on 2026-11-04. It states the problem, gives the field's names beside the practitioners', and says whether the repository's word matches. The searches are in [protocol](protocol.md).

**Shape:** [frame](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/frame.md)

## The problem in one sentence

Several **agents** (people or programs) check the same work. How many passes and raters make the answer settle, and what makes it settle wrong?

## Terms, defined before use

- A **rater** is an agent that scores or checks one item.
- **rho** is the correlation between the errors of two raters on the same items.
- **n_eff** is the number of independent raters that n correlated raters are worth.
- **lambda** is the fraction of the remaining errors that one audit pass corrects.
- An **audit pass** is one re-reading of the work by the lead, who corrects what it finds.
- An **exact check** is a program that decides an item with no error, such as a test.
- **Regret** is the shortfall of a search against the best it could have found.

## What the field calls it

| Level | The field's name | First met in |
|---|---|---|
| Rounds of exchange | **agreement theorem**, common knowledge | Aumann 1976 |
| Rounds, dynamics | **communication to consensus**: announcing posteriors in turn reaches agreement | Geanakoplos 1982 |
| Many raters | **jury theorem**, aggregation of **correlated votes** | Ladha 1992; Berg 1993; Kaniovski 2010 |
| Many workers at once | **batch** or **parallel Bayesian optimisation** | Desautels 2014; Kandasamy 2018 |
| Repeated passes of a lead | **fixed point** of a **contraction** (a mapping that shrinks distances) | derived here |
| Who decides what | **team theory** | Marschak 1972 |
| Errors across links | **error amplification**, central check | Kim 2025 |

## What practice calls it

- **Consensus**, **majority vote** and **ensemble**: many raters, one answer. The field's word is aggregation.
- **Review loop** and **audit pass**: a lead corrects, then looks again. The field's word is iteration to a fixed point.

## Does the repository's name match?

- The repository says **agents**; this strand's word is **rater** for the many and **lead** for the one that corrects.
- The field has no single name for the whole question. The name stays; the maintainer decides.

## Sub-questions

| Question | Strand in [review](review.md) |
|---|---|
| Q1 Do rounds of exchange make raters agree, and on what? | A |
| Q2 How many independent raters are n correlated ones? | B |
| Q3 What does a batch cost against going one by one? | C |
| Q4 How fast do passes remove errors? | D |
| Q5 Who decides what, so the information is cheap? | E |

## Held elsewhere

- Delegation, briefs and incentives: [multi-agent-teams](../multi-agent-teams/README.md).
