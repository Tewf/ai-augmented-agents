# Sources: the pool, its flow and its quality

The pool of the review, read on 2026-11-02 and extended on 2026-11-03: 39 sources, 36 formal or classic and 3 grey. Searches are in [protocol](protocol.md); keys are in the [bibliography](../bibliography.md).

**Shape:** [sources](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/sources.md)

## Flow

| Stage | Count |
|---|---|
| Formal strings run | 11 counted, 1 timed out; 2 arXiv strings, 1 failed |
| Grey strings run | 1 web string (7 results, none opened) |
| Records screened by title and abstract | about 40 in the first pass; 406 citing titles in the forward search |
| Opened and read in full | 7 (Cemri 2025, Kim 2025, Chen 2023b, Conway 1968, Anthropic 2024, Anthropic 2025, Cognition 2025) |
| Read in part | 1 (Ong 2024) |
| Abstract read only | 22 (18 in the first pass; the 4 forward works) |
| Method source, not part of the evidence | 1 (Garousi 2019) |
| Located only, not read | 8 (the two economics classics and the book on teams among them) |
| Set aside as one-application systems | 4 |
| Included | 39 (35 in the first pass; 4 from the forward search) |
| Grey below 10 of 20 | 0 |

## Grey sources, scored on Garousi 2019

Subtotals: authority, methodology, objectivity, date, position, novelty, impact, outlet. Tier 3 (blog) scores 0 for outlet.
The "review" column is the score of the first pass; the score in use is the one after rereading (section below).

| Key | Tier | Score in use | Review | Subtotals in use | Use |
|---|---|---|---|---|---|
| Anthropic 2025 | 3 | 14.5 of 20 | 13.5 | 3.5 / 5 / 1.5 / 1 / 0.5 / 2 / 1 / 0 | support, as its owner's claim |
| Anthropic 2024 | 3 | 11.5 of 20 | 11.5 | 3.5 / 3.5 / 1.5 / 1 / 0.5 / 1 / 0.5 / 0 | support, as its owner's claim |
| Cognition 2025 | 3 | 12 of 20 | 10.5 | 3 / 4 / 1 / 1 / 1 / 2 / 0 / 0 | support, as its owner's claim; no data |

### Changed on rereading

Each source was reread in full and scored item by item on the twenty criteria. Every change below has its reason; a score that did not change is not listed.

