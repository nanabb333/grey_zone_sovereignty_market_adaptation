# U.S. Semiconductor Export Controls on China Case Note

## Purpose

This file records research notes and source leads for U.S. semiconductor export controls on China, especially the October 2022 BIS advanced computing and semiconductor manufacturing restrictions.

These controls are relevant to the project's sanctions risk, semiconductor relevance, AI relevance, security relevance, geoeconomics, and U.S.-China technology competition variables.

## Search Terms

- US semiconductor export controls China
- October 2022 semiconductor restrictions
- BIS advanced chip restrictions

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| October 2022 BIS semiconductor export controls | Major U.S. export-control action targeting China's access to advanced chips, supercomputing inputs, and semiconductor manufacturing equipment. | Needs source verification before coding. |
| BIS advanced chip restrictions | Directly relevant to AI compute, advanced semiconductors, and U.S.-China technology competition. | Needs source verification before coding. |
| Semiconductor manufacturing equipment controls | Relevant to supply-chain control and China's ability to produce advanced chips domestically. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| U.S. Department of Commerce / BIS | 2022-10-07 | Primary source | Announces new export controls on advanced computing and semiconductor manufacturing items to the PRC. |
| BIS October 2022 press release PDF | 2022-10-07 | Primary source | Provides official rule summary and effective dates. |
| BIS FAQs on advanced computing and semiconductor manufacturing items rule | 2022-10 | Primary guidance | Explains implementation details for the October 2022 rule. |
| BIS October 2023 strengthening rule | 2023-10 | Primary source | Strengthens and clarifies October 2022 controls on advanced computing semiconductors and semiconductor manufacturing equipment. |
| Axios | 2022-10-07 | News / market-policy source | Reports the Biden administration's export restrictions and expected implications for China and chipmakers. |
| AP News | 2023 | News / response source | Reports China's criticism that advanced-chip controls harm supply chains and economic activity. |
| Legal / trade-control firm summaries | 2022 | Secondary explanation | Useful for interpreting technical provisions, but official BIS sources should anchor coding. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| October 2022 BIS advanced computing and semiconductor controls | High | Very High | Very High | High | The rule restricted China's access to advanced chips, supercomputing inputs, and semiconductor manufacturing capabilities on national-security grounds. | Yes |
| Semiconductor manufacturing equipment controls | High | Very High | Medium | High | Controls targeted equipment and support needed to produce advanced integrated circuits in China. | Yes |
| Advanced AI chip restrictions | High | High | Very High | High | Restrictions affected advanced computing chips relevant to AI, supercomputing, and military applications. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-10-07,BIS Advanced Semiconductor Export Controls,sanctions / export control,,,,,,,,SOURCE_URL
2023-10-17,BIS Advanced Chip Controls Strengthened,sanctions / export control,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. These are Commerce/BIS export controls, not OFAC financial sanctions.
2. The October 2022 controls target advanced computing chips, semiconductor manufacturing equipment, supercomputer end uses, and certain U.S. person support.
3. The controls are central to semiconductor relevance and AI relevance.
4. Market-impact evidence should be separated from legal-policy evidence.
5. Later 2023 BIS rules should be treated as updates or strengthening actions, not as the original October 2022 policy shock.

Before coding:

1. Use official BIS sources for event dates and rule descriptions.
2. Use secondary legal summaries only to interpret technical rules.
3. Decide whether to code the initial October 7 announcement date, Federal Register publication date, or effective-date sequence.
4. Attach reasoning for `sanctions_risk`, `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
5. Flag uncertainty for manual review if rule timing or scope differs across sources.

