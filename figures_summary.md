# Figures Summary

## raw_vs_abnormal_twse.png

This figure compares TWSE raw cumulative returns with TWSE abnormal cumulative returns over the [-7,+7] trading-day window for each event. It shows how benchmark adjustment against NASDAQ changes the apparent Taiwan-market reaction.

## raw_vs_abnormal_tsmc.png

This figure compares TSMC raw cumulative returns with TSMC abnormal cumulative returns over the [-7,+7] trading-day window for each event. It shows how adjustment against the SOX semiconductor benchmark changes the TSMC-specific event response.

## mechanism_comparison.png

This figure compares average abnormal CAR [-7,+7] by mechanism. It contrasts Risk events with Strategic_Importance events using both TWSE and TSMC abnormal returns.

## Note

The abnormal CAR values come from `market_abnormal_returns.csv`. Event metadata come from `final_event_study_sample.csv`. Raw CAR values were recomputed from `data/market.csv` because event-level raw CAR columns are not present in the two input CSV files.