- **All three, authority, A3 (author's other work):** 1 to 0.5 for the two Anthropic posts, and 0 for Cognition. The text shows no other work by the named authors. The company's later pages are not theirs.
- **All three, date, D1:** kept at 1. The page carries a published date in its metadata. The text also dates itself: a note on the 2024 post and a line on the 2025 one.
- **All three, outlet:** kept at 0. These are company blog posts, which the criteria list as blogs. The criteria also list company pages at 0.5, so the line between the two is open (see [protocol](protocol.md), section 8).
- **Anthropic 2024:** methodology 2 to 3.5. The post names its basis, work with customers. It asks a specific question, when to use agents, and works two domains in its appendix.
- **Anthropic 2024:** objectivity 2 to 1.5. A company page promoting its own patterns scores 0 on O3. Its conclusions are observed, not tested, so O4 is 0.5.
- **Anthropic 2024:** impact 1 to 0.5. The only sign of uptake is the owner's own "dozens of teams".
- **Anthropic 2025:** methodology 3 to 5. The post states its analysis (M2 0.5). It cites one published benchmark (M3 0.5). It states a downside, about 15 times the tokens of a chat, and a section on production challenges (M4 1). It describes one system in depth (M6 1).
- **Anthropic 2025:** objectivity 2 to 1.5. The 90.2% figure comes with no sample or variance, so O4 is 0.5. Impact stays at 1: users' reports and a product in production.
- **Cognition 2025:** methodology 1 to 4. The post states its aim (M1 1). Its principles come from building agents (M2 0.5). It says its theories may be wrong (M4 1). It asks a specific question (M5 1). It reasons from two examples (M6 0.5).
- **Cognition 2025:** objectivity 2 to 1. The post ends with a link to its own product, so O3 is 0. It argues from examples, with no data, so O4 is 0.
- **Cognition 2025:** position 0.5 to 1. It names and links Swarm and AutoGen.
- **Cognition 2025:** impact 1 to 0. Nothing in the text shows uptake by others.

### Second rater

A second rater, a language model given the criteria and the text of each source, scored each source once, in two passes: the first pass saw the first 12,000 characters, the second the whole text. Agreement with the first pass of the review, and with the score in use, is in [protocol](protocol.md), section 12.

## The pool

Grade for formal sources: **measured** (M), **supported with caveat** (S), **convention** (C). "Read" says how far.

| Key | Kind | Found via | Grade, read | Used in |
|---|---|---|---|---|
| Marschak 1972 | formal, classic book | seminal, frame | C; located only | review A |
| Holmström 1982 | formal, theory | seminal | C; located only | review A |
| Jensen 1976 | formal, theory | seminal | C; located only | review A |
| Holmström 1991 | formal, theory | snowball from Holmström 1982 | C; located only | review A |
| Nisan 2001 | formal, theory | string "mechanism design" | C; located only | review A |
| Hadfield-Menell 2019 | formal, argument | string "principal-agent" | C; abstract | review A, C |
| Fudenberg 1986 | formal, theory | repeated games | C; located only | review B |
| Bernstein 2002 | formal, theorem | string "decentralized POMDP" | S; abstract | review B |
| Pynadath 2002 | formal, theory | same | C; located only | review B |
| Zhang 2021 | formal, survey | string "MARL survey" | C; abstract | review B |
| Foerster 2018 | formal, experiments | snowball from Zhang 2021 | M, on toy games; abstract | review B |
| Leibo 2017 | formal, experiments | same | M, on toy games; abstract | review B |
| Dafoe 2020 | formal, survey | string "cooperative AI" | C; abstract | review B |
| Guo 2024 | formal, survey | arXiv string | C; abstract | review 0, C |
| Han 2024 | formal, survey | arXiv string | C; abstract | review 0, C |
| Tran 2025 | formal, survey | arXiv string | C; abstract | review 0, C |
| Du 2023 | formal, experiments | snowball from Guo 2024 | M; abstract | review C |
| Hong 2023 | formal, system | same | M, on its own benchmarks; abstract | review C |
| Wu 2023 | formal, system | same | C; abstract | review C |
| Smit 2023 | formal, benchmark | string "debate" | M; abstract | review C, against |
| Cemri 2025 | formal, dataset | string "failure taxonomy" | M, descriptive; read in full | review C |
| Kim 2025 | formal, experiments | arXiv string | M; read in full | review C |
| Lee 2026b | formal, experiments | forward from Vaccaro 2024 | M, on a pre-registered experiment; abstract (secondary) | review D, E |
| Hammond 2025 | formal, report | arXiv string | C; abstract | review B, C |
| Tomasev 2025 | formal, argument | string "mechanism design" | C; abstract | review A |
| Tomasev 2026 | formal, framework | string "intelligent AI delegation" | C; abstract | review D |
| Kapoor 2024 | formal, critique | snowball from Kim 2025 | S; abstract | review D, against |
| Chen 2023b | formal, experiments | snowball from Ong 2024 | M; read in full | review D |
| Ong 2024 | formal, experiments | string "routing" | M; read in part | review D |
| Vaccaro 2024 | formal, meta-analysis | string "human-AI teaming" | M; abstract | review D |
| Ngo 2025 | formal, meta-analysis | forward from Vaccaro 2024 | M; abstract (secondary) | review D |
| Brodeur 2026 | formal, experiment | forward from Vaccaro 2024 | M, randomised; abstract (secondary) | review D |
| Dell'Acqua 2026 | formal, field experiment | forward from Vaccaro 2024 | M, pre-registered; abstract (secondary) | review C, D |
| Garousi 2019 | formal, method | method | S; not graded | protocol |
| Conway 1968 | classic, magazine paper | practice | C; read | review E |
| Brooks 1975 | classic, book | practice | C; located only | review E |
| Anthropic 2025 | grey | practice | see table above | review C, E |
| Anthropic 2024 | grey | practice | see table above | review E |
| Cognition 2025 | grey | practice | see table above | review E |
