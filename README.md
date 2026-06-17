# Geopolitical Scenario Intelligence Engine

Portfolio project: a deterministic geopolitical risk intelligence product that turns validated Taiwan-related event research into evidence-based historical analog retrieval, scenario reasoning, analyst briefs, and a dashboard demo.

![Dashboard Intelligence](docs/screenshots/dashboard_intelligence.png)

## 30-Second Summary

The Geopolitical Scenario Intelligence Engine demonstrates a full Research → Analytics → Product workflow:

- Research: validated geopolitical event dataset, source packets, news evidence, and event-study context.
- Analytics: CAR-covered historical event analysis, event-family summaries, deterministic similarity scoring, and historical analog retrieval.
- Product: a dashboard Scenario Intelligence Demo that answers analyst-style questions with historical analogs, evidence, observed pathways, and analyst notes.

The system is designed for evidence-based historical analog and scenario reasoning. It compares user questions against validated geopolitical events and generates analyst-facing briefs.

Example questions:

- What happens if China launches another Joint Sword exercise?
- What happens if new semiconductor export controls are announced?
- What happens after a major Taiwan election?

Boundary: historical analogs only; no return forecasts; no investment advice; no trading recommendations.

## What the Dashboard Shows

The dashboard includes a Scenario Intelligence Demo that displays:

- Scenario Intelligence Demo cards for the three example questions
- top historical analogs from validated events
- deterministic similarity scores
- source-linked evidence base
- observed historical pathways from the coded record
- analyst notes and safe-use boundaries

Key release links:

- [Product Case Study](docs/product_case_study.md)
- [Sprint 2 Prototype Architecture](docs/sprint2_prototype_architecture.md)
- [Historical Analog Retrieval Workflow](docs/historical_analog_retrieval_workflow.md)
- [Dashboard Integration Plan](docs/dashboard_integration_plan_historical_analog_engine.md)
- [Demo Analyst Briefs](results/historical_analog_engine/demo_analyst_briefs.md)
- [Demo Results JSON](results/historical_analog_engine/demo_results.json)

## Reproduce the Demo

From the repository root:

```bash
python3 scripts/historical_analog_engine.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8000/dashboard/
```

## Quick Review Path

For a five-minute portfolio review:

1. Read the 30-second summary above.
2. Open the local dashboard.
3. Review the Scenario Intelligence Demo section.
4. Open [Product Case Study](docs/product_case_study.md).
5. Skim [Demo Analyst Briefs](results/historical_analog_engine/demo_analyst_briefs.md).

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

## Historical Analog Engine

Sprint 2 adds a deterministic Historical Analog Engine prototype. It maps analyst questions to scenario families, retrieves comparable validated historical events, explains similarity scores, attaches source evidence, extracts observed historical pathways, and generates analyst briefs.

Primary assets:

- `scripts/historical_analog_engine.py`
- `results/historical_analog_engine/demo_results.json`
- `results/historical_analog_engine/demo_analyst_briefs.md`
- `results/historical_analog_engine/sample_briefs/`

The engine is a historical analog retrieval and analyst briefing system. It does not forecast returns, generate investment recommendations, or provide trading guidance.

## Scenario Intelligence Demo

Sprint 3 productizes the Historical Analog Engine inside the dashboard as the Scenario Intelligence Demo. The dashboard now presents three portfolio-ready demo questions:

- What happens if China launches another Joint Sword exercise?
- What happens if new semiconductor export controls are announced?
- What happens after a major Taiwan election?

For each question, the dashboard displays scenario classification, top historical analogs, similarity scores, a brief similarity explanation, evidence base, observed historical pathways, and analyst notes. The content is loaded from `results/historical_analog_engine/demo_results.json` and includes fallback instructions if that file is unavailable.

This section is portfolio-safe: historical analogs only, scenario reasoning only, no forecasts, no investment advice, and no trading recommendations.

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
| `results/historical_analog_engine/demo_results.json` | Sprint 3 Scenario Intelligence Demo content |

## Data Layers

The repository now separates source material into clear data layers:

- validated V2 event database: `data/events_v2.csv`
- expanded validated V3 event database: `data/events_v3.csv`
- V3 source packets: `data/source_packets/`
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

## Theory Variable Layer

The repository now includes optional theory variables in `data/events_v2.csv` that operationalize dissertation concepts as structured fields: `interpretation_type`, `state_support_signal`, and `strategic_importance_level`.

These fields translate existing dissertation concepts such as threat, opportunity, adaptation, state support, and strategic importance into reviewable dataset columns. They are interpretive and conservative: blank values are allowed where the existing documentation does not provide enough support. See [Theory Variable Methodology](docs/theory_variable_methodology.md) and `results/theory_variable_coverage.md`.

