# Huawei Sanctions and Semiconductor Restrictions Case Note

## Purpose

This file records research notes and source leads for U.S. restrictions on Huawei, including the Entity List designation, semiconductor restrictions, and market impacts on technology and semiconductor firms.

## Search Terms

- Huawei sanctions market impact
- Huawei Entity List
- Huawei semiconductor restrictions

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| Huawei Entity List | U.S. export-control action against a major Chinese technology firm with national-security implications. | Needs source verification before coding. |
| Huawei semiconductor restrictions | Directly relevant to semiconductor supply chains, U.S. technology controls, and China technology competition. | Needs source verification before coding. |
| Huawei sanctions market impact | Relevant to market-reaction variables, especially semiconductor suppliers and technology equities. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| U.S. Department of Commerce / BIS | 2019-08-19 | Primary source | Reports additional Huawei affiliates added to the Entity List and temporary license details. |
| BIS Huawei Entity List FAQs | 2019 / current reference | Primary source | Explains Huawei Entity List timing and affiliate additions. |
| Federal Register / BIS | 2019 | Primary legal source | Documents Huawei affiliate additions and Entity List rulemaking. |
| GAO Federal Rules | 2020-08-20 | Regulatory tracking source | Tracks Huawei affiliate additions, Temporary General License removal, and Foreign-Produced Direct Product Rule amendments. |
| Congressional Research Service | 2022 | Policy analysis | Summarizes U.S. restrictions on Huawei across national security, foreign policy, and economic interests. |
| CNBC | 2019-05 | Market reaction source | Reports chipmaker stock declines after restrictions and supplier ties to Huawei came under pressure. |
| Axios | 2019-2020 | News / market-policy source | Covers temporary reprieve and potential impact on U.S. companies from Huawei restrictions. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| Huawei Entity List designation | High | High | Medium | High | The Entity List restricted exports to Huawei on national-security and foreign-policy grounds and affected technology supply chains. | Yes |
| Huawei semiconductor restrictions / FDPR expansion | High | Very High | Medium | High | Foreign Direct Product Rule changes targeted Huawei access to chips and semiconductor manufacturing supply chains. | Yes |
| Huawei supplier market impact | Medium | High | Medium | Medium | Semiconductor supplier stocks reacted to Huawei restrictions, making this useful for market-impact coding. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2019-05-16,Huawei Added to Entity List,sanctions / export control,,,,,,,,SOURCE_URL
2020-05-15,Huawei Semiconductor Restrictions Expanded,sanctions / semiconductor control,,,,,,,,SOURCE_URL
2020-08-20,Huawei FDPR and Entity List Restrictions Expanded,sanctions / semiconductor control,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. The Huawei Entity List action is a Commerce/BIS export-control measure, not an OFAC sanctions program.
2. The semiconductor restrictions are especially relevant to supply-chain control and U.S.-China technology competition.
3. Market-impact evidence should be separated from legal-policy evidence.
4. Supplier stock reactions can support market-reaction analysis, but should not be used alone to code the policy event.

Before coding:

1. Use official BIS, Federal Register, GAO, or CRS sources for policy-event dates.
2. Use financial-news sources only for market-impact evidence.
3. Attach reasoning for `sanctions_risk`, `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
4. Flag uncertainty for manual review if dates differ across sources.

