# China Sanctions and Technology Controls Case Note

## Purpose

This file records research notes and source leads for U.S. sanctions, investment restrictions, and export controls affecting Chinese military-industrial and technology companies. These sources are relevant to the project's sanctions risk, semiconductor relevance, AI relevance, financial statecraft, and U.S.-China competition variables.

## Search Terms

- Chinese Military Industrial Complex sanctions
- OFAC China sanctions
- US sanctions Chinese technology companies
- SMIC sanctions

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| Chinese Military-Industrial Complex sanctions | U.S. financial-statecraft tool restricting certain securities investments connected to PRC military-linked companies. | Needs source verification before coding. |
| OFAC China sanctions | Primary source for U.S. Treasury sanctions programs and rules. | Needs source verification before coding. |
| U.S. sanctions on Chinese technology companies | Relevant to geoeconomics, technology competition, AI, semiconductors, and market effects. | Needs event-level source verification. |
| SMIC sanctions / export controls | Key semiconductor case involving U.S. Commerce Entity List restrictions. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| OFAC Chinese Military Companies Sanctions page | Current program page | Primary source | Tracks Chinese Military Companies sanctions program materials and related executive orders. |
| OFAC Chinese Military-Industrial Complex Sanctions Regulations | 2022 | Primary legal source | Regulations implementing Chinese Military-Industrial Complex sanctions under 31 CFR Part 586. |
| e-CFR / Cornell Legal Information Institute, 31 CFR Part 586 | Current legal text | Legal reference | Provides the regulatory text for Chinese Military-Industrial Complex Sanctions Regulations. |
| U.S. GAO Federal Rules page | 2022 | Regulatory tracking source | Summarizes the Chinese Military-Industrial Complex Sanctions Regulations rule. |
| U.S. Department of Commerce / BIS | 2020-12-18 | Primary source for SMIC restrictions | Announces SMIC's addition to the Entity List, restricting access to key U.S. technology. |
| Legal / sanctions law firm summaries | 2020-2022 | Secondary explanation | Useful for interpreting OFAC and BIS actions, but should not replace official sources. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- |
| Chinese Military-Industrial Complex sanctions regulations | High | Medium | Medium | High | U.S. investment restrictions target PRC military-linked companies and connect finance, security, and technology competition. | Yes |
| OFAC Chinese Military Companies sanctions program | High | Medium | Medium | High | OFAC program is a financial-statecraft mechanism tied to PRC military-linked firms. | Yes |
| SMIC Entity List addition | High | High | Medium | High | SMIC is a major Chinese semiconductor firm; BIS restrictions limit access to U.S. technology on national security grounds. | Yes |
| U.S. sanctions on Chinese technology companies | Medium to High | High | High | High | Technology-company sanctions and export controls affect semiconductors, AI, surveillance, and military-civil fusion concerns. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2020-12-18,SMIC Added to Entity List,sanctions / export control,,,,,,,,SOURCE_URL
2022-02-16,Chinese Military-Industrial Complex Sanctions Regulations,sanctions / financial statecraft,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinction:

1. OFAC sanctions and investment restrictions are Treasury-administered financial-statecraft tools.
2. BIS Entity List controls are Commerce-administered export-control tools.
3. SMIC is most directly linked to semiconductor relevance and U.S. technology-access restrictions.
4. Chinese Military-Industrial Complex sanctions are more directly linked to investment restrictions and military-linked firms.

Before coding:

1. Use official OFAC, e-CFR, GAO, or Commerce/BIS sources where possible.
2. Do not merge OFAC sanctions and BIS Entity List controls into one category without noting the distinction.
3. Attach reasoning for `sanctions_risk`, `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
4. Flag uncertainty for manual review if a source discusses broad policy rather than a discrete event date.

