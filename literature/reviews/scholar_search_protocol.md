# Scholar Search Protocol

Use this alongside the previous-publications archive. The team leader's mandatory
keywords are: `robotics`, `multi-agent`, `cooperative`, `meta-heuristics`,
`optimization`.

## Search setup

- Date filter: **2019–2026** for the proposal.
  - Milestone 2 later allows **2018–2026**.
- Prefer peer-reviewed, open-access papers with an identifiable optimization method
  and empirical evaluation.
- Record kept and rejected papers in
  [`literature_review_log.md`](literature_review_log.md); never keep a paper only
  because it matched the keywords.

## Starting queries

Copy, adapt, and record the exact query used.

1. `"multi-agent" cooperative robotics task allocation metaheuristic`
2. `"heterogeneous robot fleet" task allocation routing metaheuristic`
3. `"Unmanned Aerial Vehicle" cooperative task assignment energy time window`
4. `"multi-robot" surveillance task allocation route planning`
5. `"hyper-heuristic" task assignment heterogeneous robots`
6. `"memetic algorithm" multi-robot task allocation`
7. `"multi-objective" "task allocation" heterogeneous robots`
8. `"adaptive operator selection" routing scheduling optimization`
9. `"energy-aware" multi-robot task allocation recharging`
10. `"robust" multi-robot task allocation failure uncertainty`

## Inclusion rules

Keep a paper if it has all of the following:

- A cooperative multi-agent robotics or autonomous-system problem.
- An identifiable optimization or metaheuristic method.
- A clear decision being optimized: assignment, routing, scheduling, or a combination.
- Publication year 2019–2026.
- Enough methodological detail to reproduce or adapt the idea.

## Exclusion rules

Reject a paper if any of the following is true:

- Only one vehicle or robot with no cooperation.
- Pure traffic or power-grid optimization with no autonomous agents.
- Year outside 2019–2026.
- No method, results, or accessible full text for the proposal stage.
- The manufacturing or general scheduling problem has no cooperative fleet.

## Snowball rule

For each kept paper, check:

1. One paper it cites that handles constraints or a method better.
2. One newer paper that cites it, if available.
3. Add only genuinely better candidates; stop when new papers repeat the same method.

## Minimum pre-Wednesday target

- Each reader records **at least one external candidate or one archive-backed
  rejection reason** in the log.
- The team leaves Wednesday with **five locked papers** for the proposal.
