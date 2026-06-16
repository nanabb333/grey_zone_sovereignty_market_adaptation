# Scenario Similarity Methodology

## Purpose

The scenario similarity layer compares example geopolitical scenarios with historical coded events in the repository. It is designed for historical similarity analysis, context retrieval, and scenario comparison.

The layer helps analysts identify prior events that share similar language, event-family coding, actors, geography, and linked news evidence. It does not change the event-study methodology, event coding, or prior empirical results.

## Rule-Based Similarity Scoring

`scripts/scenario_similarity.py` uses transparent scoring rules. Each example scenario is compared with every event in `data/events_v2.csv`.

The score combines:

- keyword overlap between the scenario text and event descriptions
- event-family match using the existing `event_family` field
- actor match from linked news evidence in `data/news/news_events.csv`
- geography match from linked news evidence
- linked news evidence count
- optional surprise-score and repetition-level signals when present in the event database

The nominal maximum score is 108. The script returns the top three historical events for each example scenario. The score is a retrieval aid, not a measure of event severity or future market impact.

## Context Retrieval Boundary

This layer retrieves similar historical cases for analyst review. It should be used to ask: "Which coded events in the repository look most similar to this scenario under transparent rules?"

It should not be used to infer that a new scenario will produce the same market reaction as a historical event. Similarity in event description, actor, geography, or event family does not establish causality or future outcomes.

## Historical CAR Interpretation

Historical CAR patterns can provide context about how coded events were summarized in the existing event-study outputs. They should be interpreted only within the original research design and data limitations.

CAR values should not be mechanically transferred from a historical event to a new scenario. A similar event family or keyword profile is not enough to support a market-outcome claim.

When available, the script displays `tsmc_car_7` as a historical descriptive market-reaction metric. This label is included to keep the boundary explicit: the value describes a past coded event and is not an estimate for any user-provided scenario.

## Limitations

The scenario examples are embedded in the script for reproducible demonstration. They are not a complete scenario library.

The scoring logic is intentionally simple and auditable. It does not understand nuance beyond the coded fields, keyword overlap, and linked news metadata. News evidence rows may include placeholder-safe source metadata that requires verification before public use.

Analyst review is required before using the outputs in research, dashboard narratives, or decision-support materials.
