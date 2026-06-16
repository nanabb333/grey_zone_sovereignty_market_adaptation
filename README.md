# Taiwan Geopolitical Risk Intelligence Dashboard

Portfolio project: an academic Taiwan geopolitical risk event-study extended into a dashboard-ready intelligence prototype for analyst review, evidence traceability, and stakeholder communication.

## Quick Review Path

For a five-minute portfolio review:

1. Read the project overview below.
2. Skim the screenshots in this README.
3. Open [Portfolio Landing Page](docs/portfolio_landing_page.md).
4. Review [Results Index](docs/results_index.md).
5. Run `python3 scripts/run_all_checks.py`.
6. Launch the dashboard locally from the repository root.

## Project Overview

This project starts from an academic event-study on Taiwan-related geopolitical shocks and extends it into a polished, dashboard-ready intelligence prototype. The repository keeps the original event-study design intact while adding structured evidence, descriptive analytics, scenario context retrieval, data validation, and portfolio-facing documentation.

The result is a research-to-product portfolio piece: rigorous enough to show methodological discipline, structured enough to show analytics engineering, and accessible enough for recruiters or stakeholders to understand the product value quickly.

The prototype is designed for historical similarity analysis, evidence enrichment, descriptive scenario comparison, and dashboard communication. It does not provide market prediction, investment advice, automated trading signals, or unsupported causal claims.

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

## What This Project Demonstrates

- Research-to-product translation from event-study outputs to a static dashboard prototype
- Structured data design across event coding, news evidence, analytics, and scenario retrieval
- Cautious geopolitical risk communication for analyst review
- Deterministic intelligence workflows without API keys, live LLM calls, or internet dependency
- Portfolio-ready product framing without changing validated research claims

## Decision-Support Value

The dashboard helps analysts and stakeholders answer:

- Which events produced the strongest positive or negative abnormal returns?
- How do individual events compare with mechanism-level averages?
- What event-study outputs support an analyst explanation?
- What summary can be shared with non-technical stakeholders?
- What structured context is available for future analyst-reviewed LLM support?

## Dashboard Screenshots

The dashboard is static and local-file friendly. It presents the project as an analyst-support workspace rather than a notebook-only research artifact.

Executive dashboard:

![Dashboard Home](docs/screenshots/dashboard_home.png)

Dashboard intelligence layer:

![Dashboard Intelligence](docs/screenshots/dashboard_intelligence.png)

Additional screenshot targets are tracked in [GitHub Publication Checklist](docs/github_publication_checklist.md).

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
| `results/event_family_summary.json` | Descriptive event-family analytics linking events, news evidence, and CAR outputs |
| `results/scenario_similarity_results.json` | Historical similarity results for example scenario comparison |

## Data Layers

The repository now separates source material into clear data layers:

- event database: `data/events_v2.csv`
- curated news evidence: `data/news/news_events.csv`
- market-reaction outputs: `results/event_abnormal_return_summary.csv`
- dashboard-ready summaries: `results/*.json` and `results/*.md`

## Data Architecture

The intelligence prototype follows a layered architecture:

```text
Research Layer -> Evidence Layer -> Analytics Layer -> Scenario Layer -> Dashboard Layer
```

The research layer preserves the original event-study data and outputs. The evidence layer adds curated news-source context. The analytics layer summarizes event-family patterns. The scenario layer retrieves historically similar coded events. The dashboard layer presents these static outputs for analyst review.

Each event in `data/events_v2.csv` has a persistent `event_id` in `E###` format, and downstream evidence or scenario outputs use that ID where possible.

## Analytics Layers

The analytics layer is descriptive and reproducible:

- `scripts/build_news_event_database.py` validates and summarizes curated news evidence
- `scripts/analyze_event_family_patterns.py` summarizes historical market reactions by event family
- `scripts/scenario_similarity.py` retrieves historically similar coded events for example scenarios
- `scripts/validate_project_data.py` checks data integrity and linkage health

## Data Integrity

Core data quality conventions:

- stable `event_id` values in `data/events_v2.csv`
- stable `news_id` values in `data/news/news_events.csv`
- explicit `related_event_id` links from news evidence to coded events
- generated validation reports in `results/data_validation_report.json` and `results/data_validation_report.md`

One contextual news row may remain intentionally unlinked when the evidence item is relevant but not represented as a coded event in `data/events_v2.csv`; this is surfaced as a validation warning for analyst review.

## Validation Framework

Run the project validation check with:

```bash
python3 scripts/validate_project_data.py
```

