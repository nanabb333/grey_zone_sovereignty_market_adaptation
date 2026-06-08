# Codebook V2

## Purpose

This codebook documents the v2 event dataset for the project:

Taiwan's Grey-Zone Sovereignty: Why Strategic Ambiguity Generates Both Geopolitical Risk and Economic Opportunity.

The v2 dataset adds investor-interpretation variables to help explain why high geopolitical risk does not always produce negative market reactions.

## Dataset

File:

`data/events_v2.csv`

## Variables

| Variable | Type | Scale / Format | Definition |
| --- | --- | --- | --- |
| `date` | Date | `YYYY-MM-DD` | Event date. |
| `event_name` | Text | Name | Short event name. |
| `event_category` | Text | Category | Event type, such as diplomatic or military. |
| `military_risk` | Integer | 1-5 | Degree of military escalation or coercive military pressure. |
| `diplomatic_risk` | Integer | 1-5 | Degree of diplomatic tension or political signaling. |
| `sanctions_risk` | Integer | 1-5 | Degree of sanctions, export-control, or financial-statecraft relevance. |
| `semiconductor_relevance` | Integer | 1-5 | Degree to which the event connects to Taiwan's semiconductor role. |
| `ai_relevance` | Integer | 1-5 | Degree to which the event connects to AI infrastructure, AI chips, or AI investment. |
| `security_relevance` | Integer | 1-5 | Degree to which the event matters for Taiwan security or U.S.-China competition. |
| `surprise_level` | Integer | 1-5 | Degree to which investors likely did not anticipate the event before it occurred. |
| `event_repetition` | Integer | 1-5 | Degree to which similar geopolitical events had already occurred previously. |
| `confidence_level` | Text | TBD / Low / Medium / High | Confidence in the coding. |
| `source` | Text | URL or citation | Source supporting the event and coding. |

## New Explanatory Variables

### `surprise_level`

Definition:
Degree to which investors likely anticipated the event before it occurred.

Scale:

| Score | Meaning |
| ---: | --- |
| 1 | Very low surprise; event was highly anticipated. |
| 2 | Low surprise; event was partly anticipated. |
| 3 | Medium surprise. |
| 4 | High surprise. |
| 5 | Very high surprise; event was largely unexpected. |

### `event_repetition`

Definition:
Degree to which similar geopolitical events had already occurred previously.

Scale:

| Score | Meaning |
| ---: | --- |
| 1 | Very low repetition; event type was relatively novel. |
| 2 | Low repetition; a few similar events had occurred. |
| 3 | Medium repetition; similar events were becoming familiar. |
| 4 | High repetition; similar events had occurred repeatedly. |
| 5 | Very high repetition; event type was routine or highly familiar. |

## Coding Notes

| Event | `surprise_level` | `event_repetition` | Rationale |
| --- | ---: | ---: | --- |
| Pelosi Visit | 2 | 1 | The visit was signaled in advance, but the market had limited recent precedent for this exact type of high-profile crisis. |
| Joint Sword 2023 | 1 | 2 | The exercise followed a recognizable political trigger and came after the 2022 Pelosi crisis pattern. |
| Joint Sword-2024A | 1 | 3 | The PLA response after Lai's inauguration was highly anticipated and followed prior exercise patterns. |
| Joint Sword-2024B | 1 | 4 | The event fits an increasingly repeated pattern of PLA exercises after political speeches or sovereignty-related signals. |

