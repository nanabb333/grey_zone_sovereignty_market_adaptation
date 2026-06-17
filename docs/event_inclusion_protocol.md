# Event Inclusion Protocol

> Academic Research Notice:
> This protocol governs candidate review before events are added to a validated event-study dataset. It does not itself validate or insert any event.

## Inclusion Criteria

An event may be included in a validated dataset only when all criteria below are satisfied:

1. The event is a real historical event with a documented date.
2. The event has a public source that identifies the relevant actors and action.
3. The event is relevant to at least one project mechanism:
   - Taiwan security risk
   - U.S.-China strategic competition
   - semiconductor policy
   - export controls
   - state support or industrial policy
   - strategic investment
   - supply-chain security
   - diplomatic-recognition competition
4. The event has a plausible investor-interpretation channel for Taiwan, semiconductor, technology, defense, or supply-chain assets.
5. The event date can be mapped to a market trading date.
6. The event is not already represented by an existing validated event unless it captures a separate action, actor, or information release.
7. The event window is not dominated by an unrelated same-day shock that makes interpretation unusable.

## Exclusion Criteria

Exclude or defer events when any condition below applies:

- The event is rumored, forecasted, speculative, or not historically confirmed.
- The date is ambiguous and cannot be reconciled to a clear public announcement or implementation point.
- The event duplicates an existing validated event.
- The event is too broad, gradual, or cumulative to assign a defensible event date.
- The event has weak relevance to Taiwan, semiconductors, strategic technology, supply-chain security, or diplomatic competition.
- The event is primarily a dashboard, product, or internal-project milestone rather than a geopolitical or policy event.
- The event window is heavily confounded by a larger unrelated market-moving event.

## Coding Standards

Candidate records should use stable, reviewable fields:

| Field | Standard |
| --- | --- |
| `candidate_id` | Use `CAND-V3-###` for candidate records before validation. |
| `date` | Use ISO format: `YYYY-MM-DD`. |
| `title` | Use a concise event title that identifies the action. |
| `category` | Use a project-relevant category, not a vague geography label. |
| `actors` | List primary public actors separated by semicolons. |
| `rationale` | State why the event is substantively relevant. |
| `inclusion_status` | Use only `Include`, `Review Further`, or `Exclude`. |
| `notes` | Record duplication, source, confounding, or trading-calendar issues. |

Validated event records should additionally include:

- event ID
- market trading date
- days to trading date
- event window start and end
- source URL or citation
- mechanism
- event family
- surprise score
- surprise rationale
- interpretation type
- state-support signal where supported
- strategic-importance level where supported

## Evidence Requirements

Before a candidate becomes a validated event, the reviewer should collect at least two evidence layers:

1. A primary or official source where available, such as a government release, company announcement, legislation, regulator notice, or official military statement.
2. A contemporaneous reputable news source or specialist analysis showing public market-relevant disclosure.

For each event, reviewers should record:

- source title
- source publisher
- publication date
- event date
- whether the source appeared before market open, during trading, after market close, or on a non-trading day when that information is available
- any known same-day confounding events

## Trading-Date Rules

- If an event occurs on a trading day before or during market hours, use the same date as the event trading date.
- If an event occurs after market close, on a weekend, or on a market holiday, map to the next open trading date.
- Record the number of calendar days between the historical event date and the trading date.
- Do not silently change historical dates; keep both event date and event trading date.

## Review Workflow

1. Enter discovered events into `data/event_candidates_v3.csv`.
2. Assign preliminary status: `Include`, `Review Further`, or `Exclude`.
3. Resolve source quality, duplicate coverage, and trading-calendar issues.
4. Move only validated events into the master event dataset in a separate sprint.
5. Update the coding log and readiness report after validation.
