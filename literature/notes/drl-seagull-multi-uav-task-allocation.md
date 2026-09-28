---
id: drl-seagull-multi-uav-task-allocation
title: "A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration"
authors: ["Lijing Qin", "Zhao Zhou", "Huan Liu", "Zhengang Yan", "Yongqiang Dai"]
year: 2025
venue: "Drones"
doi: "10.3390/drones9060436"
url: "https://doi.org/10.3390/drones9060436"
pdf: literature/papers/drl-seagull-multi-uav-task-allocation.pdf
tags: ["reinforcement-learning", "swarm-intelligence", "multi-uav", "task-allocation", "adaptive-strategy", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration

> [!info] Citation
> L. Qin, Z. Zhou, H. Liu, Z. Yan, and Y. Dai, "A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration," *Drones*, vol. 9, no. 6, art. 436, 2025.
> **Access:** Open access (MDPI, CC BY 4.0). [Local PDF](../papers/drl-seagull-multi-uav-task-allocation.pdf) · [DOI](https://doi.org/10.3390/drones9060436)

## Why this paper (pre-selected)

- **DRL controls a swarm optimizer's search phases** (migration / attack / post-attack) — a concrete, OA example of learning-assisted metaheuristics, directly feeding the optional ML bonus.
- **Multi-objective, multi-constraint model** (max completion time and total flow time; collaboration, priority, range limits) is a ready M2 template.
- Benchmarked against **five swarm algorithms**, useful baselines for M5.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** Multi-UAV collaborative task allocation under collaboration, priority and range constraints (plateau grassland restoration).
- **Why it matters:**
- **Application domain:** Agricultural / ecological multi-UAV operations.

## Research Question / Objective

-

## Contributions

- [ ] Multi-objective multi-constraint collaborative task allocation problem (MOMCCTAP) model.
- [ ] DRL-driven seagull optimization (DRL-SOA): DQN adapts search factors and selects local-search strategies per phase.

## Methodology

- **Problem formulation:** Minimize max completion time and total flow time, subject to UAV range, priority and coordination constraints.
- **Algorithm:** DRL-SOA (seagull optimization controlled by a DQN agent across migration/attack/refinement).
- **Baselines compared:** Five advanced swarm-intelligence algorithms.
- **Validation:** Eight sets of benchmark cases.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:** Better convergence speed and solution diversity than the five baselines.
- **Best-performing method:** DRL-SOA.

## Strengths

-

## Limitations & Threats to Validity

- No explicit energy-consumption model and static task environment (authors' stated limitation).

## Relevance to Our Project

- **Which milestones it informs:** M2 (multi-objective model), M5 (swarm baselines), M6 (DRL-driven adaptive selection), ML bonus.
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

deep reinforcement learning, seagull optimization, multi-UAV, task allocation, multi-objective, adaptive search

## Abstract (verbatim)

The rapid advancement of unmanned aerial vehicle (UAV) technology has enabled the coordinated operation of multi-UAV systems, offering significant applications in agriculture, logistics, environmental monitoring, and disaster relief. In agriculture, UAVs are widely utilized for tasks such as ecological restoration, crop monitoring, and fertilization, providing efficient and cost-effective solutions for improved productivity and sustainability. This study addresses the collaborative task allocation problem for multi-UAV systems, using ecological grassland restoration as a case study. A multi-objective, multi-constraint collaborative task allocation problem (MOMCCTAP) model was developed, incorporating constraints such as UAV collaboration, task completion priorities, and maximum range restrictions. The optimization objectives include minimizing the maximum task completion time for any UAV and minimizing the total time for all UAVs. To solve this model, a deep reinforcement learning-based seagull optimization algorithm (DRL-SOA) is proposed, which integrates deep reinforcement learning with the seagull optimization algorithm (SOA) for adaptive optimization. The algorithm improves both global and local search capabilities by optimizing key phases of seagull migration, attack, and post-attack refinement. Evaluation against five advanced swarm intelligence algorithms demonstrates that the DRL-SOA outperforms the alternatives in convergence speed and solution diversity, validating its efficacy for solving the MOMCCTAP.
