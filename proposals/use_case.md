# Use Case — Cooperative Inspection of a Renewable-Energy Site

## One-line pitch

A heterogeneous fleet of ground robots and aerial drones cooperatively inspects a
solar (or wind) farm: it decides **which inspection point each robot handles and in
what order**, to minimize energy use and mission time while balancing workload and
respecting each robot's sensors, battery range and the site's no-go zones.

## Scenario

A renewable-energy operator must periodically inspect a site for defects (hot spots,
soiling, cracks, loose connections, structural damage). Manual inspection is slow
and, for aerial assets, risky. A mixed fleet — some tasks need a ground robot that
can walk a row and take electrical readings; others need a drone that can fly over
panels or turbine blades — performs the inspection instead. The cooperative
challenge is that the robots are **not interchangeable**: they carry different
sensors, move at different speeds, and have different energy budgets, so both the
**assignment** and the **visit order** must be planned together.

## Agents (heterogeneous fleet)

| Robot | Type | Sensors / capability | Speed | Energy budget | Notes |
| --- | --- | --- | --- | --- | --- |
| Ground 1 | Ground | Visual, Electrical | Low | High | Walks service roads; precise measurements |
| Ground 2 | Ground | Visual | Low | High | Backup visual coverage |
| Drone 1 | Aerial | Aerial Visual | High | Low | Fast wide-area survey |
| Drone 2 | Aerial | Thermal | High | Low | Hot-spot detection |
| Drone 3 | Aerial | LiDAR | High | Low | Structural and terrain scan |

Counts are tunable (typically 2–3 ground and 2–5 aerial).

## Tasks (inspection points)

| Task group | Count (default) | Required capability | Time window | Precedence | Priority |
| --- | --- | --- | --- | --- | --- |
| Visual survey | 20 | Visual or Aerial Visual | Any | Before electrical/thermal on the same asset | Medium |
| Thermal inspection | 10 | Thermal | Midday window | — | High |
| Electrical check | 6 | Electrical | Any | After visual survey | High |
| LiDAR scan | 4 | LiDAR | Any | — | Low |

Total default workload: 40 tasks. Counts, windows and precedences are parameters.

## Environment

- 2D site (default 2 km × 2 km) with a depot and optional charging stations.
- No-go zones (control building, roads, keep-out areas) that force detours.
- Inspection points are known in advance; the environment is otherwise static.
- Distance between points is **obstacle-aware**, not straight-line.

## Decision variables

1. **Assignment:** whether robot *i* performs task *j* with capability *k*.
2. **Routing:** the visiting sequence (permutation) of assigned tasks per robot.
3. **Optional:** charging stops and waiting times (used in Idea #2).

## Objective(s)

Default: a multi-objective model that we can weight or Pareto-optimize.

1. **Energy:** total energy consumed by the fleet (robot-specific consumption).
2. **Makespan:** time until the last robot finishes.
3. **Workload balance:** spread of busy time (or energy) across robots.

Coverage of all tasks is a **hard constraint**, not an objective.

## Constraints

- Every required task is inspected by exactly one robot that has the needed capability.
- Capability–task matching (a LiDAR task cannot go to a thermal drone).
- Per-robot energy budget is not exceeded (with recharging in Idea #2).
- Each robot starts and ends at the depot; routes are continuous.
- Time windows and task precedence are respected.
- Paths avoid no-go zones.
- (Optional, simplified) no two robots occupy the same cell at the same time.

## Simulation and metrics

- 2D continuous or discrete site with an obstacle-aware path length computed once.
- Deterministic mission simulation: energy proportional to travelled distance
  (optionally plus hover cost for drones) and makespan from the slowest robot.
- Metrics: total energy, makespan, total distance, workload standard deviation,
  coverage percentage, runtime, convergence curves, hypervolume for the
  multi-objective runs, and statistical comparisons over repeated seeds.

## Assumptions and simplifications

- No hardware: everything is simulated.
- Known, static inspection points; deterministic travel; no wind.
- Constant speed per robot; energy modelled as a coefficient times distance.
- Collision avoidance captured through obstacle-aware distances, not full dynamics.

## Why this use case

- Clearly on the course theme: multi-agent cooperative robotics, simulated, no hardware.
- Naturally **heterogeneous**, so capability constraints are meaningful.
- **Energy is central**, which fills the main gap found in the five reviewed papers.
- Distinct from the disaster search-and-rescue scenarios already present in the
  course archive.
- Straightforward to simulate in Python and to scale up or down for comparisons.
- It maps directly onto the reviewed work: capability-preserving encoding (Nait
  Chabane), energy-aware hyper-heuristics (Yuan), dual-level routing search (Cheng),
  multi-objective formulations (Qin, Chen).
