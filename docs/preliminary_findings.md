# Preliminary Findings

## Section 1: Pelosi Visit (2022-08-02)

## Observed Results

| Measure | Result |
| --- | ---: |
| TWSE event-day return | -1.56% |
| TSMC event-day return | -2.38% |
| TWSE cumulative return at end of window | 1.74% |
| TSMC cumulative return at end of window | 2.59% |

The event window covers 7 trading days before and 7 trading days after the Pelosi Visit event date.

## Preliminary Interpretation

The Pelosi Visit shows evidence of short-term market disruption. On the event day, both TWSE and TSMC had negative daily returns, with TSMC showing the larger decline.

The event window also shows evidence of recovery. By the end of the -7/+7 trading-day window, both TWSE and TSMC cumulative returns were positive.

## Limitations

1. This is a single-event observation.
2. There is no benchmark market included yet.
3. There is no abnormal-return model yet.
4. USD/TWD is not included in the cleaned market dataset yet.
5. The analysis uses raw daily returns, not risk-adjusted returns.

## Research Notes

Questions for future analysis:

1. Did the Pelosi Visit generate abnormal returns relative to a benchmark such as NASDAQ or MSCI Asia?
2. Was the TSMC reaction stronger than the broader Taiwan market reaction?
3. Did USD/TWD move in the same direction as equity-market risk?
4. Did market recovery occur because investors reassessed the crisis as temporary?
5. Are military events, such as PLA exercises, more disruptive than diplomatic events?
6. Do high `military_risk` events produce larger market reactions than high `diplomatic_risk` events?

