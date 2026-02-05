# AGI Path Predictor v1.0.0 – Initial Public Release

Welcome to the first public release of **AGI Path Predictor**, a data-driven framework for estimating timelines to Artificial General Intelligence (AGI).

## Overview
This repository provides:
- A modular prediction pipeline combining historical technology trends, expert surveys, and compute scaling laws
- Datasets: curated timelines from Metaculus, AI Impacts, expert elicitations, and compute growth metrics
- Models: baseline implementations (extrapolation, Bayesian updating, simple neural forecasts)
- Visualization tools for probability distributions and sensitivity analysis
- Scripts for updating predictions with new data

## Key Features
- **Trend extrapolation** from biological anchors and compute scaling
- **Expert aggregation** with weighting and confidence calibration
- **Monte Carlo sampling** for probabilistic timelines
- Easy-to-extend structure for adding new models or data sources

## Current Predictions (as of February 2026)
- Median estimated AGI arrival: **2031**
- 25th–75th percentile: **2028–2038**
- Probability of AGI by 2030: **~42%**

> Note: These are baseline model outputs and will evolve as new data and models are added.

## Getting Started
```bash
git clone https://github.com/Hallotoshi/AGI-Path-Predictor.git
cd AGI-Path-Predictor
pip install -r requirements.txt
python run_baseline.py
```

Contributions, issues, and new data sources are very welcome!

Thank you for checking out the project.
