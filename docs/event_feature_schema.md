# Event Feature Schema

## Purpose

The event feature schema defines the minimum structured fields required for Historical Analog Engine retrieval. It standardizes the fields used to compare a query scenario with validated historical events.

The schema is intentionally compact for Sprint 1. Additional fields can be added later without changing the core retrieval contract.

## Required Feature Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `event_id` | string | Yes | Stable unique identifier for the historical event or scenario query |
| `event_family` | enum | Yes | Normalized scenario taxonomy family |
| `actor` | string or list | Yes | Actor initiating, announcing, or driving the event |
| `target` | string or list | Yes | Actor, sector, geography, or institution primarily affected |
| `severity_score` | number | Yes | Deterministic intensity score |
| `surprise_score` | number | Yes | Deterministic information-shock score |
| `event_date` | date | Yes | Date of the event in `YYYY-MM-DD` format |

## Field Definitions

### `event_id`

Stable event identifier used to connect metadata, evidence, CAR context, and analyst outputs.

Rules:

- historical events should preserve repository IDs such as `E001`
- query scenarios should use scenario IDs such as `S001`
- generated identifiers should not overwrite validated event IDs

### `event_family`

Normalized taxonomy label used for first-pass retrieval.

Allowed Sprint 1 values:

- `Military Exercise`
- `Diplomatic Shock`
- `Export Control`
- `Sanction`
- `Election`
- `Strategic Investment`
- `Technology Restriction`

The original repository field should be preserved separately when it differs from the normalized value.

### `actor`

The initiating or primary driving actor.

Examples:

- `PRC`
- `United States`
- `Taiwan`
- `TSMC`
- `U.S. Commerce Department`
- `PLA`

Rules:

- store as a list when multiple actors are material
- normalize common aliases such as `PRC`, `China`, and `People's Republic of China`
- preserve original source wording in the evidence layer

### `target`

The affected actor, sector, geography, or object of pressure.

Examples:

- `Taiwan`
- `China`
- `Global semiconductor supply chain`
- `Advanced semiconductor equipment`
- `Huawei`
- `TSMC`

Rules:

- use specific targets when available
- allow sector-level targets when the event affects a broad domain
- separate target from geography when later schema versions add a geography field

### `severity_score`

Deterministic score representing event intensity.

Recommended Sprint 1 scale:

| Score | Meaning |
|---|---|
| 1 | Low salience or routine signal |
| 2 | Moderate event with limited escalation |
| 3 | Material event with clear geopolitical relevance |
| 4 | High-intensity event with broad policy, military, or supply-chain relevance |
| 5 | Exceptional escalation or systemically important event |

Severity should be based on event features, not observed market reaction.

Recommended severity inputs:

- operational scale
- policy scope
- affected sector importance
- number of affected actors
- formal legal or military status
- geographic proximity to Taiwan or semiconductor supply chains

### `surprise_score`

Deterministic score representing how much new information the event introduced relative to what was already visible.

Recommended Sprint 1 scale:

| Score | Meaning |
|---|---|
| 1 | Expected, scheduled, or highly repeated |
| 2 | Somewhat expected with minor new information |
| 3 | Meaningful new details or timing uncertainty |
| 4 | High surprise in timing, scope, or actor behavior |
| 5 | Exceptional information shock |

Existing repository values such as `Low`, `Medium`, and `High` can be mapped as:

| Existing value | Numeric score |
|---|---|
| `Low` | 1 |
| `Medium` | 3 |
| `High` | 5 |

### `event_date`

Primary date of the event.

Rules:

- use announcement date for policy and investment events
- use start date for exercises or multi-day actions
- use election date for election outcomes
- use publication or effective date consistently for legal restrictions
- store dates as `YYYY-MM-DD`

## Recommended Extended Fields

The following fields are not required for Sprint 1 but should be supported by the architecture:

| Field | Purpose |
|---|---|
| `event_name` | Analyst-readable label |
| `event_description` | Short summary for text overlap and reporting |
| `geography` | Location or affected region |
| `mechanism` | Existing research mechanism such as `Risk` or `Strategic_Importance` |
| `event_repetition_level` | Repetition or adaptation signal |
| `interpretation_type` | Threat, opportunity, mixed, or adaptation label |
| `source_packet` | Path to curated source packet |
| `evidence_count` | Number of linked evidence items |
| `historical_car_context` | Descriptive historical CAR metrics when available |

## Example Feature Object

```json
{
  "event_id": "E005",
  "event_family": "Export Control",
  "actor": ["United States", "U.S. Commerce Department"],
  "target": ["China", "Advanced semiconductor supply chain"],
  "severity_score": 4,
  "surprise_score": 3,
  "event_date": "2022-10-07"
}
```

## Validation Rules

Sprint 1 feature records should pass these checks:

- `event_id` is present and unique within the retrieval index
- `event_family` matches the scenario taxonomy
- `actor` is non-empty
- `target` is non-empty
- `severity_score` is numeric and between 1 and 5
- `surprise_score` is numeric and between 1 and 5
- `event_date` is a valid ISO date
- derived fields do not overwrite original event metadata

## Versioning

The schema should be versioned as `event_feature_schema_v1`.

Future versions may add:

- geography normalization
- actor role typing
- target sector ontology
- source credibility score
- event duration
- escalation pathway labels
- multilingual source support
