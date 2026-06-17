# Historical Analog Engine Design

## Purpose

The Historical Analog Engine retrieves validated historical events that are similar to a user-defined geopolitical scenario. It is designed to support analyst review by organizing prior events, explaining similarity, and linking evidence.

It does not forecast outcomes, estimate future returns, or produce investment recommendations.

## Design Objectives

- Retrieve relevant historical analogs from validated event records.
- Use deterministic scoring that can be audited and explained.
- Attach evidence and historical context to each analog.
- Preserve clear separation between historical observation and future inference.
- Support future dashboard, API, and report-generation workflows.

## Retrieval Workflow

```text
Scenario Query
      ↓
Feature Normalization
      ↓
Candidate Event Index
      ↓
Deterministic Similarity Score
      ↓
Ranked Historical Analogs
      ↓
Evidence and Context Assembly
      ↓
Analyst-Style Output
```

## Candidate Index

The candidate index should be built from validated historical events. Each indexed event should contain:

- normalized feature object
- original event metadata
- linked news evidence
- source packet path
- available historical CAR context
- validation status

Events with incomplete features can remain in the index but should receive data-quality flags.

## Similarity Scoring Framework

The similarity score should be deterministic and decomposable. The recommended Sprint 1 maximum score is 100.

| Component | Weight | Description |
|---|---:|---|
| Event-family match | 30 | Exact or related taxonomy-family match |
| Actor overlap | 20 | Shared initiating or driving actors |
| Target overlap | 15 | Shared affected actor, geography, sector, or technology |
| Severity proximity | 10 | Distance between severity scores |
| Surprise proximity | 10 | Distance between surprise scores |
| Temporal-context fit | 5 | Recency, repetition level, or sequencing relevance |
| Evidence coverage | 10 | Availability and quality of linked evidence |

### Event-Family Match

Recommended scoring:

| Match type | Points |
|---|---:|
| Exact taxonomy match | 30 |
| Closely related family | 18 |
| Weakly related family | 8 |
| No meaningful relationship | 0 |

Related-family examples:

- Export Control and Technology Restriction
- Diplomatic Shock and Election when the election creates diplomatic signaling
- Sanction and Export Control when both restrict a named target

### Actor Overlap

Recommended scoring:

```text
actor_score = 20 * normalized_actor_overlap
```

Where normalized overlap uses alias-aware matching across query actors and event actors.

Alias examples:

- `PRC`, `China`, `People's Republic of China`
- `United States`, `U.S.`, `US`
- `PLA`, `People's Liberation Army`

### Target Overlap

Recommended scoring:

```text
target_score = 15 * normalized_target_overlap
```

Target matching should recognize sector-level relationships such as:

- `advanced semiconductors` to `global semiconductor supply chain`
- `Taiwan` to `Taiwan Strait`
- named firms to their sector when appropriate

### Severity Proximity

Recommended scoring:

```text
severity_score = 10 * (1 - abs(query_severity - event_severity) / 4)
```

The value should be bounded between 0 and 10.

### Surprise Proximity

Recommended scoring:

```text
surprise_score = 10 * (1 - abs(query_surprise - event_surprise) / 4)
```

The value should be bounded between 0 and 10.

### Temporal-Context Fit

Temporal context should not dominate retrieval in Sprint 1. It should capture whether an event belongs to a relevant repeated sequence or strategic period.

Possible signals:

- same crisis sequence
- repeated event pattern
- post-election or post-visit response
- same technology-policy cycle
- near-term source coverage density

### Evidence Coverage

Evidence coverage rewards events with stronger support material.

Recommended scoring:

| Evidence state | Points |
|---|---:|
| Source packet and linked news evidence available | 10 |
| Linked news evidence available | 7 |
| Source URL available in event record | 5 |
| Minimal event metadata only | 2 |
| Missing source support | 0 |

## Ranking Rules

After calculating total similarity:

1. Sort by total score descending.
2. Break ties by event-family score.
3. Break remaining ties by evidence coverage.
4. Break remaining ties by event date descending.
5. Return top `k` results, with `k = 5` as the recommended default.

Low-scoring results should be flagged:

| Score range | Retrieval confidence |
|---|---|
| 80-100 | Strong analog |
| 60-79 | Useful analog |
| 40-59 | Weak analog requiring analyst review |
| Below 40 | Do not show by default |

## Analyst-Style Output Format

### Historical Analogs

List ranked analogs with:

- event ID
- event name
- event date
- taxonomy family
- total similarity score
- confidence label
- short reason for retrieval

### Similarity Explanation

Report the component breakdown:

| Component | Query value | Historical value | Points | Explanation |
|---|---|---|---:|---|
| Event family | Export Control | Export Control | 30 | Exact match |
| Actor | United States | United States | 20 | Same initiating actor |
| Target | China semiconductors | China semiconductor supply chain | 13 | Strong sector overlap |

The explanation should be mechanical and auditable, not narrative speculation.

### Evidence Base

Attach:

- linked news IDs
- source names
- URLs when available
- source packet path
- event summary
- coding notes

Evidence should be reported as support for historical classification, not as proof of future outcomes.

### Observed Historical Pathways

Describe what happened in the historical record after the analog event using neutral language.

Allowed examples:

- follow-on military activity occurred
- a policy rule was expanded later
- a repeated exercise pattern developed
- linked evidence shows diplomatic response language
- descriptive CAR context is available in the historical results

Disallowed examples:

- expected future market direction
- asset recommendations
- claims that a new scenario will repeat the historical CAR
- unsupported causal claims

### Analyst Notes

Include:

- data-quality caveats
- classification ambiguity
- missing evidence
- difference between query scenario and historical analog
- reminder that output is contextual and non-forecasting

## Example Output Skeleton

```markdown
# Historical Analog Brief: S001

## Historical Analogs

| Rank | Event ID | Event Name | Date | Family | Score | Confidence |
|---:|---|---|---|---|---:|---|
| 1 | E004 | PLA Military Exercises After Pelosi Visit | 2022-08-04 | Military Exercise | 87 | Strong analog |

## Similarity Explanation

The top analog was retrieved because it shares the same event family, overlapping PRC/PLA actors, Taiwan Strait target geography, and similar severity and surprise coding.

## Evidence Base

- Event source: source URL from validated event record
- Linked news evidence: associated evidence rows from `data/news/news_events.csv`
- Source packet: linked source packet when available

## Observed Historical Pathways

The historical case was followed by additional diplomatic and military response coverage in the existing evidence base. Historical CAR context is descriptive only.

## Analyst Notes

This output is for historical context only. It does not forecast future outcomes or provide investment recommendations.
```

## Future Scalability

Sprint 1 should leave room for:

- richer actor ontology
- sector and technology graph matching
- multilingual evidence ingestion
- dashboard filtering by taxonomy family
- analyst feedback on retrieved analog quality
- JSON API output
- LLM-assisted summarization grounded only in retrieved evidence

Forecasting modules, portfolio recommendations, and automated investment advice are outside the product boundary.
