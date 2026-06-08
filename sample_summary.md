# Event Study Sample Summary

This memo documents the cleaned event-study sample after reducing severe [-7,+7] trading-day event-window overlap.

## Sample Counts

- Total candidate events reviewed: 25
- Final included events: 12
- Excluded events: 13

## Final Event Count by Mechanism

| mechanism | count |
| --- | ---: |
| Risk | 8 |
| Strategic_Importance | 4 |

## Final Event Count by Event Category

| event_category | count |
| --- | ---: |
| Military Demonstration | 6 |
| Technology Competition | 4 |
| Diplomatic Shock | 1 |
| Political Signaling | 1 |

## Final Event Count by Event Role

| event_role | count |
| --- | ---: |
| Military_Risk_Shock | 6 |
| Strategic_Importance_Shock | 4 |
| Diplomatic_Risk_Shock | 1 |
| Political_Signaling_Shock | 1 |

## Included Events

| date | event_name | mechanism | event_category | event_role |
| --- | --- | --- | --- | --- |
| 2022-08-02 | Pelosi Visit | Risk | Diplomatic Shock | Diplomatic_Risk_Shock |
| 2022-10-07 | BIS Advanced Semiconductor Export Controls | Strategic_Importance | Technology Competition | Strategic_Importance_Shock |
| 2022-12-06 | TSMC Arizona US$40B Expansion | Strategic_Importance | Technology Competition | Strategic_Importance_Shock |
| 2023-04-08 | Joint Sword 2023 | Risk | Military Demonstration | Military_Risk_Shock |
| 2023-08-19 | PLA Drills After Lai U.S. Transit | Risk | Military Demonstration | Military_Risk_Shock |
| 2024-04-08 | TSMC CHIPS Act Preliminary Terms | Strategic_Importance | Technology Competition | Strategic_Importance_Shock |
| 2024-05-23 | Joint Sword-2024A | Risk | Military Demonstration | Military_Risk_Shock |
| 2024-06-21 | PRC Judicial Guidelines on Taiwan Independence | Risk | Political Signaling | Political_Signaling_Shock |
| 2024-10-14 | Joint Sword-2024B | Risk | Military Demonstration | Military_Risk_Shock |
| 2025-01-22 | PLA Joint Combat Readiness Patrols Around Taiwan | Risk | Military Demonstration | Military_Risk_Shock |
| 2025-03-04 | TSMC US$165B U.S. Expansion | Strategic_Importance | Technology Competition | Strategic_Importance_Shock |
| 2025-04-01 | Strait Thunder-2025A | Risk | Military Demonstration | Military_Risk_Shock |

## Excluded Events and Reasons

| date | event_name | exclusion_reason |
| --- | --- | --- |
| 2022-07-19 | China Warns Against Pelosi Taiwan Visit | Excluded due to severe overlap with Pelosi Visit; Pelosi Visit is the preferred repricing event. |
| 2022-08-03 | China Trade Restrictions After Pelosi Visit | Excluded due to severe overlap with Pelosi Visit; Pelosi Visit is the preferred repricing event. |
| 2022-08-04 | PLA Military Exercises After Pelosi Visit | Excluded due to severe overlap with Pelosi Visit; Pelosi Visit is the preferred repricing event. |
| 2023-04-05 | Tsai-McCarthy Meeting | Excluded due to severe overlap with Joint Sword 2023; Joint Sword 2023 is the preferred repricing event. |
| 2023-08-12 | Lai U.S. Transit | Excluded due to severe overlap with PLA Drills After Lai U.S. Transit; the military response is the preferred repricing event. |
| 2023-08-26 | China Sends Aircraft and Vessels After U.S. Arms Sale | Excluded due to severe overlap with the August 2023 Lai transit military-response window. |
| 2024-01-13 | Lai Wins Taiwan Presidential Election | Excluded because event-day market data are incomplete: nasdaq_close;nvidia_close;sox_close. |
| 2024-01-15 | Nauru Switches Recognition to China | Excluded because event-day market data are incomplete: nasdaq_close;nvidia_close;sox_close. |
| 2024-02-14 | Kinmen Boat Capsizing Incident | Excluded because event-day market data are incomplete: twse_close;tsmc_close. |
| 2024-02-18 | China Coast Guard Patrols Near Kinmen | Excluded because event-day market data are incomplete: nasdaq_close;nvidia_close;sox_close. |
| 2024-05-20 | Lai Ching-te Inauguration | Excluded due to severe overlap with Joint Sword-2024A; Joint Sword-2024A is the preferred repricing event. |
| 2024-10-10 | Lai National Day Speech | Excluded due to severe overlap with Joint Sword-2024B; Joint Sword-2024B is the preferred repricing event. |
| 2025-12-29 | Justice Mission 2025 | Excluded because no complete [-7,+7] trading window is available in the market dataset. |