## Dataset V3 Expansion

The repository now includes `data/events_v3.csv`, an expanded validated event dataset that preserves all 18 V2 events and adds seven net-new validated geopolitical competition events. Three V2 events were also revalidated with source packets rather than duplicated: Pelosi Taiwan Visit, China live-fire exercises around Taiwan, and the October 7 semiconductor export controls.

V3 expands coverage of:

- U.S.-China export-control escalation
- Huawei and SMIC technology restrictions
- semiconductor industrial policy
- strategic investment in semiconductor capacity
- China state-backed semiconductor support

The V3 dataset uses source packets in `data/source_packets/` to document event date, source references, evidence quality, event-family classification, inclusion rationale, and theory relevance. This preserves a clear distinction between validated V2 events, candidate events, and newly integrated V3 events.

V3 theory coding extends the existing interpretive layer with:

- `interpretation_type`
- `strategic_importance_level`
- `state_support_signal`

The V3 validation report is available at `results/events_v3_validation_report.md`. Descriptive V3 summaries are available at `results/event_family_v3_summary.md` and `results/theory_variable_v3_summary.md`. These reports provide counts and coverage only; they do not create CAR values, forecasts, or causal claims.

## Current Event Study Coverage

The validated V3 dataset contains 25 events. The original empirical CAR summary, `results/event_abnormal_return_summary.csv`, covers 18 of those events. The expanded V3 CAR summary, `results/event_abnormal_return_summary_v3.csv`, covers 21 of 25 validated V3 events, or 84%.

The four remaining validated events are not yet included in the CAR layer:

- E019: Huawei Added to U.S. Entity List
- E020: Huawei Foreign-Direct-Product Rule
- E021: SMIC Added to U.S. Entity List
- E022: TSMC Announces $12B Arizona Fab

These events are tracked in `data/car_expansion_candidates.csv`. The remaining 2019-2020 events require historical market-data backfill before CAR calculations can be run. E020 and E022 also share the same event date, so future interpretation will require confounding review. See `docs/v3_car_integration_findings.md`, `results/event_family_v3_car_summary.md`, and `results/theory_variable_v3_car_summary.md`.

## Theory Findings from V3 Dataset

The V3 research integration layer uses `data/events_v3.csv` to connect the expanded validated dataset back to the project's theoretical framework. The current findings are cautious and descriptive.

V3 makes the strategic-importance dimension stronger by adding validated export-control, semiconductor industrial-policy, and strategic-investment events. It also makes the `Mixed` interpretation category more meaningful because export controls can simultaneously create compliance or revenue risk and increase the strategic value of allied semiconductor chokepoints.

The state-support dimension improves but remains selectively coded. This is intentional: many military, diplomatic, legal, and coercive events do not provide direct evidence of public subsidy or state-backed investment. The current V3 CAR coverage also remains incomplete because observed CAR summaries exist for the legacy 18-event analytics layer, not for all newly validated V3 rows.

The main V3 theory reports are:

- `results/theory_variable_analysis.md`
- `results/state_support_analysis.md`
- `results/strategic_importance_analysis.md`
- `results/theory_interaction_analysis.md`
- `results/theory_dataset_coverage.md`
- `docs/theory_findings_memo.md`

## Scenario Similarity Layer

The repository now includes a scenario similarity layer that compares example geopolitical scenarios against historical coded events. It supports historical similarity, context retrieval, and scenario comparison by matching scenario text to event-family coding, actor metadata, geography metadata, linked news evidence, surprise coding, repetition level, and available historical CAR context.

This layer helps users retrieve similar precedents and supporting evidence for analyst review. It does not change the event-study methodology or treat historical market reactions as future-market estimates. Scenario case briefs are available in `docs/scenario_case_briefs.md`.

Generate the scenario similarity outputs with:

```bash
python3 scripts/scenario_similarity.py
```

## Historical Analog Demo Outputs

Regenerate the deterministic Historical Analog Engine demo outputs with:

```bash
python3 scripts/historical_analog_engine.py
```

This writes:

- `results/historical_analog_engine/demo_results.json`
- `results/historical_analog_engine/demo_analyst_briefs.md`
- `results/historical_analog_engine/sample_briefs/`

The dashboard Scenario Intelligence Demo reads the JSON file directly. The generated briefs are analyst-facing Markdown artifacts for review and portfolio documentation.

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
- theory variable coverage
- scenario similarity cards
- Scenario Intelligence Demo cards powered by the Historical Analog Engine
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
python3 scripts/historical_analog_engine.py
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
- [Theory Variable Methodology](docs/theory_variable_methodology.md)
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
