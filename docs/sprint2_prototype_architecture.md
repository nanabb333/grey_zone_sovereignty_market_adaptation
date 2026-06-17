# Sprint 2 Prototype Architecture: Historical Analog Engine

## Purpose

Sprint 2 turns the Historical Analog Engine design into a working deterministic prototype. The prototype maps analyst questions to scenario features, retrieves comparable historical events, assembles evidence, extracts observed pathways, and renders analyst briefs.

The prototype is not a forecasting system and is not an investment recommendation system.

## Prototype Components

```text
Analyst Question
      ↓
Question-to-Scenario Mapper
      ↓
Feature Normalizer
      ↓
Historical Event Candidate Index
      ↓
Deterministic Similarity Scorer
      ↓
Historical Analog Retriever
      ↓
Evidence and Pathway Assembler
      ↓
Analyst Brief Generator
```

## Implementation Artifact

Primary script:

```text
scripts/historical_analog_engine.py
```

Primary outputs:

```text
results/historical_analog_engine/demo_results.json
results/historical_analog_engine/demo_analyst_briefs.md
results/historical_analog_engine/sample_briefs/
```

## Data Inputs

| Input | Use |
|---|---|
| `data/events_v3.csv` | Validated historical event candidate index |
| `data/news/news_events.csv` | Linked evidence base |
| `results/event_abnormal_return_summary_v3.csv` | Historical descriptive CAR context |
| `docs/scenario_taxonomy.md` | Taxonomy design reference |
| `docs/event_feature_schema.md` | Feature contract design reference |

## Question-to-Scenario Mapping

The mapper uses deterministic keyword rules. It maps analyst questions into structured scenario objects containing:

- scenario ID
- scenario title
- event family
- actor set
- target set
- severity score
- surprise score
- query terms
- mapping rationale

Sprint 2 supports the required demo cases:

| Question Pattern | Scenario Family |
|---|---|
| Joint Sword, military exercise, drills, blockade | Military Exercise |
| semiconductor export controls, chip controls, entity list | Export Control |
| election, inauguration, vote, presidential | Election |

## Similarity Scoring

The prototype follows the Sprint 1 deterministic framework with a 100-point nominal score:

| Component | Max Points |
|---|---:|
| Event-family match | 30 |
| Actor overlap | 20 |
| Target overlap | 15 |
| Severity proximity | 10 |
| Surprise proximity | 10 |
| Temporal-context fit | 5 |
| Evidence coverage | 10 |

The score is decomposed in every analyst brief so the analyst can inspect why a historical event was retrieved.

## Historical Pathway Extraction

Pathways are extracted from coded historical records using deterministic rules:

- later same-family events in the dataset
- near-term subsequent coded events in the same calendar year
- repetition-level coding
- availability of historical CAR context

Pathway language is descriptive. It does not state or imply that a future event will follow the same path.

## Analyst Brief Contract

Each generated brief contains:

- Question
- Historical Analogs
- Similarity Explanation
- Evidence Base
- Observed Historical Pathways
- Analyst Notes

The same structure is suitable for dashboard panels, Markdown reports, and future API responses.

## Governance Boundary

Every generated output includes this constraint:

```text
Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.
```
