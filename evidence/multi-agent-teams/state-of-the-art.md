# State of the art: the best evidence and the practice most adopted

Step 3 of the review. For each question, the **best evidence** (a research record) stands apart from the **practice most adopted** (a practice record), and what has been achieved stands apart from what is proved impossible. Keys are in the [bibliography](../bibliography.md).

**Shape:** [state of the art](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/state-of-the-art.md)

## Q1: delegate or do

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence, achieved | Chen 2023b | a cascade of models matched the best one at up to 98.3% lower cost on one dataset | measured |
| Best evidence, achieved | Ong 2024 | routing between a strong and a weak model cut cost over 2 times in certain cases | measured |
| Best evidence, people | Vaccaro 2024; Ngo 2025 | people with AI did worse than the better of the two, g = -0.23; augmentation helped (g = 0.62) and synergy did not (g = -0.38), secondary | measured |
| Practice most adopted | orchestrator and workers (Anthropic 2024; Anthropic 2025) | a lead model splits the task and hands parts to others | convention |
| Lower bound | none found | no source proves a floor on briefing and checking cost | |

## Q2: the brief

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence | Cemri 2025 | failures cluster in design, misalignment between agents, and verification | measured, descriptive |
| Practice most adopted | Anthropic 2025 | objective, output format, tools and boundaries in each brief | convention, owner's claim |
| Practice, against | Cognition 2025 | pass full context, not a summary | convention |
| Lower bound | none | no study varies a brief and measures the result | |

## Q3: incentives

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Impossibility, people | Holmström 1982 | no sharing rule gives balanced budget and efficient effort in a team; source located only | convention |
| Impossibility, planning | Bernstein 2002 | decentralised control is complete for nondeterministic exponential time (secondary) | supported with caveat |
| Achieved, learning | Leibo 2017; Foerster 2018 | cooperation among learners on toy games (secondary) | measured |
| Best frame for models | Hammond 2025; Hadfield-Menell 2019 | failures sorted by incentive; misalignment as an incomplete contract (secondary) | convention |

## Q4: measured coordination

| Record | Holder | What it shows | Grade |
|---|---|---|---|
| Best evidence | Kim 2025 | error amplification 4.4 times with a central check, 17.2 times without | measured |
| Practice most adopted | Conway 1968; Brooks 1975 | structure follows communication; cost grows with pairs of people | convention |
| Counts of duplicate decisions across repositories | none | not measured anywhere found | |

## Where the two records part

- Practice adopts many agents; the best evidence says the gain depends on the task and can be -70.0%.
- Practice reports 90.2% from one system; the controlled comparison found a range of +80.8% to -70.0% over six benchmarks.
