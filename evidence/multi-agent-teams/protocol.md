# Protocol: how the pool was built

A first pass, run on 2026-11-02 by one reviewer, and extended on 2026-11-03 with a forward search and a second rater for the grey sources (sections 11 and 12). Terms are in [frame](frame.md); the pool is in [sources](sources.md).
The method is the multivocal review of Garousi 2019.

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

## 1. Why grey literature

Garousi 2019, Table 4, seven questions.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: language-model agent systems are built and described by companies first |
| 2 | Lack of volume or quality of evidence? | yes: the formal evidence on briefs and delegation to models is thin |
| 3 | Context important? | yes: a team of people differs from a team of models |
| 4 | Corroborate research with practice? | yes: benchmark gains against production reports |
| 5 | Challenge practice with research, or the reverse? | yes: advice to build many agents against advice not to |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: course notes and skill files on delegation abound |

## 2. Questions

Q1 to Q4 of [frame](frame.md): delegate or do, the brief, incentives, measured coordination.

## 3. Existing reviews (Garousi Guideline 2)

- Surveys of language-model agent systems: Guo 2024, Han 2024, Tran 2025.
- A survey of multi-agent reinforcement learning: Zhang 2021.
- A meta-analysis of people and AI together: Vaccaro 2024.
- A taxonomy of risks: Hammond 2025.
- No review of the whole problem was found (see [frame](frame.md), last section).

## 4. Formal search

Counts are from OpenAlex, title and abstract field, on 2026-11-02, with no key and no account. One query timed out and was not rerun.

| String | Database | Hits |
|---|---|---|
| moral hazard in teams | OpenAlex | 496 |
| team theory Marschak Radner | OpenAlex | 18 |
| principal-agent problem | OpenAlex | 13,224 |
| multi-agent reinforcement learning survey | OpenAlex | 588 |
| multi-agent debate language models | OpenAlex | 761 |
| multi-agent failure taxonomy language model | OpenAlex | 197 |
| decentralized POMDP communication cost | OpenAlex | 24 |
| intelligent AI delegation | OpenAlex | 153 |
| cooperative AI | OpenAlex | 6,208 |
| mechanism design language model agents | OpenAlex | 3,612 |
| human-AI teaming delegation | OpenAlex | 131 |
| large language model multi-agent survey | OpenAlex | timed out |

- arXiv title and abstract searches by category (cs.MA, cs.AI) covered surveys and failures of language-model agent systems.
- Two strings gave 18 results, which were screened.
- A third string, on the principal-agent problem, failed on a network error.
- Snowballing: backward from Guo 2024, Cemri 2025 and Kim 2025; forward from Holmström 1982 by title only, since its citing list was not opened.
- Each source's own page was fetched without sign-in. A paywalled source was located by Crossref and marked "located only".

## 5. Grey search

- Types and producers: engineering blogs of companies that build agents (two producers), classic practitioner texts (a magazine paper and a book).
- One web search string, "writing a brief for subagents delegation lessons multi-agent coding agents orchestrator worker", returned 7 results, all course notes, skill files or tutorials. None was opened. They are examples of the volume of practice, not sources.
- Two company posts were fetched in full and scored.

## 6. Stopping rule

Effort bounded with saturation. Each search string stopped after 5 consecutive results that added no concept; the grey search stopped at 3 sources because the pool was already at 35. The forward search added four works, under the cap of five set for it.

## 7. Selection

- Include: a survey, a controlled or descriptive study of several agents or of delegation, a theorem on teams or contracts, or a practice text that gives a number or a rule.
- Exclude: a single-application system paper (manufacturing, driving, flight), found in the arXiv screen and set aside.
- Quality: formal sources carry an evidence grade; grey sources a score (section 8).

## 8. Quality of grey sources

Garousi Table 7: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. Threshold 10 of 20. The scores are in [sources](sources.md). A company page reporting its own system is its owner's claim.

The criteria list company pages at tier 2 (0.5 for outlet) and blogs at tier 3 (0). The three grey sources are company blog posts, and were scored tier 3 as in the first pass. A reader who takes them as company pages would add 0.5 to each. This is a rule the maintainer should settle.

## 9. Extraction and synthesis

Per source: the claim, the number, where it was read. Synthesis is narrative by question, traceable through the table in [sources](sources.md).

## 10. Not searched, and limits

- Not searched: Google Scholar, Scopus, Web of Science, SSRN, and forums. The human-AI teaming literature outside Vaccaro 2024 is largely unread.
- Not read: the full text of the two economics classics and the book on teams; they are paywalled or scanned.
- One reviewer for the formal sources, with no inter-rater check on them. The grey sources have a second rater with poor agreement (section 12). A number read only in an abstract is marked "(secondary)".
- The forward search covers only the three seeds named in section 11, and only the most cited of Vaccaro 2024's citing works.
- No identity was sent to any service.

