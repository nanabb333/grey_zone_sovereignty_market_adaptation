# Event Family Analytics Methodology

## Purpose

Event-family analytics adds a descriptive bridge between the geopolitical event database, the curated news evidence layer, and available market-reaction outputs. It helps analysts compare how different categories of Taiwan-related events appear in the dataset without changing the original event-study design, event windows, abnormal-return calculations, or research claims.

The layer is intended for evidence organization and analyst review. It is not a forecasting tool, investment model, or automated causal inference module.

## Event-Family Grouping

Events are grouped using the `event_family` field in `data/events_v2.csv`. This keeps the analysis anchored to the existing curated event database rather than introducing a new classification scheme.

Examples of event families include:

- `Diplomatic_Shock`
- `Military_Exercise`
- `Strategic_Investment`
- `Export_Control`
- `Economic_Coercion`
- `Political_Signaling`
- `Legal_Judicial_Signaling`

The summary script counts the number of events in each family and, where market-reaction outputs are available, calculates simple descriptive CAR statistics for matched events.

## Linking News Evidence To Market Reaction Data

The script reads `data/news/news_events.csv` and links news items to event families through `related_event_id`, dated event labels, and conservative single-event date matches. This allows structured source evidence to be summarized alongside event-family counts.

Market reaction data are read from `results/event_abnormal_return_summary.csv` when available. Because that file is keyed by event name and event date, the script matches it back to `data/events_v2.csv` using normalized event names and dates. The preferred CAR metric is selected from available columns, with `tsmc_car_7` used first when present.

This creates a descriptive view of how many events, news items, and CAR observations are available for each event family.

## Descriptive, Not Causal

The event-family summary reports counts, averages, medians, ranges, and positive or negative CAR counts. These are descriptive statistics only. They do not establish that an event family caused a market move, that similar events will produce similar reactions, or that the observed pattern should guide investment decisions.

Any interpretation should be framed as an analyst-reviewed description of the current curated dataset.

## Limitations

The dataset is curated and not exhaustive. News rows include placeholder-safe starter entries that require verification against exact source URLs before publication or formal research use.

Event-family labels reflect the current coding scheme and may require review as the dataset expands. Market reactions depend on the existing event-study outputs and should be interpreted within the original methodology's scope and limitations.

This layer does not provide forecasting, trading recommendations, investment advice, policy advice, or unsupported causal claims. Analyst review is required before using the outputs in public-facing research, dashboard narratives, or decision-support materials.
