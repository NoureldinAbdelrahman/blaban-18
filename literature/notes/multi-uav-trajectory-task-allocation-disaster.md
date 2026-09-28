---
id: multi-uav-trajectory-task-allocation-disaster
title: "Multi-UAV Trajectory Planning and Task Allocation for Disaster Rescue Operations"
authors: ["Yousra M. Aljifri", "Sarah H. Shaaban", "Farida B. El-Saadawy", "Yousef H. Ali", "Youssof M. Awad", "Youssef M. El-Khawanky", "Dalia M. Mahfouz", "Omar M. Shehata"]
year: null
tags: ["uav", "trajectory-planning", "task-allocation", "disaster-relief"]
pdf: literature/papers/multi-uav-trajectory-task-allocation-disaster.pdf
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Multi-UAV Trajectory Planning and Task Allocation for Disaster Rescue Operations

> [!info] Citation
> Yousra M. Aljifri, Sarah H. Shaaban, Farida B. El-Saadawy, Yousef H. Ali, Youssof M. Awad, Youssef M. El-Khawanky, Dalia M. Mahfouz, Omar M. Shehata. *Multi-UAV Trajectory Planning and Task Allocation for Disaster Rescue Operations*. [PDF](../papers/multi-uav-trajectory-task-allocation-disaster.pdf)

## TL;DR

_One or two sentences capturing the core contribution in your own words._

## Problem & Motivation

- **Problem addressed:**
- **Why it matters:**
- **Application domain:**

## Research Question / Objective

-

## Contributions

- [ ]
- [ ]

## Methodology

- **Problem formulation:** (decision variables, objective(s), constraints)
- **Algorithms / techniques:**
- **Baselines compared:**
- **Datasets / environments:**

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:**
- **Best-performing method:**

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which of our milestones it informs:** (formulation / SA / GA / swarm / novel algorithm)
- **Ideas it suggests for our problem:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Notable Quotes

> "..." (p. )

## Keywords

multi-UAV, trajectory planning, task allocation, disaster rescue, VRPTW, endurance

## Abstract (verbatim)

This paper presents a constrained multi-UAV routing framework for disaster rescue missions that incorporates load-dependent endurance coupling and time-window constraints within a unified optimization model. Segment cost is dynamically linked to remaining payload, capturing realistic energy–mass interactions during flight. The objective integrates travel cost, UAV activation cost, temporal penalties, and utilization efficiency rewards. Two solution strategies are proposed: a Discrete Teaching–Learning-Based Optimization with Local Search (DTLBO-II-LS), featuring class-based learning and embedded local search operators for robust low-variance combinatorial routing, and a policy-gradient Reinforcement Learning formulation (REINFORCE) that generates adaptive routing policies through episodic sampling without predefined neighborhood operators. Both are benchmarked against three classical metaheuristics: Simulated Annealing (SA), Genetic Algorithm (GA), and Particle Swarm Optimization (PSO) under a unified framework. Across 10- and 20-node scenarios, DTLBO-II-LS attains the lowest variance (4.64 over 20 runs) and outperforms GA by approximately 2% in larger instances, demonstrating superior robustness and convergence stability, while SA achieves the best single-run cost (−950.41). REINFORCE produces competitive feasible solutions and demonstrates adaptive behavior, though variability increases with problem scale. These results demonstrate that structured discrete metaheuristics (SA, GA, DTLBO-II-LS) offer superior solution quality and robustness for time-critical UAV disaster response, while learning-based routing (REINFORCE) provides a flexible, operator-free alternative whose scalability can be improved through enhanced policy parameterization and reward design. The two paradigms thus represent complementary directions: metaheuristics for deployment-ready optimization and RL for adaptive long-term learning.