## 11. Forward search, added 2026-11-03

Seeds: the three works cited most in the review, by count of keys in [review](review.md). Kim 2025 has four. Vaccaro 2024 and Cemri 2025 have two each, as do Hammond 2025 and Anthropic 2025.

The tie was cut toward formal works that the review grades as measured. Hammond 2025, a report graded convention, and Anthropic 2025, a blog that no index holds, were left out.

Database: OpenAlex, citing lists by work identifier, on 2026-11-03. The client identified itself with a project name and no contact, sent no account, and spaced requests half a second apart.

| Seed | Filter | Listed | Screened |
|---|---|---|---|
| Kim 2025 | cites, the work's identifier | 1 | 1 |
| Cemri 2025 | cites, the work's identifier | 21 | 21 |
| Vaccaro 2024 | cites, the work's identifier | 597 (of 604 citations counted by the database) | top 200 by citation count |
| Vaccaro 2024, subset | title and abstract match "agent" | 88 | 88 |
| Vaccaro 2024, subset | title and abstract match "language model" or "LLM" | 101 | 101 |
| Vaccaro 2024, subset | title and abstract match "delegation", "teams" or "collaboration" | 226 | top 200 |

- Unique citing works screened by title: 406. Abstracts read: 11. Added: 4.
- Not paged: the rest of Vaccaro 2024's list below the top 200 without a keyword match. Not screened: works citing Hammond 2025 or Anthropic 2025.
- Set aside: a system paper for software engineering (Kim 2025's citer), a multi-agent annotation system, a failure-attribution method, and a fault-detection benchmark that runs on mock language models by a single author. Each is a single application or a method, not a finding about teams.
- Added, because each changes or sharpens a finding in [review](review.md):
  - Dell'Acqua 2026 (field experiment, 758 workers): the task decides the gain for people too. Review D, C.
  - Brodeur 2026 (randomised, 288 researchers in 103 teams): leaving the model to lead lost most of the result. Review D.
  - Ngo 2025 (meta-analysis, 146 experiments): augmentation helped and synergy did not. Review D.
  - Lee 2026b (pre-registered experiment, N = 269, and a survey, N = 270): a cost of delegation the saving does not show. Review D.
- Every number from these four is read in the abstract and marked "(secondary)".

## 12. Second rater, added 2026-11-03

Procedure. A second rater, a language model, scored each grey source once per pass.

- Input: the twenty criteria of Garousi 2019, Table 7, in the eight groups of the first pass, and the rule that a part of the source not in the text scores 0.
- Input, also: the source text.
- Output: eight subtotals, one per group.
- Pass 1 gave the first 12,000 characters of each text. Pass 2 gave the whole text.

The rater's scores set no score in the review. Each change in [sources](sources.md), "Changed on rereading", was made on a reread of the source, with its reason.

| Source | Review | Score in use | Rater, pass 1 | Rater, pass 2 |
|---|---|---|---|---|
| Anthropic 2024 | 11.5 | 11.5 | 3 | 6.5 |
| Anthropic 2025 | 13.5 | 14.5 | 4 | 6.5 |
| Cognition 2025 | 10.5 | 12 | 4 | 7 |

Agreement, on totals and on the threshold of 10 of 20:

| Comparison | Mean absolute difference | Kappa on the threshold |
|---|---|---|
| Review, against pass 1 | 8.2 | 0 |
| Score in use, against pass 1 | 9.0 | 0 |
| Review, against pass 2 | 5.2 | 0 |
| Score in use, against pass 2 | 6.0 | 0 |

Every disagreement above 3 points was reread, in all three sources, for both passes. Kappa is 0 because the review put all three sources above the threshold and the rater put all three below it: there is no agreement to correct for, and three sources cannot estimate kappa. It is reported, not read.

Where the rater and the review differ, from the subtotals:

- **Authority.** The rater gave 0 on all four authority criteria in both passes, including the first pass, where the named authors appear after the 12,000th character. It does not credit a company as a reputable publisher (A1) or the named authors as tied to it (A2). The reread keeps those at 1.
- **Objectivity.** The rater gave 0 in both passes. The reread gave 0.5 to balance and to the stated claims where the text shows them, and 0 to vested interest (O3) on the company pages.
- **Date.** In pass 1 the date was outside the text; in pass 2 the rater gave 1 for two of three. The reread gives 1 for all three: the page states the date in its metadata, and the text dates itself.
- **Methodology.** The rater gave 3 for each source in both passes. The reread found the limits and the specific question of the two long posts after the first 12,000 characters, which is why pass 1 scored them low.
- **Outlet.** The rater gave 0.5 for the two Anthropic posts in pass 2 and 0 in pass 1, so its outlet judgment is not stable.

Reading. The rater is harsher than the review on authority and objectivity, and does not reliably see past the start of a long text. Its scores show where a reread is needed; they do not replace the review's scores.

