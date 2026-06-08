# Lai Inauguration China Response Case Note

## Purpose

This file records research notes and source leads for China's response to Lai Ching-te's May 2024 inauguration, especially the Joint Sword-2024A PLA exercise.

## Search Terms

- Lai Ching-te inauguration China response
- Lai inauguration PLA exercise
- May 2024 Taiwan inauguration military drills

## Case Summary

| Field | Note |
| --- | --- |
| Event | Lai Ching-te Inauguration / China Response |
| Inauguration Date | 2024-05-20 |
| PLA Exercise Date | 2024-05-23 to 2024-05-24 |
| PLA Exercise Name | Joint Sword-2024A |
| Event Category | Political event / military exercise |
| Project Relevance | Links Taiwan democratic transition, PRC coercive response, military risk, diplomatic risk, and security relevance. |
| Coding Status | Needs source verification before entry into `data/events_v1.csv`. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| Taiwan Ministry of National Defense | 2024-05-23 | Primary source for Taiwan response | Taiwan MND responded to the CCP announcement of Joint Sword-2024A around Taiwan. |
| CSIS ChinaPower | 2024 | Analytical source | Tracks China's response to Lai's inauguration and notes that China's MND announced Joint Sword-2024A on May 23. |
| Global Taiwan Institute | 2024 | Analytical source | Describes Joint Sword-2024A as a two-day exercise on May 23-24 following Lai's inauguration. |
| CNBC | 2024-05-23 | News source | Reports that China launched two days of drills after Lai took office. |
| Guardian | 2024-05 | News source | Reports China's "punishment" drills after Lai's inauguration and links them to sovereignty language in Lai's speech. |
| Axios | 2024-05-23 | News source | Reports that Taiwan's Defense Ministry went on alert after China announced two days of drills. |
| U.S. Department of Defense PRC Military Power Report | 2024 | Government / security source | Notes PLA Joint Sword-2024A in response to Lai's inauguration. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Variable | Preliminary Assessment | Reasoning | Manual Review |
| --- | --- | --- | --- |
| `military_risk` | High | Joint Sword-2024A involved PLA activity around Taiwan and outlying islands shortly after the inauguration. | Yes |
| `diplomatic_risk` | High | The drills followed PRC criticism of Lai's inauguration speech and Taiwan sovereignty language. | Yes |
| `sanctions_risk` | Low | The searched sources emphasize military and diplomatic response rather than sanctions. | Yes |
| `semiconductor_relevance` | Medium | Taiwan market and semiconductor exposure are relevant to broader risk, but the immediate event was political-military. | Yes |
| `ai_relevance` | Low | The inauguration response was not primarily AI-related. | Yes |
| `security_relevance` | High | The event directly relates to Taiwan security and U.S.-China competition. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and the scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2024-05-20,Lai Ching-te Inauguration,political event,,,,,,,,SOURCE_URL
2024-05-23,Joint Sword-2024A,military exercise,,,,,,,,SOURCE_URL
```

## Research Notes

Key coding decision:
The inauguration and the PLA exercise can be coded either as:

1. One combined political-military event window beginning on 2024-05-20.
2. Two separate events: the inauguration on 2024-05-20 and the PLA exercise on 2024-05-23.

The second option is cleaner for event-study analysis because the political trigger and military response occur on different dates.

Before coding:

1. Confirm the exact start and end times of Joint Sword-2024A.
2. Select one primary source and one analytical or news source.
3. Attach reasoning for each risk and relevance score.
4. Flag any uncertainty for manual review.

