# Use Cases (team choice — not decided)

Two candidate settings. Both are simulated, multi-agent, and need joint task
assignment plus routing.

## A — Agricultural ground-robot monitoring (Idea 1)

- Fleet: 3–5 ground robots with different sensors (soil probe, camera, sprayer).
- Tasks: soil sampling, weed mapping, pest scouting points in a field.
- Decide: task-to-robot assignment and visit order.
- Minimize: energy, mission time; balance workload.
- Respect: sensor–task match, battery range, crop-row no-go lines, spray time
  windows, scout-before-spray precedence.

## B — Planetary-surface cooperative exploration (Idea 2)

- Fleet: 3–6 heterogeneous rovers (imager, spectrometer, sampler) plus a lander relay.
- Tasks: science targets needing specific instruments, with priority and
  illumination windows.
- Decide: assignment, routes, recharge and waiting timing.
- Minimize: energy and makespan; maximize science return; balance workload.
- Respect: instrument match, slope and crater no-go zones, battery plus solar
  recharge, communication range to the lander, image-before-sample precedence.

## Shared simulation rules

- 2D site, known static targets, obstacle-aware distances.
- Energy proportional to distance; constant speeds; no hardware.
