# Sprint 1 Architecture: Historical Analog Engine

## Purpose

The Historical Analog Engine is the first product layer of the Geopolitical Scenario Intelligence Engine. Its role is to retrieve historically similar geopolitical events from the existing validated event database and present them in an analyst-ready format.

Sprint 1 is limited to historical analog retrieval, explanation, and evidence organization. It does not forecast future market behavior, estimate future returns, or generate investment recommendations.

## Product Boundary

The engine answers:

- Which validated historical events are most similar to a scenario?
- Why were those events retrieved?
- What evidence supports each historical analog?
- What historical pathways were observed after similar coded events?
- What caveats should an analyst keep in view?

The engine does not answer:

- What will happen next?
- Which asset should be bought, sold, or hedged?
- What return should be expected from a future event?
- Which policy response is optimal?

## System Layers

```text
Validated Event Repository
        ↓
Event Feature Layer
        ↓
Taxonomy Normalization Layer
        ↓
Similarity Scoring Layer
        ↓
Analog Retrieval Layer
        ↓
Evidence Assembly Layer
        ↓
Analyst Output Layer
```

## Source Systems

The Sprint 1 design should reuse the repository's existing assets:

| Source | Role |
|---|---|
| `data/events_v3.csv` | Primary validated event record |
| `data/news/news_events.csv` | Linked source evidence and metadata |
| `results/event_abnormal_return_summary_v3.csv` | Historical descriptive CAR context |
| `results/scenario_similarity_results.*` | Current prototype similarity outputs |
| `data/source_packets/` | Event-level source packets for analyst review |

The event database remains the source of truth for event metadata. CAR files are contextual historical observations only.

## Core Components

### 1. Event Feature Layer

Converts validated events into a consistent retrieval feature set:

- `event_id`
- `event_family`
- `actor`
- `target`
- `severity_score`
- `surprise_score`
- `event_date`

The feature layer should preserve the original event record and expose derived fields separately. Derived scores should be auditable and reproducible.

### 2. Taxonomy Normalization Layer

Maps existing event-family labels into the Sprint 1 scenario taxonomy:

- Military Exercise
- Diplomatic Shock
- Export Control
- Sanction
- Election
- Strategic Investment
- Technology Restriction

This layer should support many-to-one and alias mappings because the existing repository contains adjacent labels such as `Economic_Coercion`, `Political_Signaling`, and `Legal_Judicial_Signaling`.

### 3. Similarity Scoring Layer

Calculates deterministic similarity between a query scenario and each historical event. The score should be transparent, decomposable, and stable across runs.

The score should combine:

- event-family match
- actor overlap
- target overlap
- severity proximity
- surprise proximity
- temporal context
- evidence coverage

Each component should be reported in the output so analysts can see why a case was retrieved.

### 4. Analog Retrieval Layer

Ranks historical events by similarity score and returns a bounded set of analogs.

Recommended Sprint 1 default:

- return top 3 to top 5 analogs
- require minimum evidence coverage for production-facing output
- flag low-confidence matches rather than hiding them
- preserve score components for auditability

### 5. Evidence Assembly Layer

Attaches support material to each retrieved analog:

- linked news evidence
- source packet path when available
- event metadata
- historical CAR context when available
- coding notes and surprise rationale

Evidence should be clearly labeled as historical context, not predictive support.

### 6. Analyst Output Layer

Generates a structured analyst note with the following sections:

- Historical Analogs
- Similarity Explanation
- Evidence Base
- Observed Historical Pathways
- Analyst Notes

The output should be usable in a dashboard, Markdown report, or future API response.

## Data Contracts

### Scenario Query Contract

Recommended input fields:

| Field | Type | Required | Purpose |
|---|---|---|---|
| `scenario_id` | string | Yes | Stable query identifier |
| `scenario_title` | string | Yes | Analyst-readable scenario label |
| `event_family` | string | Yes | Scenario taxonomy label |
| `actor` | string or list | Yes | Initiating state, institution, firm, or group |
| `target` | string or list | Yes | Affected state, sector, firm, or geography |
| `severity_score` | number | Yes | Coded intensity level |
| `surprise_score` | number | Yes | Coded information shock level |
| `event_date` | date | Optional | Known or assumed event date |
| `scenario_description` | string | Optional | Free-text context for analyst review |

### Analog Result Contract

Recommended output fields:

| Field | Purpose |
|---|---|
| `query_scenario_id` | Links result to input scenario |
| `analog_event_id` | Historical event identifier |
| `analog_event_name` | Historical event label |
| `event_family` | Normalized taxonomy family |
| `similarity_score` | Total deterministic score |
| `score_components` | Component-level score breakdown |
| `evidence_items` | Linked source evidence |
| `historical_context` | Descriptive CAR and pathway fields |
| `analyst_caveats` | Limitations and review notes |

## Scalability Principles

- Keep retrieval deterministic before adding AI-assisted summarization.
- Store feature extraction rules separately from event records.
- Preserve backward compatibility with existing event IDs.
- Use normalized taxonomy labels but retain original source labels.
- Treat source evidence quality as a first-class retrieval signal.
- Make every score explainable at the component level.
- Design outputs for both Markdown reports and machine-readable JSON.

## Governance Guardrails

Every Sprint 1 output should include a boundary statement:

```text
This historical analog output is for contextual analysis only. It does not forecast future outcomes, estimate future market returns, or provide investment recommendations.
```

Analyst review is required before external publication or decision-support use.
