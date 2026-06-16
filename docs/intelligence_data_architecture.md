# Intelligence Data Architecture

The project is organized as a layered intelligence prototype. Each layer adds structure or presentation while preserving the original event-study design and avoiding forecasting or investment advice.

```text
Research Layer
  ↓
Evidence Layer
  ↓
Analytics Layer
  ↓
Scenario Layer
  ↓
Dashboard Layer
```

## Research Layer

Primary files:

- `data/events_v2.csv`
- `results/event_abnormal_return_summary.csv`
- existing event-window outputs, reports, and figures

This layer contains the curated geopolitical event database and historical market-reaction outputs. The `event_id` field provides stable traceability across downstream layers.

## Evidence Layer

Primary files:

- `data/news/news_events.csv`
- `results/news_database_summary.json`
- `results/news_database_summary.md`

This layer adds curated news evidence linked to `event_id` where possible. It supports source traceability and analyst review but does not replace the original research design.

## Analytics Layer

Primary files:

- `scripts/analyze_event_family_patterns.py`
- `results/event_family_summary.csv`
- `results/event_family_summary.json`
- `results/event_family_summary.md`

This layer groups historical events by `event_family` and summarizes descriptive counts and historical CAR context where available.

## Scenario Layer

Primary files:

- `scripts/scenario_similarity.py`
- `results/scenario_similarity_results.json`
- `results/scenario_similarity_results.md`
- `docs/scenario_case_briefs.md`

This layer compares example scenarios against historical coded events using transparent rule-based similarity. It is context retrieval, not prediction.

## Dashboard Layer

Primary files:

- `dashboard/index.html`
- `dashboard/app.js`
- `dashboard/styles.css`

The dashboard reads static outputs from `results/` and presents the intelligence prototype for analyst review. It requires no API key, LLM call, or internet access.

## Validation Flow

Primary files:

- `scripts/validate_project_data.py`
- `results/data_validation_report.json`
- `results/data_validation_report.md`

Validation checks event IDs, news IDs, required fields, event-family values, and news-to-event linkage. The dashboard metadata panel uses the validation report to expose basic project integrity status.
