# Analyst Brief Templates

## Markdown Template

```markdown
# Analyst Brief: {scenario_title}

## Question

{question}

Mapped scenario family: `{event_family}`

Mapping rationale: {mapping_reason}

## Historical Analogs

| Rank | Event ID | Historical Event | Date | Family | Score | Confidence |
|---:|---|---|---|---|---:|---|
| 1 | {event_id} | {event_name} | {event_date} | {event_family} | {similarity_score} | {confidence} |

## Similarity Explanation

### 1. {event_id} - {event_name}

| Component | Query Value | Historical Value | Points | Explanation |
|---|---|---|---:|---|
| Event Family Match | {query_family} | {historical_family} | {points} | {explanation} |
| Actor Overlap | {query_actors} | {historical_actors} | {points} | {explanation} |
| Target Overlap | {query_targets} | {historical_targets} | {points} | {explanation} |
| Severity Proximity | {query_severity} | {historical_severity} | {points} | {explanation} |
| Surprise Proximity | {query_surprise} | {historical_surprise} | {points} | {explanation} |
| Temporal Context Fit | {query_terms} | {historical_context} | {points} | {explanation} |
| Evidence Coverage | evidence coverage | {evidence_count} | {points} | {explanation} |

## Evidence Base

### {event_id} - {event_name}

- Event source: {source}
- Source packet: `{source_packet}`
- Surprise rationale: {surprise_rationale}
- Linked evidence: {news_id}, {source}, {title}, {url}
- Historical CAR context: {car_metrics}. Historical context only.

## Observed Historical Pathways

### {event_id} - {event_name}

- {pathway_summary}

## Analyst Notes

- Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations.
- Similarity scores are deterministic retrieval aids and require analyst review.
- Evidence rows may contain placeholder source metadata that should be verified before publication.
- Historical CAR fields, when shown, describe prior coded events and are not estimates for the question scenario.
```

## JSON Shape

```json
{
  "question": "What happens if China launches another Joint Sword exercise?",
  "mapped_scenario": {
    "scenario_id": "S2-DEMO-001",
    "title": "Renewed Joint Sword-Style Military Exercise",
    "event_family": "Military Exercise",
    "actors": ["PRC", "PLA", "China"],
    "targets": ["Taiwan", "Taiwan Strait"],
    "severity_score": 4,
    "surprise_score": 3,
    "mapping_reason": "Deterministic rule explanation"
  },
  "historical_analogs": [
    {
      "event_id": "E013",
      "event_name": "Joint Sword-2024A",
      "event_date": "2024-05-23",
      "event_family": "Military Exercise",
      "similarity_score": 87.0,
      "confidence": "Strong analog",
      "score_components": {},
      "evidence_items": [],
      "observed_historical_pathways": []
    }
  ],
  "analyst_notes": [
    "Historical analog retrieval only. This output does not forecast future outcomes, estimate future returns, or provide investment recommendations."
  ]
}
```

## Dashboard Panel Mapping

| Brief Section | Dashboard Component |
|---|---|
| Question | Scenario header |
| Historical Analogs | Ranked analog table |
| Similarity Explanation | Score breakdown accordion |
| Evidence Base | Evidence drawer |
| Observed Historical Pathways | Pathway timeline panel |
| Analyst Notes | Guardrail and caveat panel |