The validator checks duplicate event IDs, missing event IDs, orphan news records, invalid event-family values, missing critical fields, and duplicate news IDs. The dashboard metadata panel displays the validation status from the generated report.

## News Evidence Database Layer

The repository now includes a curated news-evidence layer in `data/news/news_events.csv`. This layer links geopolitical events and related candidate events to structured source evidence, including event family, actor, geography, summary notes, and analyst coding notes.

The layer is designed as evidence enrichment for future analysis and dashboard drilldowns. It does not replace the original event-study design, alter the empirical results, forecast markets, or provide investment advice. Placeholder rows should be verified against exact source URLs before publication or formal research use.

Generate the summary outputs with:

```bash
python3 scripts/build_news_event_database.py
```

## Event Family Analytics

The repository now summarizes market-reaction outputs by geopolitical event type using the existing `event_family` coding in `data/events_v2.csv`. The event-family layer connects curated event records, structured news evidence, and available CAR outputs to support descriptive comparison across categories such as military exercises, diplomatic shocks, export controls, and strategic investments.

This layer is descriptive and analyst-reviewed. It does not change the event-study methodology, infer causality, forecast market outcomes, or provide investment advice.

Generate the event-family outputs with:

```bash
python3 scripts/analyze_event_family_patterns.py
```

## Scenario Similarity Layer

The repository now includes a scenario similarity layer that compares example geopolitical scenarios against historical coded events. It supports historical similarity, context retrieval, and scenario comparison by matching scenario text to event-family coding, actor metadata, geography metadata, linked news evidence, surprise coding, repetition level, and available historical CAR context.

This layer helps users retrieve similar precedents and supporting evidence for analyst review. It does not change the event-study methodology or treat historical market reactions as future-market estimates. Scenario case briefs are available in `docs/scenario_case_briefs.md`.

Generate the scenario similarity outputs with:

```bash
python3 scripts/scenario_similarity.py
```

## Dashboard Prototype

The static dashboard in `dashboard/` presents event-study outputs, evidence summaries, event-family analytics, and scenario similarity results in one local-file-friendly interface. It requires no API key, internet access, or LLM call.

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
- news evidence summary
- event-family analytics
- scenario similarity cards
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

## Reproduce Outputs

Run the full release check:

```bash
python3 scripts/run_all_checks.py
```

Or run the core scripts individually:

```bash
python3 scripts/build_news_event_database.py
python3 scripts/analyze_event_family_patterns.py
python3 scripts/scenario_similarity.py
python3 scripts/validate_project_data.py
```

See [Reproducibility Guide](docs/reproducibility_guide.md) for expected outputs and known validation warnings.

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

## Portfolio Framing

This repository is designed to show four portfolio signals:

- Research judgment: the project preserves method boundaries and avoids unsupported claims.
- Analytics engineering: scripts generate structured outputs and validation reports.
- Data product thinking: research artifacts are translated into a dashboard workflow.
- Communication quality: documentation is written for analysts, recruiters, and stakeholders.

## Portfolio Documentation

- [Portfolio Landing Page](docs/portfolio_landing_page.md)
- [Results Index](docs/results_index.md)
- [Reproducibility Guide](docs/reproducibility_guide.md)
- [Repository Quality Audit](docs/repository_quality_audit.md)
- [Executive Walkthrough](docs/executive_walkthrough.md)
- [Portfolio Case Study](docs/portfolio_case_study.md)
- [Recruiter Summary](docs/recruiter_summary.md)
- [GitHub Publication Checklist](docs/github_publication_checklist.md)
- [Repo 3 Case Study](docs/repo3_case_study.md)
- [Repo 3 Product Spec](docs/repo3_product_spec.md)
- [Dashboard Information Architecture](docs/dashboard_information_architecture.md)
- [Dashboard Wireframe](docs/dashboard_wireframe.md)
- [AI Workflow Design](docs/ai_workflow_design.md)
- [Research to Product Story](docs/research_to_product_story.md)
- [Scenario Similarity Methodology](docs/scenario_similarity_methodology.md)
- [Scenario Case Briefs](docs/scenario_case_briefs.md)
- [Intelligence Product Positioning](docs/intelligence_product_positioning.md)

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

## Limitations

The repository uses curated datasets and deterministic summary scripts. News evidence includes placeholder-safe starter rows that require exact source verification before publication. Scenario similarity scores are transparent retrieval aids and should not be interpreted as severity measures, causal estimates, or future-market estimates.

## Future Enhancements

- Add analyst-reviewed LLM explanation drafts using `llm_context.json`
- Add dashboard filters for event mechanism and direction
- Add event-detail drilldowns linked to reports and figures
