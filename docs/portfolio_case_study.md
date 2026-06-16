# Portfolio Case Study

## Project Title

Taiwan Geopolitical Risk Dashboard: From Event-Study Research To Intelligence Prototype

## Problem

Geopolitical event-study outputs are often difficult for non-technical stakeholders to review. The underlying analysis may be reproducible, but the results are distributed across datasets, figures, reports, and summary files.

This project addresses that communication problem by extending an academic Taiwan geopolitical risk event-study into a dashboard-ready intelligence prototype.

## Approach

The project uses a layered architecture:

- Research layer: coded Taiwan-related geopolitical events and historical market-reaction outputs
- Evidence layer: curated news evidence linked to coded events
- Analytics layer: event-family descriptive summaries
- Scenario layer: historical similarity and context retrieval
- Dashboard layer: static analyst-facing presentation

The goal is not to add new research claims. The goal is to make existing outputs easier to inspect, explain, and reuse responsibly.

## Build Decisions

The prototype uses static files and deterministic scripts. This keeps the system reproducible and easy to review without API keys, live LLM calls, or internet access.

The repository also includes a data validation framework that checks event IDs, news IDs, required fields, event-family values, and news-to-event links.

## Outputs

Key deliverables include:

- dashboard interface in `dashboard/`
- event database in `data/events_v2.csv`
- news evidence database in `data/news/news_events.csv`
- event-family summaries in `results/event_family_summary.*`
- scenario similarity outputs in `results/scenario_similarity_results.*`
- validation report in `results/data_validation_report.*`
- methodology and portfolio documentation in `docs/`

## Portfolio Value

This project demonstrates:

- research-to-product translation
- data structuring and documentation
- reproducible Python scripting
- dashboard communication
- product framing for analyst workflows
- careful responsible-use boundaries

## What It Does Not Do

The prototype does not produce market forecasts, investment advice, automated trading signals, or causal proof. It is a descriptive, analyst-support portfolio project.

## Result

The repository now reads as an integrated geopolitical intelligence prototype rather than a collection of research artifacts. It shows how academic analytics can be made accessible for stakeholder review while preserving methodological caution.
