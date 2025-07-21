# Mary and Martha

**Domain**: Sustainability / Battery Intelligence  
**Type**: Developer Tool / SaaS Prototype  

## Problem
Battery engineers and data scientists often work with complex and noisy time-series data. There’s no intuitive way to extract high-level insights from raw test data.

## Solution
Mary and Martha is a Python-first tool that automatically parses battery datasets (e.g., from PyProBE, CSVs), detects relevant features (e.g., charge/discharge phases, anomalies), and returns clean summaries and visualizations. Designed to integrate with ML workflows or be used standalone.

## Key Features
- Auto feature extraction (cycle count, voltage dip, rest phases)
- Summary statistics & anomaly detection
- Natural-language output: “During cycle 5, cell behavior deviated from previous patterns…”
- Fuzzy file name recognition for messy lab datasets

## Tech Stack
- **Python** (pandas, NumPy, scikit-learn, fuzzywuzzy)
- **Jupyter** for dev notebooks
- GitHub for version control

## Architecture
Coming soon — check `/design/architecture.png`

##  License
All rights reserved by Hayden Rodrigues. See `LICENSE` for details.
