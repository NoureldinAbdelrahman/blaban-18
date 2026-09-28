---
id: adaptive-memetic-multi-uav-task-assignment
title: "An adaptive memetic algorithm for multi-UAV cooperative task assignment under complex constraints"
authors: ["Kai Meng", "Zonghong Jiang", "Bin Xin", "Fang Deng", "Chen Chen"]
year: 2026
venue: "Swarm and Evolutionary Computation"
doi: "10.1016/j.swevo.2026.102395"
url: "https://doi.org/10.1016/j.swevo.2026.102395"
pdf: null
tags: ["memetic-algorithm", "uav", "task-assignment", "mixed-variable", "operator-selection", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# An adaptive memetic algorithm for multi-UAV cooperative task assignment under complex constraints

> [!info] Citation
> K. Meng, Z. Jiang, B. Xin, F. Deng, and C. Chen, "An adaptive memetic algorithm for multi-UAV cooperative task assignment under complex constraints," *Swarm and Evolutionary Computation*, vol. 105, art. 102395, 2026.
> **Access:** Elsevier (paywalled). Use the DOI via the university library.

## Why this paper (pre-selected)

- **Memetic = GA + adaptive local search** — the exact bridge between our Milestone 4 (GA) and Milestone 6 (novel algorithm), with an adaptive operator-selection mechanism we can imitate.
- **Mixed-variable, heavily constrained model** (precedence, simultaneous arrival, resource capacity, capability matching) — a rich template for Milestone 2 problem formulation.
- Very recent (2026) and in a top-tier venue, so it is unlikely to be a classmate's default pick.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** Multi-UAV cooperative task assignment with task precedence, simultaneous arrival, per-task resource demand, per-UAV capacity, and capability-matching constraints.
- **Why it matters:**
- **Application domain:** Large-scale reconnaissance and strike operations.

## Research Question / Objective

-

## Contributions

- [ ] Target-bundled encoding + constraint-aware initialization for feasible solutions.
- [ ] Module-based crossover and sparrow-search-inspired mutation operators.
- [ ] Adaptive operator selection + dual-space adaptive frequency control for local search.

## Methodology

- **Problem formulation:** Mixed-variable model; weighted objective over total flight distance, maximum task completion time, and a cost-effectiveness ratio.
- **Algorithm:** Adaptive Memetic Algorithm (AMA).
- **Baselines compared:** Three prevailing methods (unknown / fill in).
- **Validation:** 100 test instances with varying UAVs and tasks.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Average relative percentage deviation reduction | 65%–92% | vs. three baselines |

- **Key findings:**
- **Best-performing method:** AMA.

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which milestones it informs:** M2 (formulation), M4 (GA), M6 (memetic + adaptive operator selection).
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

adaptive memetic algorithm, mixed-variable optimization, operator selection, multi-UAV, cooperative task assignment

## Abstract (verbatim)

Multiple unmanned aerial vehicle (multi-UAV) cooperative task assignment is a critical technology for large-scale reconnaissance and strike operations. In realistic combat environments, this problem is subject to complex constraints, including task precedence relations, simultaneous arrival requirements, task-specific resource demands, per-UAV resource capacity limits, and capability-requirement matching. However, most existing studies consider only subsets of these constraints or oversimplify their interactions, often resulting in infeasible or suboptimal task assignment solutions. To address these limitations, we formulate a mixed-variable multi-UAV cooperative task assignment model that incorporates all the aforementioned constraints and optimizes a weighted objective function comprising total flight distance, maximum task completion time, and a cost-effectiveness ratio. To efficiently solve the proposed model, we develop an adaptive memetic algorithm (AMA). Specifically, a target-bundled encoding scheme combined with a constraint-aware initialization strategy is introduced to generate high-quality feasible initial solutions. To enhance global exploration capability, a module-based crossover operator strategy and a sparrow-search-inspired mutation operator strategy are designed to effectively increase population diversity. Promising solutions are subsequently refined using knowledge-specific local search operators, with an adaptive operator selection mechanism dynamically choosing appropriate operators and a dual-space adaptive frequency control strategy determining when to activate local search based on feedback from both the decision and objective spaces. Experimental results on 100 test instances with varying numbers of UAVs and tasks demonstrate that AMA consistently outperforms three prevailing methods, achieving a 65%–92% reduction in average relative percentage deviation, thereby confirming its effectiveness and robustness.
