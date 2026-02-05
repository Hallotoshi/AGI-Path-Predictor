# AGI Path Predictor (Prototype)

A lightweight Streamlit dashboard that explores a proxy for AGI progress by combining AI benchmark performance (currently synthetic ARC-AGI scores) with sentiment analysis from X (Twitter) posts related to Grok, xAI, and Elon Musk.

A RandomForest model is trained on historical trends to predict short-term benchmark progress based on recent performance delta and public sentiment.

**This is an early-stage prototype / proof-of-concept.** It is **not** a rigorous AGI timeline forecaster. The goal is to experiment with leading indicators (hype/sentiment) that might correlate with benchmark leaps.

## Features (Current)
- Synthetic monthly ARC-AGI benchmark time series
- Sentiment analysis of recent X posts (via TextBlob)
- RandomForestRegressor for one-step-ahead progress prediction
- Interactive Streamlit app with visualizations and "what-if" sliders
- Docker support

## Roadmap / Future Work
- Replace synthetic data with real ARC-AGI leaderboard history
- Integrate additional benchmarks (MMLU, BIG-Bench, etc.)
- Switch to robust X data source (official API or academic datasets)
- Expand features: compute trends, publication volume, investment data
- Advanced modeling: time-series (Prophet/LSTM), multi-step, probabilistic forecasts
- True timeline extrapolation (scaling laws, biological anchors, Monte Carlo)

## Quick Start
```bash
pip install -r requirements.txt
python data_fetch.py   # generates CSVs (note: snscrape may fail due to X API changes)
python train_model.py
streamlit run app.py
```

Or with Docker:
```bash
docker build -t agi-predictor .
docker run -p 8501:8501 agi-predictor
```

## Limitations
- Data fetching relies on deprecated `snscrape` (planned migration)
- Tiny dataset → limited predictive power
- Single-step prediction only
- No probabilistic timelines yet

Contributions welcome! Open issues for bugs, ideas, or the roadmap items above.

Licensed under MIT (see LICENSE).