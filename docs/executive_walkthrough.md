# Executive Walkthrough

## What This Project Is

This repository presents an academic Taiwan geopolitical risk event-study extended into a dashboard-ready geopolitical intelligence prototype.

The project keeps the original research method intact and adds presentation layers that make the outputs easier to review:

- structured event data
- curated news evidence
- event-family summaries
- scenario similarity for historical context retrieval
- a static dashboard for analyst-facing communication

The prototype is for academic, portfolio, and analyst-support demonstration. It does not provide market forecasts, trading recommendations, investment advice, or automated policy guidance.

## Executive Narrative

The original research problem asks how Taiwan-related geopolitical events are reflected in market behavior. The dashboard prototype turns that research into a more accessible product experience.

Instead of asking a reviewer to inspect many CSV files, reports, and figures manually, the project organizes the work into a decision-support flow:

1. Review the coded geopolitical event database.
2. Inspect curated source evidence linked to events.
3. Compare event families using descriptive statistics.
4. Retrieve historically similar coded events for example scenarios.
5. Present the outputs in a static dashboard.

## Dashboard Walkthrough

The dashboard opens with KPI cards and the latest event view. These summarize the event-study run and provide a compact entry point for non-technical review.

The executive summary and intelligence sections translate generated outputs into readable analyst-support language. These sections are deterministic and auditable.

The news evidence and event-family sections add traceability. They show how event coding is supported by structured evidence and how similar event families can be summarized descriptively.

The scenario similarity section compares example geopolitical scenarios against historical coded events. This is historical similarity analysis and context retrieval only.

## What A Reviewer Should Notice

- The project connects research, data engineering, analytics, documentation, and dashboard communication.
- The repository uses static, reproducible outputs rather than live external services.
- Responsible-use boundaries are explicit throughout the project.
- The dashboard is designed for analyst review rather than automated decision-making.

## Responsible Use Boundary

Historical CAR values and similarity scores are descriptive context. They should not be treated as predictions, recommendations, investment signals, or causal proof.
