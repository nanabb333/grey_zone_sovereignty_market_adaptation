# Portfolio Landing Page

## Project Summary

This project extends an academic Taiwan geopolitical risk event-study into a finished, dashboard-ready intelligence prototype. It preserves the original research design while adding evidence traceability, descriptive analytics, scenario context retrieval, validation reporting, and recruiter-accessible documentation.

## Problem Statement

Event-study projects often produce useful outputs but present them as scattered CSV files, figures, scripts, and research notes. That makes the work harder for recruiters, professors, analysts, and portfolio reviewers to evaluate quickly.

This repository turns the research workflow into a public-facing analytics product that can be reviewed through structured data, generated summaries, a static dashboard, and concise documentation.

## Why It Matters

Taiwan-related geopolitical risk sits at the intersection of security, diplomacy, semiconductor supply chains, and market interpretation. A responsible analytics prototype in this domain needs clear data lineage, cautious language, and explicit limits.

The project demonstrates how to communicate high-stakes analysis without overclaiming.

## Data Layers

- Research events: `data/events_v2.csv`
- News evidence: `data/news/news_events.csv`
- Historical market-reaction outputs: `results/event_abnormal_return_summary.csv`
- Validation outputs: `results/data_validation_report.json` and `results/data_validation_report.md`

## Analytics Layers

- News evidence summary: validates and summarizes source-evidence rows
- Event-family analytics: groups coded events into descriptive families
- Scenario similarity: retrieves historically comparable coded events for example scenarios
- Data validation: checks IDs, required fields, and event-news link integrity

## Dashboard Features

- KPI cards and latest-event summary
- Executive summary and deterministic intelligence sections
- Project metadata and validation status
- News evidence summary
- Event-family analytics
- Scenario similarity cards
- Rule-based insights and historical comparison sections

## What This Demonstrates

- Research-to-product translation
- Reproducible Python scripting
- Data documentation and validation
- Dashboard communication
- Product-oriented portfolio presentation
- Responsible analytical framing in a geopolitical-risk domain

## Limitations

The prototype is descriptive and educational. It does not provide market prediction, trading advice, investment recommendations, policy advice, or causal proof. News evidence includes placeholder-safe entries that require source verification before publication.

## Five-Minute Review Path

1. Read the top of `README.md`.
2. Review the screenshots in `docs/screenshots/`.
3. Open `docs/portfolio_case_study.md`.
4. Scan `docs/results_index.md`.
5. Run `python3 scripts/run_all_checks.py`.
6. Start the dashboard with `python3 -m http.server 8000 --bind 127.0.0.1` and open `http://127.0.0.1:8000/dashboard/`.
