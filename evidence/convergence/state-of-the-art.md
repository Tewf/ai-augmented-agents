# State of the art: the best evidence and the practice most adopted

The same step for the neighbouring strand is in [multi-agent teams](../multi-agent-teams/state-of-the-art.md).

Step 3 of the review: one table per question, with the best record and the common practice in separate rows. Keys are in the [bibliography](../bibliography.md).

**Shape:** [state of the art](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/state-of-the-art.md)

## Q1: rounds of exchange

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence, proved | Aumann 1976; Geanakoplos 1982 | raters with a common prior cannot agree to disagree; rounds of announcements reach agreement | derived |
| Practice most adopted | none found | no source runs rounds between model raters | |
| Lower bound | none found | no bound on rounds for models | |

## Q2: correlated raters

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence, proved | Ladha 1992; Berg 1993; Kaniovski 2010 | the jury theorem with dependent votes | derived |
| Derived here | the formula of strand B | n correlated raters are worth n_eff, at most 1 / rho | derived |
| Practice most adopted | several raters, one family | no measure of rho found | |

## Q3: batches

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence, achieved | Desautels 2014 | regret within a constant factor of sequential, independent of B | derived, with two applications (secondary) |
| Best evidence, achieved | Kandasamy 2018 | n evaluations over M workers are essentially n in sequence | derived, with simulations (secondary) |
| Lower bound | none found | no floor on the factor | |

## Q4 and Q5: passes and links

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence | Kim 2025 | error amplification 4.4 times with a central check, 17.2 without | measured |
| Derived here | the contraction of strand D | geometric fall at rate 1 - lambda; reset by an exact check | derived |
| No outside signal | Huang 2024 | self-correction is unreliable without one (secondary) | measured |
| Practice most adopted | review loops of a lead | lambda not recorded anywhere found | |

## Where the two records part

- Practice adds raters and passes. The proofs say how fast they pay: at most 1 / rho raters, and 1 - lambda per pass. Neither rho nor lambda is known for models.
