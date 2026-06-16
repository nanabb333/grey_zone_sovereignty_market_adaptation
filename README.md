# AI Geopolitical Risk Dashboard

## Portfolio Positioning

This repository is the product layer of a three-part Taiwan geopolitical risk portfolio:

```text
Research → Analytics → Product
```

Repo 1 develops the research question and interpretation framework. Repo 2 turns the event-study workflow into a reproducible analytics engine. Repo 3 converts those analytics outputs into a dashboard-ready decision-support product for geopolitical risk analysis.

| Repository | Role | Portfolio Signal |
|---|---|---|
| Repo 1: Grey-Zone Sovereignty and Market Adaptation | Research | Research design and interpretation |
| Repo 2: Taiwan Geopolitical Risk Event Study Engine | Analytics Engine | Reproducible event-study workflow |
| Repo 3: AI Geopolitical Risk Dashboard | Decision-Support Product | Productized analytics for risk interpretation |

## Product Problem

Event-study outputs are useful, but CSV files, figures, and Markdown reports are slow for executives and analysts to review manually.

Risk analysts, business analytics teams, and strategy stakeholders need a clear interface that summarizes event-level market reactions, compares events against mechanism-level patterns, surfaces deterministic insights, and prepares executive-facing summaries.

## Product Solution

This dashboard turns Repo 2 outputs into an analyst-facing decision-support workspace.

It provides KPI cards, latest-event review, executive summaries, rule-based insights, historical comparisons, deterministic executive briefs, and LLM-ready context for future analyst-reviewed AI workflows.

The current version uses deterministic rules only. It does not use live LLM calls, external APIs, forecasting, trading recommendations, or automated investment advice.

## Decision-Support Value

The dashboard helps analysts and stakeholders answer:

- Which events produced the strongest positive or negative abnormal returns?
- How do individual events compare with mechanism-level averages?
- What event-study outputs support an analyst explanation?
- What summary can be shared with non-technical stakeholders?
- What structured context is available for future analyst-reviewed LLM support?

## Dashboard Screenshots

Executive dashboard:

![Dashboard Home](docs/screenshots/dashboard_home.png)

Dashboard intelligence layer:

![Dashboard Intelligence](docs/screenshots/dashboard_intelligence.png)

## Executive User Value

The dashboard is designed for fast executive review of Taiwan-related geopolitical risk analytics.

It helps non-technical stakeholders understand:

- key risk indicators from the latest event-study run
- strongest positive and negative market reactions
- event interpretation using benchmark-adjusted abnormal CAR
- mechanism-level historical comparisons
- rule-based insights that require analyst review
- concise executive brief language for discussion

## Data Inputs

The dashboard consumes structured outputs from Repo 2:

| Input | Purpose |
|---|---|
| `results/dashboard_data.csv` | Event-level dashboard dataset |
| `results/mechanism_summary.csv` | Mechanism-level summary |
| `results/executive_summary.md` | Executive-facing run summary |
| `results/event_insights.json` | Rule-based event insights |
| `results/historical_comparison.json` | Event-versus-mechanism comparison metadata |
| `results/executive_brief.json` | Deterministic executive brief |
| `results/llm_context.json` | Structured context for future analyst-reviewed LLM use |
| `results/news_database_summary.json` | Curated news-evidence summary for future source drilldowns |

## News Evidence Database Layer

The repository now includes a curated news-evidence layer in `data/news/news_events.csv`. This layer links geopolitical events and related candidate events to structured source evidence, including event family, actor, geography, summary notes, and analyst coding notes.

The layer is designed as evidence enrichment for future analysis and dashboard drilldowns. It does not replace the original event-study design, alter the empirical results, forecast markets, or provide investment advice. Placeholder rows should be verified against exact source URLs before publication or formal research use.

Generate the summary outputs with:

```bash
python3 scripts/build_news_event_database.py
```

## Intelligence Layer

The intelligence layer is deterministic and auditable.

It includes:

- `event_insights.json`: rule-based event insights derived from Repo 2 outputs
- `historical_comparison.json`: event-versus-mechanism comparison metadata
- `executive_brief.json`: deterministic executive brief content
- `llm_context.json`: structured context for future analyst-reviewed LLM support

The intelligence layer summarizes existing analytics outputs. It does not create new event classifications, forecasts, trading recommendations, or unsupported claims.

## Dashboard Features

Current dashboard views include:

- KPI cards
- latest event review
- executive summary display
- historical comparison section
- executive brief section
- LLM-ready context summary
- rule-based insight panel

The dashboard is designed as a decision-support product, not a prediction system.

## How to Run

From the repository root, start a local server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8000/dashboard/
```

The dashboard reads static outputs from `results/` and renders the product interface from `dashboard/`.

## Product Analytics Skills Demonstrated

- Product analytics
- Business analytics
- Risk analytics
- Strategy analytics
- KPI design
- Dashboard information architecture
- Stakeholder-focused analytics communication
- Decision-support product thinking
- Rule-based insight generation
- Executive communication
- AI product analytics
- LLM-ready context design

## Portfolio Documentation

- [Repo 3 Case Study](docs/repo3_case_study.md)
- [Repo 3 Product Spec](docs/repo3_product_spec.md)
- [Dashboard Information Architecture](docs/dashboard_information_architecture.md)
- [Dashboard Wireframe](docs/dashboard_wireframe.md)
- [AI Workflow Design](docs/ai_workflow_design.md)
- [Research to Product Story](docs/research_to_product_story.md)

## Responsible Use Boundary

This dashboard is for academic, educational, and portfolio demonstration purposes.

It does not provide:

- forecasting
- trading recommendations
- investment advice
- policy advice
- live LLM-generated interpretation
- external API-based analysis

All dashboard intelligence should be treated as analyst-review support.

## Future Enhancements

- Add analyst-reviewed LLM explanation drafts using `llm_context.json`
- Add dashboard filters for event mechanism and direction
- Add event-detail drilldowns linked to reports and figures
