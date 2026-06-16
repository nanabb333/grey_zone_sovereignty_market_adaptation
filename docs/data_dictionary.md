# Data Dictionary

This dictionary documents the core datasets and generated outputs used by the geopolitical intelligence prototype. Fields are descriptive and support analyst review; they do not introduce new analytical claims.

## Events Dataset

File: `data/events_v2.csv`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `event_id` | string | Persistent event identifier using `E###` format | `E002` |
| `date` | date | Calendar date of the geopolitical event | `2022-08-02` |
| `event_name` | string | Short event label | `Pelosi Visit` |
| `event_category` | string | Broad descriptive category | `Diplomatic Shock` |
| `mechanism` | string | Existing research mechanism label | `Risk` |
| `event_trading_date` | date | Trading date used by the event-study workflow | `2022-08-02` |
| `days_to_trading_date` | integer | Calendar-day offset between event date and trading date | `0` |
| `window_start` | date | Event-window start date | `2022-07-22` |
| `window_end` | date | Event-window end date | `2022-08-11` |
| `brief_description` | string | Cautious factual description | `U.S. House Speaker Nancy Pelosi visited Taiwan amid PRC warnings` |
| `source` | URL/string | Source used for event coding | `https://...` |
| `surprise_score` | categorical | Low/Medium/High expectedness coding | `High` |
| `surprise_rationale` | string | Rationale for surprise coding | `The visit was discussed in advance...` |
| `event_family` | categorical | Comparable event-family group | `Diplomatic_Shock` |
| `event_repetition_level` | integer | Repetition indicator within comparable event family | `1` |

## News Evidence Dataset

File: `data/news/news_events.csv`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `news_id` | string | Persistent news-evidence identifier | `N001` |
| `date` | date | Publication or event-related date | `2022-08-02` |
| `source` | string | Source label; placeholders require verification | `Reuters placeholder` |
| `title` | string | News or source-document title | `Pelosi arrives in Taiwan amid heightened cross-strait warnings` |
| `url` | URL/string | Source URL or placeholder source homepage | `https://www.reuters.com/` |
| `related_event_id` | string | Linked `event_id` from `data/events_v2.csv`, or explicit unlinked placeholder | `E002` |
| `event_family` | string | Evidence-level category | `Diplomatic Shock` |
| `actor` | string | Actors named or relevant to the evidence row | `United States; Taiwan; PRC` |
| `geography` | string | Relevant geography | `Taiwan Strait` |
| `summary` | string | Cautious evidence summary | `Placeholder entry representing reporting...` |
| `relevance_score` | float | Manual relevance score from 0 to 1 | `0.95` |
| `coding_notes` | string | Analyst-review notes and verification cautions | `Verify exact article metadata...` |

## Analytics Outputs

### News Database Summary

Files: `results/news_database_summary.json`, `results/news_database_summary.md`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `news_item_count` | integer | Number of news evidence rows | `12` |
| `count_by_event_family` | object | News count by evidence family | `{"Military Demonstration": 5}` |
| `count_by_actor` | object | News count by actor field | `{"PRC": 5}` |
| `count_by_geography` | object | News count by geography field | `{"Taiwan Strait": 6}` |
| `average_relevance_score` | float | Mean relevance score | `0.869` |
| `use_limits` | list | Responsible-use boundaries | `Curated dataset, not exhaustive.` |

### Event Family Summary

Files: `results/event_family_summary.csv`, `results/event_family_summary.json`, `results/event_family_summary.md`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `event_family` | string | Event family from `data/events_v2.csv` | `Military_Exercise` |
| `event_count` | integer | Number of events in the family | `8` |
| `linked_news_count` | integer | Number of linked news items | `5` |
| `car_observation_count` | integer | Number of historical CAR values available | `8` |
| `car_metric` | string | Historical CAR metric used | `tsmc_car_7` |
| `average_car` | float/string | Average historical CAR if available | `-0.2862` |
| `median_car` | float/string | Median historical CAR if available | `-0.7499` |
| `min_car` | float/string | Minimum historical CAR if available | `-4.4508` |
| `max_car` | float/string | Maximum historical CAR if available | `5.3488` |
| `positive_car_count` | integer | Count of positive historical CAR values | `2` |
| `negative_car_count` | integer | Count of negative historical CAR values | `6` |
| `interpretation_note` | string | Descriptive-use limitation | `Descriptive event-family summary...` |

## Scenario Outputs

Files: `results/scenario_similarity_results.json`, `results/scenario_similarity_results.md`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `scenario_id` | string | Example scenario identifier | `S001` |
| `scenario_text` | string | Scenario input text | `large-scale military exercises near Taiwan` |
| `scenario_event_family` | string | Expected event-family context for scoring | `Military_Exercise` |
| `top_matches` | list | Top three historically similar coded events | `[ ... ]` |
| `event_id` | string | Matched historical event ID | `E007` |
| `event_date` | date | Matched historical event date | `2023-04-08` |
| `event_family` | string | Matched event family | `Military_Exercise` |
| `similarity_score` | integer | Rule-based retrieval score | `73` |
| `matched_terms` | list | Keyword overlap terms | `["exercises", "military"]` |
| `linked_news_count` | integer | Count of linked news evidence rows | `1` |
| `historical_market_reaction` | object/null | Historical descriptive CAR context when available | `{"metric": "tsmc_car_7", "value": -1.0286}` |
| `caution_label` | string | Responsible-use warning | `Historical similarity is not a forecast or investment signal.` |

## Validation Outputs

Files: `results/data_validation_report.json`, `results/data_validation_report.md`

| Field | Type | Meaning | Example |
|---|---|---|---|
| `status` | string | Overall status: `pass`, `warning`, or `fail` | `warning` |
| `summary.event_count` | integer | Number of coded events | `18` |
| `summary.news_item_count` | integer | Number of news rows | `12` |
| `summary.event_family_count` | integer | Number of event families | `7` |
| `errors` | list | Blocking validation issues | `[]` |
| `warnings` | list | Non-blocking review issues | `orphan_news_records` |
