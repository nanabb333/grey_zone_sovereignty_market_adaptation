# Codebook

## Research Question

How does geopolitical risk affect Taiwan financial markets?

## Input Datasets

### `data/events.csv`

| Variable | Type | Description |
| --- | --- | --- |
| `date` | Date | Date of the event. |
| `event_name` | Text | Short name of the event. |
| `event_type` | Text | Event category, such as diplomatic, political, or investment. |
| `risk_level` | Integer | Estimated geopolitical risk score from 1 to 5. |
| `strategic_value` | Integer | Estimated strategic importance score from 1 to 5. |
| `source` | Text | Source note or URL for the event. |

### `data/market.csv`

| Variable | Type | Description |
| --- | --- | --- |
| `date` | Date | Market observation date. |
| `taiex` | Numeric | TAIEX index value. |
| `usd_twd` | Numeric | USD/TWD exchange rate. |
| `tsmc` | Numeric | TSMC stock price. |

### `data/event_scores.csv`

| Variable | Type | Description |
| --- | --- | --- |
| `date` | Date | Date of the scored event. |
| `event_name` | Text | Short name of the event. |
| `risk_level` | Integer | Assigned geopolitical risk score. |
| `strategic_value` | Integer | Assigned strategic-value score. |
| `reasoning` | Text | Short justification for the assigned scores. |

## Independent Variables

### Geopolitical Risk

Definition:
Political or military events related to Taiwan Strait tensions.

Measurement:
Event occurrence and `risk_level`.

Examples:
- PLA exercises
- Pelosi visit
- Election events
- U.S.-Taiwan policy announcements

### Strategic Importance

Definition:
Events highlighting Taiwan's role in global semiconductor and AI supply chains.

Measurement:
Event occurrence and `strategic_value`.

Examples:
- TSMC expansion
- Nvidia investment
- AI factory announcements

## Dependent Variables

| Variable | Measurement |
| --- | --- |
| Market reaction | TAIEX return or percentage change. |
| Exchange rate | USD/TWD change. |
| Strategic investment | Investment announcement count. |
| Semiconductor-sector response | TSMC change. |

## Coding Rules

### `risk_level`

| Value | Label | Meaning |
| ---: | --- | --- |
| 1 | Very Low | Routine event with little geopolitical significance. |
| 2 | Low | Minor political signal with limited market impact. |
| 3 | Medium | Noticeable increase in geopolitical uncertainty. |
| 4 | High | Major escalation in cross-strait tensions. |
| 5 | Very High | Potential crisis or conflict scenario. |

### `strategic_value`

| Value | Label | Meaning |
| ---: | --- | --- |
| 1 | Very Low | Little connection to Taiwan's strategic role. |
| 2 | Low | Limited relevance. |
| 3 | Medium | Moderate relevance to Taiwan's strategic position. |
| 4 | High | Strong relevance to semiconductor, AI, or security issues. |
| 5 | Very High | Directly linked to Taiwan's critical role in global supply chains or U.S.-China competition. |

## Coding Protocol

When assigning `risk_level` or `strategic_value`:

1. Never guess silently.
2. Provide a short justification.
3. If uncertain, flag the event for manual review.
4. Return `event_name`, `risk_level`, `strategic_value`, and `reasoning`.

## Output Datasets

### `output/event_summary.csv`

| Variable | Description |
| --- | --- |
| `date` | Event date. |
| `event_name` | Event name. |
| `event_type` | Event category. |
| `risk_level` | Geopolitical risk score. |
| `strategic_value` | Strategic-value score. |
| `taiex` | TAIEX value on the event date. |
| `usd_twd` | USD/TWD value on the event date. |
| `tsmc` | TSMC value on the event date. |

### `output/event_impact.csv`

| Variable | Description |
| --- | --- |
| `event_name` | Event name. |
| `event_type` | Event category. |
| `risk_level` | Geopolitical risk score. |
| `strategic_value` | Strategic-value score. |
| `taiex_before` | TAIEX value one day before the event. |
| `taiex_event_day` | TAIEX value on the event date. |
| `taiex_after` | TAIEX value one day after the event. |
| `taiex_change` | Percentage change in TAIEX from before to after. |
| `usd_twd_before` | USD/TWD value one day before the event. |
| `usd_twd_event_day` | USD/TWD value on the event date. |
| `usd_twd_after` | USD/TWD value one day after the event. |
| `usd_twd_change` | Percentage change in USD/TWD from before to after. |
| `tsmc_before` | TSMC value one day before the event. |
| `tsmc_event_day` | TSMC value on the event date. |
| `tsmc_after` | TSMC value one day after the event. |
| `tsmc_change` | Percentage change in TSMC from before to after. |

