# NVIDIA Taiwan AI Factory Case Note

## Purpose

This file records research notes and source leads for NVIDIA's Taiwan AI factory, Foxconn partnership, Taiwan investment context, and NVIDIA-TSMC partnership announcements.

These cases are relevant to strategic investment, AI relevance, semiconductor relevance, security relevance, and Taiwan's role in global AI infrastructure.

## Search Terms

- Nvidia Taiwan AI factory
- Nvidia Taiwan investment
- Nvidia Foxconn AI factory Taiwan
- Nvidia TSMC partnership announcement

## Case Summary

| Topic | Project Relevance | Coding Status |
| --- | --- | --- |
| NVIDIA-Foxconn Taiwan AI factory | Major AI infrastructure announcement involving NVIDIA, Foxconn, and Taiwan. | Needs source verification before coding. |
| NVIDIA Taiwan investment context | Supports Taiwan's strategic value in AI, compute, and semiconductor ecosystems. | Needs event-level source verification. |
| NVIDIA-Foxconn AI factory partnership | Relevant to strategic investment and Taiwan AI infrastructure. | Needs source verification before coding. |
| NVIDIA-TSMC partnership announcement | Relevant to semiconductor design/manufacturing and AI-enabled fabs. | Needs source verification before coding. |

## Source Leads

| Source | Date | Use in Project | Notes |
| --- | --- | --- | --- |
| NVIDIA investor release: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA | 2025-05-18 | Primary corporate source | Announces NVIDIA and Foxconn working with Taiwan government to build an AI factory supercomputer using NVIDIA Blackwell infrastructure. |
| NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA | 2025-05 | Primary corporate source | Newsroom version of the AI factory announcement; notes support for TSMC and other leading companies. |
| Hon Hai / Foxconn press release | 2025-05-19 | Primary corporate source | States Foxconn will build an AI factory and become Taiwan's first NVIDIA Cloud Partner. |
| CNBC | 2025-05-20 | News / market-policy source | Reports the Taiwan AI data center with NVIDIA and Foxconn will have 100 MW of power and mentions TSMC and Taiwan government involvement. |
| Taiwan News | 2025-05 | News source | Reports Foxconn and NVIDIA AI factory partnership in Taiwan. |
| NVIDIA investor release: NVIDIA and TSMC Bring AI Into Fabs | 2026-06-01 | Primary corporate source | Separate NVIDIA-TSMC announcement about using NVIDIA accelerated computing and AI for semiconductor design and manufacturing. |
| NVIDIA-Foxconn AI industrial revolution release | 2023-10 | Primary corporate source | Earlier partnership context for AI factories, manufacturing systems, and simulation. |

## Preliminary Coding Considerations

Do not treat these scores as final until sources are verified.

| Event / Topic | military_risk | diplomatic_risk | sanctions_risk | semiconductor_relevance | ai_relevance | security_relevance | Reasoning | Manual Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NVIDIA-Foxconn Taiwan AI factory | Low | Medium | Low | High | Very High | High | The announcement directly builds Taiwan AI infrastructure and supports TSMC and Taiwan's broader technology ecosystem. | Yes |
| Foxconn becomes NVIDIA Cloud Partner in Taiwan | Low | Medium | Low | High | Very High | Medium | Strengthens Taiwan's AI compute capacity and industrial AI platform role. | Yes |
| NVIDIA-TSMC AI into fabs announcement | Low | Medium | Low | Very High | Very High | High | Directly connects NVIDIA AI systems with TSMC semiconductor design and manufacturing. | Yes |
| NVIDIA-Foxconn AI industrial revolution partnership | Low | Medium | Low | High | High | Medium | Earlier partnership context for AI factories and manufacturing systems. | Yes |

## Recommended Event Rows After Verification

These should not be copied into `data/events_v1.csv` until sources are selected and scores are finalized.

```csv
date,event_name,event_category,military_risk,diplomatic_risk,sanctions_risk,semiconductor_relevance,ai_relevance,security_relevance,source
2025-05-18,NVIDIA-Foxconn Taiwan AI Factory Announcement,investment,,,,,,,,SOURCE_URL
2025-05-19,Foxconn NVIDIA Cloud Partner Taiwan Announcement,investment,,,,,,,,SOURCE_URL
2026-06-01,NVIDIA-TSMC AI Into Fabs Announcement,investment / technology partnership,,,,,,,,SOURCE_URL
```

## Research Notes

Key distinctions:

1. The 2025 NVIDIA-Foxconn-Taiwan AI factory announcement is an AI infrastructure and strategic-investment event.
2. The 2026 NVIDIA-TSMC announcement is a separate technology-partnership event focused on AI in semiconductor fabs.
3. These are not sanctions events, but they are relevant to U.S.-Taiwan technology ties, AI infrastructure, and Taiwan's strategic importance.
4. Market-impact evidence should be separated from corporate announcement evidence.
5. If the project studies event timing, code NVIDIA-Foxconn and NVIDIA-TSMC as separate events.

Before coding:

1. Use NVIDIA and Foxconn releases as primary sources.
2. Use CNBC or Taiwan News only as supporting news sources.
3. Confirm whether the event date should follow NVIDIA's May 18 release date or Foxconn's May 19 release date.
4. Attach reasoning for `semiconductor_relevance`, `ai_relevance`, and `security_relevance`.
5. Flag uncertainty for manual review if partnership scope or investment amount is unclear.

