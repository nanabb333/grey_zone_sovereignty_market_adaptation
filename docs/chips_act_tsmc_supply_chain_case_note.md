# CHIPS Act, TSMC, and Semiconductor Supply Chain Case Note

## Purpose

This file records research notes and source leads for the CHIPS and Science Act as it relates to Taiwan, TSMC, and semiconductor supply-chain resilience.

These sources are relevant to strategic investment, semiconductor relevance, security relevance, geoeconomics, and U.S.-Taiwan technology cooperation.

## Search Terms

- CHIPS and Science Act Taiwan
- CHIPS Act TSMC
- CHIPS Act semiconductor supply chain

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| CHIPS and Science Act | U.S. industrial policy intended to strengthen domestic semiconductor manufacturing and reduce supply-chain vulnerability. | Needs source verification before coding. |
| CHIPS Act and TSMC | Directly linked to TSMC Arizona investment, U.S. semiconductor capacity, and Taiwan's strategic role. | Needs source verification before coding. |
| Semiconductor supply-chain resilience | Supports the project's link between Taiwan's semiconductor role and economic-security outcomes. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| U.S. Department of Commerce: TSMC CHIPS Act preliminary terms | 2024-04-08 | Primary government source | Announces preliminary terms with TSMC, including up to US$6.6 billion in direct funding and expanded Arizona investment. |
| TSMC Arizona CHIPS Act / third fab announcement | 2024-04 | Primary corporate source | Notes proposed CHIPS Act funding, third leading-edge fab, and more than US$65 billion total Phoenix capital expenditure. |
| Council on Foreign Relations: What Is the CHIPS Act? | 2024 | Policy background source | Explains CHIPS Act goals, TSMC funding, loans, and restrictions on expansion in countries of concern. |
| Council on Foreign Relations: Onshoring Semiconductor Production | 2024 | Analytical source | Discusses national security versus economic efficiency and U.S. reliance on Taiwan-centered advanced chip manufacturing. |
| TSMC Arizona update | 2022-12-06 | Primary corporate source | Frames Arizona expansion in relation to CHIPS Act support and supply-chain resilience. |
| U.S. Department of Commerce CHIPS implementation remarks | 2024 | Government / policy source | Describes CHIPS Act implementation and leading-edge semiconductor manufacturing goals. |
| Taiwan-USA Industrial Cooperation Promotion Office | Current background | Taiwan government-linked source | Describes Taiwan's semiconductor supply chain and U.S.-Taiwan semiconductor cooperation. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | military_risk | diplomatic_risk | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CHIPS and Science Act signed | Low | Medium | Low | Very High | Medium | High | The law targets semiconductor capacity and supply-chain resilience, partly responding to reliance on Taiwan-centered advanced chip manufacturing. | Yes |
| TSMC CHIPS Act preliminary terms | Low | Medium | Low | Very High | High | High | TSMC Arizona funding directly links Taiwan's leading semiconductor firm to U.S. industrial policy and advanced-chip capacity. | Yes |
| TSMC Arizona third fab announcement | Low | Medium | Low | Very High | High | High | Third fab expands U.S.-based leading-edge manufacturing and reinforces supply-chain diversification. | Yes |
| Semiconductor supply-chain resilience framing | Low | Medium | Low | Very High | Medium | High | Supply-chain resilience is central to the economic-security rationale for CHIPS Act support. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2022-08-09,CHIPS and Science Act Signed,industrial policy,,,,,,,,SOURCE_URL
2024-04-08,TSMC CHIPS Act Preliminary Terms,investment / industrial policy,,,,,,,,SOURCE_URL
2024-04-08,TSMC Arizona Third Fab Announcement,investment,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. The CHIPS Act is industrial policy, not a sanctions event.
2. TSMC CHIPS Act funding is a strategic-investment and supply-chain-resilience event.
3. The project should distinguish between legislation-level events and company-specific investment announcements.
4. CHIPS Act sources can support `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
5. Market-impact evidence should be separated from policy and supply-chain evidence.

Before coding:

1. Use U.S. Commerce and TSMC releases as primary sources.
2. Confirm whether the coded date should be the CHIPS Act signing date, Commerce announcement date, or TSMC corporate announcement date.
3. Attach reasoning for every relevance score.
4. Flag uncertainty for manual review if investment totals, funding terms, or production timelines differ across sources.

