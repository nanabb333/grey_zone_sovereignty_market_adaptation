# TSMC Overseas Investment Case Note

## Purpose

This file records research notes and source leads for TSMC overseas investment announcements, especially Arizona expansion announcements. These cases are relevant to strategic investment, semiconductor relevance, AI relevance, security relevance, supply-chain resilience, and U.S.-Taiwan technology cooperation.

## Search Terms

- TSMC Arizona announcement
- TSMC overseas investment announcement
- TSMC expansion investment

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| TSMC Arizona announcement | Major overseas semiconductor investment tied to U.S. supply-chain resilience and Taiwan's strategic value. | Needs source verification before coding. |
| TSMC Arizona expansion | Indicates growing strategic importance of TSMC in U.S. semiconductor policy. | Needs source verification before coding. |
| TSMC overseas investment | Supports `strategic_value`, `semiconductor_relevance`, and `security_relevance` coding. | Needs event-level source verification. |
| TSMC AI-focused expansion | Directly relevant to AI infrastructure and advanced semiconductor supply chains. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| TSMC press release: TSMC Announces Updates for TSMC Arizona | 2022-12-06 | Primary corporate source | Announces second Arizona fab and approximately US$40 billion total investment for two fabs. |
| U.S. Department of Commerce CHIPS Act announcement | 2024-04-08 | Primary government source | Announces preliminary terms with TSMC and expanded investment exceeding US$65 billion for three Arizona fabs. |
| TSMC press release: TSMC Arizona and U.S. Department of Commerce announce proposed CHIPS Act direct funding | 2024-04 | Primary corporate / government-linked source | Notes third leading-edge fab in Phoenix and more than US$65 billion total capital expenditure. |
| TSMC press release: TSMC intends to expand U.S. investment to US$165 billion | 2025-03-04 | Primary corporate source | Frames expansion as powering the future of AI and increasing total expected U.S. investment to US$165 billion. |
| CNBC | 2022-12-06 | News / market-policy source | Reports TSMC raising Arizona investment from US$12 billion to US$40 billion. |
| TSMC annual reports | 2020 / 2022 | Corporate reporting source | Provides context for overseas fab strategy and Arizona investment. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | military_risk | diplomatic_risk | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TSMC Arizona second fab / US$40B update | Low | Medium | Low | Very High | Medium | High | Major U.S.-based TSMC investment strengthens semiconductor supply-chain resilience and reflects Taiwan's strategic value. | Yes |
| TSMC Arizona third fab / US$65B CHIPS Act announcement | Low | Medium | Low | Very High | High | High | Adds leading-edge U.S. production and links TSMC to U.S. industrial policy and advanced technology security. | Yes |
| TSMC US$165B AI-focused expansion | Low | Medium | Low | Very High | Very High | High | Explicitly tied to AI and advanced semiconductor capacity in the United States. | Yes |
| TSMC overseas investment strategy | Low | Medium | Low | Very High | Medium | High | Overseas fabs reflect strategic diversification of Taiwan-centered semiconductor production. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-12-06,TSMC Arizona US$40B Expansion,investment,,,,,,,,SOURCE_URL
2024-04-08,TSMC Arizona CHIPS Act and Third Fab Announcement,investment,,,,,,,,SOURCE_URL
2025-03-04,TSMC US$165B AI-Focused U.S. Expansion,investment,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. TSMC investment events are strategic-investment events, not sanctions events.
2. Arizona expansion announcements should be coded separately if the project studies event timing and market reactions.
3. The 2022 announcement emphasizes overseas semiconductor manufacturing and supply-chain resilience.
4. The 2024 announcement links TSMC Arizona to CHIPS Act support and a third leading-edge fab.
5. The 2025 announcement is especially relevant to AI because TSMC frames the expansion around AI and cutting-edge applications.

Before coding:

1. Use TSMC press releases and U.S. Commerce releases as primary sources.
2. Decide whether to include only official announcement dates or also board approvals and capital injections.
3. Attach reasoning for `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
4. Flag uncertainty for manual review if investment totals or production timelines differ across sources.

