# PLA Joint Sword Case Note

## Purpose

This file records research notes and source leads for the PLA's Joint Sword exercise series around Taiwan. These cases are relevant to military escalation, diplomatic risk, security relevance, and Taiwan Strait crisis coding.

## Search Terms

- Joint Sword 2023
- Joint Sword 2024A
- Joint Sword 2024B
- PLA Joint Sword Taiwan

## Case Summary

| Event | Approximate Date | Event Category | Project Relevance | Coding Status |
| --- | --- | --- | --- | --- |
| Joint Sword 2023 | 2023-04-08 to 2023-04-10 | Military exercise | PLA encirclement-style exercise after Taiwan President Tsai Ing-wen's U.S. transit and meeting with U.S. House Speaker Kevin McCarthy. | Needs source verification before coding. |
| Joint Sword-2024A | 2024-05-23 to 2024-05-24 | Military exercise | PLA exercise around Taiwan after President Lai Ching-te's inauguration. | Needs source verification before coding. |
| Joint Sword-2024B | 2024-10-14 to 2024-10-15 | Military exercise | PLA exercise around Taiwan after Lai's National Day speech; relevant to coercive pressure and blockade/quarantine scenarios. | Needs source verification before coding. |

## Source Leads

| Source | Event | Use in Project | Notes |
| --- | --- | --- | --- |
| PRC Ministry of National Defense / China Military Online | Joint Sword 2023 | Primary source for PLA framing | Reports PLA wrap-up of Joint Sword exercise from April 8 to April 10, 2023. |
| Global Taiwan Institute | Joint Sword 2023 | Analytical source | Compares PLA exercises after high-profile political visits and discusses symbolic encirclement. |
| Taiwan Ministry of National Defense | Joint Sword-2024A | Primary source for Taiwan response | Taiwan MND press release responding to the CCP announcement of Joint Sword-2024A. |
| Global Taiwan Institute | Joint Sword-2024A | Analytical source | Frames the exercise as a response to President Lai's inauguration and describes the May 23-24 exercise window. |
| CSIS ChinaPower | Joint Sword-2024B | Analytical source | Analyzes China's escalation after Lai's National Day speech and the October 14, 2024 drills. |
| Global Taiwan Institute | Joint Sword-2024B | Analytical source | Discusses Joint Sword-2024B as political warfare and creeping territorial encroachment. |
| Reuters / Investing.com | Joint Sword-2024B | News / case source | Reports U.S. Pentagon criticism of Chinese war games around Taiwan. |
| Taiwan News | Joint Sword-2024A / 2024B | News / case source | Reports PLA exercise announcements and Taiwan response. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event | military_risk | diplomatic_risk | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Joint Sword 2023 | High | Medium | Low | Medium | Low | High | Military exercise around Taiwan with clear coercive and security significance. | Yes |
| Joint Sword-2024A | High | High | Low | Medium | Low | High | Exercise followed Lai's inauguration and involved military activity around Taiwan and outlying islands. | Yes |
| Joint Sword-2024B | High | High | Low | Medium | Low | High | Exercise followed Lai's National Day speech and is relevant to blockade/quarantine scenarios. | Yes |

## Recommended Event Rows After Verification

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2023-04-08,Joint Sword 2023,military exercise,,,,,,,,SOURCE_URL
2024-05-23,Joint Sword-2024A,military exercise,,,,,,,,SOURCE_URL
2024-10-14,Joint Sword-2024B,military exercise,,,,,,,,SOURCE_URL
```

## Research Notes

Before adding these events to `data/events_v1.csv`:

1. Verify the exact start and end dates from primary or high-quality secondary sources.
2. Decide whether each exercise should be coded as one event or split across multiple event dates.
3. Record the source used for each risk and relevance score.
4. Keep reasoning attached to every assigned score.
5. Flag uncertainty for manual review if sources disagree on exercise scale, dates, or intent.

