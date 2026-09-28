---
id: energy-learning-hyper-heuristic-heterogeneous-uav
title: "Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints"
authors: ["Mengshun Yuan", "Mou Chen", "Tongle Zhou", "Zengliang Han"]
year: 2025
venue: "Defence Technology"
doi: "10.1016/j.dt.2025.06.006"
url: "https://doi.org/10.1016/j.dt.2025.06.006"
pdf: null
tags: ["hyper-heuristic", "uav", "task-assignment", "energy", "operator-selection", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints

> [!info] Citation
> M. Yuan, M. Chen, T. Zhou, and Z. Han, "Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints," *Defence Technology*, vol. 54, pp. 1–14, 2025.
> **Access:** Open access (Elsevier / KeAi). Download from the DOI link.

## Why this paper (pre-selected)

- **Hyper-heuristic, not another named swarm algorithm** — it learns *how to pick* low-level operators via an "energy learning" mechanism instead of relying on one metaphor. Ideal seed for the Milestone 6 novel algorithm.
- **Energy is the optimization currency**, matching our goal of energy-aware cooperative assignment.
- The authors benchmark **against PSO and GWO**, giving us ready baselines for Milestone 5.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** Cooperative task assignment for heterogeneous UAVs under complex constraints (task types, time windows, payload limits).
- **Why it matters:**
- **Application domain:** Multi-UAV / UAV-swarm operations.

## Research Question / Objective

-

## Contributions

- [ ] Three-layer encoding (task sequence, UAV sequence, waiting time).
- [ ] Energy-learning hyper-heuristic that adaptively updates operator selection probabilities.
- [ ] Directed-graph task-order and time-adjustment strategies.

## Methodology

- **Problem formulation:** Mathematical model with complex constraints and an explicit objective function.
- **Algorithm:** Energy learning hyper-heuristic (EL-HH); adaptive operator selection; multiple optimization operators.
- **Baselines compared:** PSO, GWO, other conventional metaheuristics.
- **Validation:** Simple and complex simulation scenes plus real indoor experiments.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:** Faster convergence and higher solution quality than PSO/GWO as constraints and problem size grow.
- **Best-performing method:** EL-HH.

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which milestones it informs:** M5 (baselines), M6 (hyper-heuristic / adaptive operator selection), optional ML bonus.
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

hyper-heuristic, operator selection, energy learning, heterogeneous UAVs, cooperative task assignment, complex constraints

## Abstract (verbatim)

Cooperative task assignment is one of the key research focuses in the field of unmanned aerial vehicles (UAVs). In this paper, an energy learning hyper-heuristic (EL-HH) algorithm is proposed to address the cooperative task assignment problem of heterogeneous UAVs under complex constraints. First, a mathematical model is designed to define the scenario, complex constraints, and objective function of the problem. Then, the scheme encoding, the EL-HH strategy, multiple optimization operators, and the task sequence and time adjustment strategies are designed in the EL-HH algorithm. The scheme encoding is designed with three layers: task sequence, UAV sequence, and waiting time. The EL-HH strategy applies an energy learning method to adaptively adjust the energies of operators, thereby facilitating the selection and application of operators. Multiple optimization operators can update schemes in different ways, enabling the algorithm to fully explore the solution space. Afterward, the task order and time adjustment strategies are designed to adjust task order and insert waiting time. Through the iterative optimization process, a satisfactory assignment scheme is ultimately produced. Finally, simulation and experiment verify the effectiveness of the proposed algorithm.
