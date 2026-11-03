# Review: what each tradition has measured

Step 2 of the review. It groups the 39 sources by strand and answers Q1 to Q4 of [frame](frame.md).

Grades: measured, supported with caveat, convention, not supported. A number read only in an abstract is marked (secondary). Keys are in the [bibliography](../bibliography.md).

## 0. Existing reviews

- Guo 2024, Han 2024 and Tran 2025 survey systems of language-model agents. They give vocabulary: roles, communication, structure, task allocation. None measures a gain over one agent.
- Zhang 2021 surveys multi-agent reinforcement learning, mostly theory (secondary).
- Vaccaro 2024 is the one meta-analysis of humans and models together.
- Hammond 2025 is a taxonomy of risks, not a measurement.

## A. The economics of teams and delegation (Q1, Q3)

- **Principal-agent problem**: a principal hires an agent whose effort the principal cannot see (Jensen 1976). Grade: convention, theory; source located only.
- **Moral hazard in teams**: when only the team's output is seen, no sharing rule gives both a balanced budget and efficient effort (Holmström 1982). Grade: convention, theory; source located only, so the statement is the textbook one.
- **Team theory**: with a shared goal, the cost is information, not conflict (Marschak 1972). Grade: convention; the book is scanned and was not read.
- **Multitask**: pay on one measured task pulls effort from unmeasured ones (Holmström 1991). Grade: convention; located only.
- **Mechanism design**: Nisan 2001 brings it to computation; Tomasev 2025 proposes auctions and mission economies for agent markets. Grade: convention, argued.
- **Incomplete contracts**: Hadfield-Menell 2019 reads the alignment problem as one (secondary).
- Whether a model agent has an incentive, in the economists' sense, is not answered by any source here (Q3).

## B. Cooperation, planning and learning (Q3, Q4)

- **Dec-POMDP**: for even a small number of agents, the finite-horizon problem is complete for nondeterministic exponential time (Bernstein 2002, secondary). Grade: supported with caveat; a proof about a model, not about teams in practice.
- **Communication cost** enters the model as a decision (Pynadath 2002); located only.
- **Repeated games**: cooperation can be sustained when players are patient (Fudenberg 1986); located only.
- **Learning agents**: independent learners in sequential social dilemmas show cooperation depends on the policies learned (Leibo 2017, secondary). Opponent-learning awareness changes what agents learn (Foerster 2018, secondary). Grade: measured on toy games.
- Dafoe 2020 names cooperation as the open problem for AI (secondary).
- Hammond 2025 sorts multi-agent failure by incentives into miscoordination, conflict and collusion (secondary).

## C. Systems of language-model agents (Q1, Q2)

- **Task decides the gain**: across 260 configurations, six benchmarks, five architectures and three model families, the change against one agent ranges from +80.8% to -70.0% (Kim 2025, Table and abstract, read). Grade: measured.
- The same holds for people: AI raised output on knowledge tasks inside its frontier and lowered the rate of correct answers on a task outside it (Dell'Acqua 2026, secondary). Grade: measured, pre-registered field experiment.
- **Centralised checking contains errors**: errors grow 17.2 times without it and 4.4 times with it (Kim 2025, read). Grade: measured.
- **The predictive model is weak**: cross-validated R squared 0.373 across the six benchmarks, 0.413 with a task-grounded metric (Kim 2025, read). It explains a little over a third.
- **Failures are mostly about the team**: 14 failure modes in three groups, from 1,600+ traces over 7 frameworks (Cemri 2025, read).
- The groups are system design, inter-agent misalignment and task verification.
- Annotators agreed at kappa 0.88 on the taxonomy sample. Grade: measured, descriptive.
- **Debate does not reliably beat cheaper prompting** such as self-consistency, though tuned debate can (Smit 2023, secondary). Du 2023 found gains from debate on reasoning (secondary). The two disagree; see [against](against.md).
- **Two systems**: MetaGPT encodes standard operating procedures (Hong 2023); AutoGen lets agents converse (Wu 2023). Both report gains on their own tasks (secondary).
- **Benchmarks mislead**: accuracy-only benchmarks reward costly agents (Kapoor 2024, secondary). Grade: supported with caveat.

## D. Delegate or do (Q1)

- **Cascades and routers**: a cascade matched the best single model at 98.3% lower cost on one dataset, 73.3% on another, 59.2% on a third (Chen 2023b, table, read). Grade: measured, on three datasets.
- **Routers** cut cost by over 2 times in certain cases, without sacrificing response quality, on three public benchmarks (Ong 2024, read in part). Grade: measured.
- **Humans with AI**: a meta-analysis of 106 studies and 370 effect sizes (Vaccaro 2024, secondary).
- The combination did worse than the better of the two, Hedges g = -0.23 (95% CI -0.39 to -0.07; secondary).
- Ngo 2025 splits that average. Across 146 experiments in healthcare and public sectors, AI augmentation improved performance (g = 0.622), while synergy, the team, was generally negative (g = -0.380), with AI alone often better (secondary). Publication bias favours augmentation. Grade: measured, with that caveat.
- Brodeur 2026 gives the same split in a randomised experiment: 288 researchers in 103 teams. Reproduction ran at 94% for human-only teams and 91% for AI-assisted teams. It fell to 37% where the model led with minimal oversight (secondary). Grade: measured.
- Decision tasks lost and content creation gained. Grade: measured.
- **A framework**: delegation includes transfer of authority, responsibility, roles and trust (Tomasev 2026, secondary). Grade: convention, proposed.
- Lee 2026b measures a cost of delegation that the saving does not show. In a pre-registered experiment (N = 269), copying the model's text lowered self-efficacy, ownership and meaning, and drafting first and then refining mitigated those effects (secondary). Grade: measured, on one writing task.
- No source puts a price on briefing and checking beside the saving.

## E. Practice (Q1, Q2)

- **Brief fields**: each subagent needs an objective, an output format, guidance on tools and sources, and clear task boundaries; without them agents duplicate work and leave gaps (Anthropic 2025, read). Its owner's claim; no ablation is reported.
- **Token use**: its multi-agent system outperformed one agent by 90.2% on an internal research eval and used about 15 times the tokens of a chat (Anthropic 2025, read). Owner's claim.
- **Simplest first**: find the simplest solution, and add agents only when needed (Anthropic 2024, read). Convention.
- **Against many agents**: share context, since actions carry implicit decisions (Cognition 2025, read). Convention; no data.
- **Structure follows communication**: a system copies its organisation's communication structure (Conway 1968, read).
- **Cost of adding people**: Brooks 1975 argues communication grows with the pairs of people, n(n-1)/2; located only, so (secondary).

## F. Measured coordination (Q4)

- No source counts decisions taken twice or facts written twice across repositories built by several agents.
- Cemri 2025 counts failure modes in traces, the nearest measurement; Kim 2025 counts error amplification.
- The maintainer's own counts are the first data; they are in [baseline](baseline.md).
