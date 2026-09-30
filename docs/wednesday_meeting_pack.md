# Wednesday Meeting Pack: Settle the Idea and Start the Proposal

## Important status note

This repository already contains **discussion drafts**, not team decisions:

- `proposals/use_case.md` — uncommitted working draft.
- `proposals/idea_1.md` and `proposals/idea_2.md` — locally modified working drafts.
- `proposals/proposal.md` — template-based draft to compile after the team decides.

The Wednesday meeting must approve, amend, or replace these drafts.

## Fixed requirements

- Proposal deadline: **Thursday, 1 October 2026, 23:59**.
- Maximum: **two pages, including references**.
- Two **different** project ideas, with the first treated as first priority.
- Five recent scientific articles, publication date **2019–2026**.
- At least one reviewed article should support each proposed idea.
- The course team allocates one of the two ideas.

Template: [`docs/templates/proposal_template.md`](templates/proposal_template.md).

## Bring to the meeting

Each member brings:

1. Three completed archive readings from
   [`literature/reviews/reading_assignments.md`](../literature/reviews/reading_assignments.md).
2. Corresponding rows in
   [`literature/reviews/literature_review_log.md`](../literature/reviews/literature_review_log.md).
3. One external Scholar candidate or one written archive-backed rejection reason.
4. A first choice and a backup choice for the project idea.
5. Any blocking question about feasibility, simulation, or scope.

## Suggested 60-minute agenda

1. **Rules and deadline check — 5 minutes**
   - Confirm proposal deadline, page limit, two-idea requirement, and references.
2. **Paper lightning round — 20 minutes**
   - Each member presents their highest-relevance paper in two minutes:
     problem, agents, method, result, and which idea it supports.
3. **Option comparison — 20 minutes**
   - Score Options A–C below on novelty, feasibility, simulation readiness,
     support from papers, and distinctiveness from previous course projects.
4. **Decision — 10 minutes**
   - Lock Idea 1 as priority and Idea 2 as backup.
   - Lock the five papers to cite.
5. **Proposal ownership — 5 minutes**
   - Assign literature review, Idea 1, Idea 2, references, and final PDF export.

## Draft options for discussion

### Option A — Heterogeneous renewable-site inspection with a learning-assisted method

Pre-drafted in `proposals/use_case.md` and `proposals/idea_1.md`.

- Mixed ground and aerial fleet inspects a solar or wind site.
- Joint assignment and routing under capability, battery, time-window, precedence,
  and obstacle constraints.
- Optimize energy, makespan, and workload balance.
- Novel step: feedback-driven selection of low-level search operators.

### Option B — Robust multi-objective inspection with recharging and failure handling

Pre-drafted in `proposals/idea_2.md`.

- Same inspection setting, extended with charging stations and one simulated robot
  failure.
- Return a set of energy-versus-makespan trade-off solutions.
- Novel step: multi-objective coevolutionary planning with reallocation after failure.

### Option C — Neutral archive-style alternative

A deliberately different starting point so the team is not forced into Options A/B.

- Heterogeneous delivery, warehouse, or airport service fleet.
- Joint task allocation and route planning under capacity and scheduling limits.
- Supported especially by archive papers on heterogeneous fleets, baggage handling,
  warehouse coordination, and service robots.

## Decision table

| Criterion | Option A | Option B | Option C |
| --- | --- | --- | --- |
| Novelty versus previous course projects |  |  |  |
| Feasibility before Milestones 3–6 |  |  |  |
| Simulation readiness without hardware |  |  |  |
| Strength of supporting papers |  |  |  |
| Suitability for the machine-learning bonus |  |  |  |
| Team preference |  |  |  |

Use 1–5 for each cell and choose the highest total, with Idea 1 as priority and the
runner-up as backup.

## After the decision

1. Replace or approve `proposals/use_case.md`.
2. Finalize `proposals/idea_1.md` and `proposals/idea_2.md`.
3. Compile `proposals/proposal.md` from the approved ideas.
4. Confirm five citations against publication years and themes.
5. Export to PDF and submit on CMS before **1 October 2026, 23:59**.

## Discord resources still needed

I cannot access Discord, so please paste these into the meeting notes:

- Official proposal document link.
- CMS template or submission confirmation.
- Previous-publications source link, if different from the local archive.
- Team roster and contact person.
- Any dataset, simulator, or coding constraints posted by the course team.
