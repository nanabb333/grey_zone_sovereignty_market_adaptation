# Pelosi Taiwan Visit Case Note

## Purpose

This file records research notes and source leads for the August 2022 Nancy Pelosi visit to Taiwan. The case is relevant to the project's geopolitical risk, military escalation, and Taiwan financial-market reaction variables.

## Search Terms

- Nancy Pelosi Taiwan visit August 2022
- Pelosi Taiwan visit market reaction
- Pelosi Taiwan visit military exercises
- Pelosi Taiwan visit Taiwan stock market

## Case Summary

| Field | Note |
| --- | --- |
| Event | Pelosi Visit |
| Date | 2022-08-02 |
| Event Category | Diplomatic crisis / geopolitical risk event |
| Crisis Link | Associated with the Fourth Taiwan Strait Crisis |
| Market Variables | TAIEX, USD/TWD, TSMC |
| Risk Variables | `military_risk`, `diplomatic_risk`, `security_relevance` |
| Coding Status | Needs source verification before entry into `data/events_v1.csv` |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| Reuters / Investing.com | 2022-08 | Military escalation source | Reports that China deployed aircraft and fired missiles near Taiwan during drills after Pelosi's visit. |
| CSIS | 2022 | Policy and security analysis | Discusses implications of Pelosi's visit for the Indo-Pacific and notes Taiwan stock-market softness around the visit. |
| Fortune | 2022 | Market reaction source | Covers investor concern and Taiwan stock-market reaction around the visit. |
| CNBC | 2022 | Military and diplomatic response source | Covers Chinese military pressure, diplomatic retaliation, and live-fire exercise announcements. |
| Bloomberg | 2022 | Market reaction source | Already listed in project source inventory as a Pelosi Visit market-reaction source. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Variable | Preliminary Assessment | Reasoning | Manual Review |
| --- | --- | --- | --- |
| `military_risk` | High | PLA military exercises and missile activity were reported around the visit. | Yes |
| `diplomatic_risk` | High | The visit triggered sharp PRC diplomatic opposition and U.S.-China tension. | Yes |
| `sanctions_risk` | Medium | China announced retaliatory measures, but sanctions coding should be checked carefully. | Yes |
| `semiconductor_relevance` | Medium | Taiwan market and TSMC exposure are relevant, but the visit was primarily diplomatic/security-focused. | Yes |
| `ai_relevance` | Low | The event was not primarily about AI. | Yes |
| `security_relevance` | High | The visit is directly relevant to Taiwan security and U.S.-China competition. | Yes |

## Recommended Event Row After Verification

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-08-02,Pelosi Visit,diplomatic crisis,,,,,,,,SOURCE_URL
```

## Research Notes

This event should be coded only after confirming:

1. The exact event date and market window.
2. Whether to code the Pelosi landing date, departure date, PLA exercise announcement date, or the first full day of exercises as separate events.
3. Whether military exercises should be a distinct event from the diplomatic visit.
4. Which source is used for each risk score.

