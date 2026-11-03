# Frame: what the field calls several agents on one project

Step 1 of the review. It says the problem in one sentence, then the names the field and practice give it.
Terms are defined here once; the searches are in [protocol](protocol.md).

**Shape:** [frame](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/frame.md)

## The problem

When several **agents** (people or programs acting for a goal) work one project, who hands what to whom, and what keeps them pulling the same way?
The hand-over carries a **brief**: the message that hands a task to an agent that knows nothing else.

## Terms, defined before use

- A **principal** hands an agent a task.
- **Moral hazard in teams**: each member's effort is not seen, only the team's result, so each can free-ride.
- **Team theory**: several decision makers share one goal and differ only in what each knows; the question is the cost of information.
- **Mechanism design**: choosing the rules of a game so that self-interested players produce the outcome wanted.
- **Dec-POMDP**: a model of several agents acting together on partial observations; its general case is NEXP-complete.

## What the field calls it

The repository's word, **agents**, is the field's word for the parts, and not its word for the problem. The problem has four names, one per tradition.

| Tradition | Its name for the problem | Acronym or author | Strand |
|---|---|---|---|
| Economics of delegation | the **principal-agent problem**, or agency theory | Jensen and Meckling 1976 | Q1, Q3 |
| Economics of teams | **team theory**; **moral hazard in teams** | Marschak and Radner 1972; Holmström 1982 | Q1, Q3 |
| Economics of design | **mechanism design**; incomplete contracts | Hurwicz, Myerson; Hart and Moore | Q3 |
| Computer science, planning | **decentralised partially observable decision making**, the cost of communication | Dec-POMDP; COM-MTDP | Q2, Q4 |
| Computer science, learning | **multi-agent reinforcement learning**; **cooperative AI** | MARL | Q4 |
| Computer science, language models | **LLM-based multi-agent systems**; multi-agent collaboration | LLM-MAS | Q2 |
| Practice | **orchestrator and workers**, subagents, handoffs, supervisor pattern | | Q1, Q2 |

## Questions, mapped to the front page

| Id | Question | Traditions that answer it |
|---|---|---|
| Q1 | Delegate or do: when does a cheaper agent, with briefing and checking, cost less? | economics of teams; routing and cascades; practice |
| Q2 | The brief: what must it hold, and how is it checked? | LLM-MAS surveys and failure studies; practice |
| Q3 | Incentives: what does a model agent optimise? | principal-agent; moral hazard; cooperative AI; mechanism design |
| Q4 | Measured coordination: what can be counted from the history? | team theory; software engineering of teams; MARL for what to count |

## What the field does not call it

- No source found names the whole problem as one field. It is split between economics (people) and computer science (programs).
- The mixed team of people and language models is called **human-AI teaming** or **hybrid teams**, a fifth name, searched in the review.
- The repository's name stays; this file records that the field's word for the arrangement is **team**, not agent.
