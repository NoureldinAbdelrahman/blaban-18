---
id: enhanced-ga-heterogeneous-multi-robot
title: "An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems"
authors: ["Ahmed Nait Chabane", "Ouahib Guenounou"]
year: 2025
venue: "Complex & Intelligent Systems"
doi: "10.1007/s40747-025-02062-w"
url: "https://doi.org/10.1007/s40747-025-02062-w"
pdf: null
tags: ["genetic-algorithm", "heterogeneous-fleet", "task-allocation", "path-planning", "benchmark", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems

> [!info] Citation
> A. Nait Chabane and O. Guenounou, "An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems," *Complex & Intelligent Systems*, vol. 11, art. 435, 2025.
> **Access:** Open access (Springer). Download directly from the DOI link.

## Why this paper (pre-selected)

- **Open access + reproducible benchmark design** — it compares against MILP, standard GA, PSO and a surrogate-assisted EA across 50-site / 4-robot instances. That is a ready-made methodology template for Milestones 2 and 4.
- **Two-phase GA** (capability-constrained assignment, then per-robot route refinement) is a clean structure we can adapt for heterogeneous fleets.
- Ground-robot (not UAV) focus adds domain diversity to the review set.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** Task allocation and path planning for heterogeneous multi-robot systems (varying sensing capabilities) in industrial inspection.
- **Why it matters:**
- **Application domain:** Industrial inspection with heterogeneous robot fleets.

## Research Question / Objective

-

## Contributions

- [ ] Phase 1: domain-specific chromosome encoding enforcing robot-measurement compatibility.
- [ ] Phase 2: local genetic refinement of each robot's route for distance and load balancing.
- [ ] Benchmark against MILP, single-phase GA, PSO, and BL-SAEA.

## Methodology

- **Problem formulation:** Capability-constrained task assignment + route optimization.
- **Algorithm:** Two-phase enhanced genetic algorithm (EGA).
- **Baselines compared:** MILP (exact), GA (single-phase), PSO, BL-SAEA.
- **Validation:** Scenarios up to 50 inspection sites and 4 heterogeneous robots.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Average optimality gap | < 1.5% | near-optimal |
| Runtime reduction vs MILP | up to 90% | large-scale instances |

- **Key findings:**
- **Best-performing method:** EGA (accuracy/runtime trade-off).

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which milestones it informs:** M2 (formulation), M4 (GA), results analysis (benchmark design).
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

enhanced genetic algorithm, heterogeneous multi-robot systems, task allocation, route planning, MILP benchmark

## Abstract (verbatim)

Efficient task allocation and path planning in heterogeneous multi-robot systems (MRS) remains a significant challenge in industrial inspection contexts, particularly when robots exhibit diverse sensing capabilities and must operate across spatially distributed sites. To address the limitations of exact methods and conventional heuristics, we propose a novel two-phase enhanced genetic algorithm (EGA) tailored for capability-constrained task assignment and route optimization. The first phase employs a domain-specific chromosome encoding to assign tasks while enforcing robot-measurement compatibility. The second phase locally refines each robot's path to minimize travel distance and improve load balancing. We benchmark the EGA against an exact mixed integer linear programming (MILP) model, a standard genetic algorithm (single-phase), a particle swarm optimization (PSO) approach, and an adapted version of the bi-level surrogate-assisted evolutionary algorithm (BL-SAEA) across scenarios involving up to 50 inspection sites and 4 heterogeneous robots. Experimental results show that our EGA consistently produces near-optimal solutions, achieving average optimality gaps below 1.5%, while reducing computation times by up to 90% compared to MILP. Furthermore, the second phase significantly enhances convergence stability and solution robustness, especially in large-scale instances. These results demonstrate the scalability and practical suitability of the proposed method for real-time, resource-constrained industrial inspection missions.
