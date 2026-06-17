# Event Family Expansion Projection

> Academic Research Notice:
> This projection estimates how the dataset would change if all Include candidates were integrated after validation. It does not modify the dataset or report new event-study results.

## Dataset Size

| Dataset state | Event count |
| --- | ---: |
| Current validated dataset, `data/events_v2.csv` | 18 |
| Projected dataset after 20 Include candidates | 38 |
| Upper-bound candidate pool if Review Further events pass | 41 |

## Current Family Distribution

| Event family | Current count |
| --- | ---: |
| `Military_Exercise` | 8 |
| `Diplomatic_Shock` | 3 |
| `Strategic_Investment` | 3 |
| `Economic_Coercion` | 1 |
| `Export_Control` | 1 |
| `Legal_Judicial_Signaling` | 1 |
| `Political_Signaling` | 1 |
| Total | 18 |

## Projected Family Distribution

Projected distribution uses the current V2 baseline plus the 20 Include candidates.

| Event family | Current count | New Include candidates | Projected count |
| --- | ---: | ---: | ---: |
| `Military_Exercise` | 8 | 0 | 8 |
| `Export_Control` | 1 | 8 | 9 |
| `Strategic_Investment` | 3 | 1 | 4 |
| `Industrial_Policy` | 0 | 3 | 3 |
| `Critical_Materials_Control` | 0 | 3 | 3 |
| `Diplomatic_Shock` | 3 | 0 | 3 |
| `Recognition_Diplomacy` | 0 | 3 | 3 |
| `Economic_Coercion` | 1 | 1 | 2 |
| `Political_Signaling` | 1 | 1 | 2 |
| `Legal_Judicial_Signaling` | 1 | 0 | 1 |
| Total | 18 | 20 | 38 |

## Required Comparison Categories

| Analytical category | Current count | Projected count | Change |
| --- | ---: | ---: | ---: |
| Diplomatic events | 3 | 6 | +3 |
| Export-control events | 1 | 9 | +8 |
| Industrial-policy events | 0 | 3 | +3 |
| Military-signaling events | 8 | 8 | 0 |
| Strategic-investment events | 3 | 4 | +1 |

## Categories That Become Analytically Stronger

- Export controls become a true comparison family rather than a single case.
- Industrial policy becomes observable as its own family through U.S., EU, and China support events.
- Critical-materials controls become a new supply-chain-security channel.
- Recognition diplomacy becomes a dedicated Taiwan diplomatic-competition family.
- Economic coercion becomes modestly stronger through the Micron restriction.

## Categories That Remain Weak

- Military signaling remains numerically large but does not gain new variation from the Include candidates.
- Strategic investment improves only slightly unless Review Further CAND-V3-017 is later integrated.
- Legal and judicial signaling remains a single-event family.
- Diplomatic recognition improves, but immediate market-reaction interpretation may remain weaker than export controls.

## Interpretation

The V3 expansion would make the dataset less dependent on Taiwan military events and more capable of testing broader geopolitical competition mechanisms. The largest analytical upgrade is the move from one export-control event to a sequence of export-control and countermeasure events across U.S., allied, Chinese, and Taiwan actors.
