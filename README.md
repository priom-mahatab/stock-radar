# AI Market Radar 

A daily AI-powered stock discovery system that runs after market close and recommends stocks and ETFs worth researching. Built to learn about markets, practice machine learning engineering, and surface opportunities — not to automate trading.

---

## What It Does

Every day after the market closes, AI Market Radar:

- Analyzes the S&P 100 stock universe
- Computes price, volume, sector, and sentiment features
- Ranks stocks using a machine learning model
- Outputs a daily report with the top 5 stocks and 2 ETFs to research

### Example Output

```
AI MARKET RADAR
Date: 2026-03-09

Top Stocks to Research

NVDA  |  Technology
  - Strong 5-day momentum (+6.2%)
  - Unusual volume (2.4x 30-day average)
  - Positive news sentiment
  - Sector outperforming market

Top ETFs to Watch
  - XLK  (Technology Select Sector SPDR)
  - XLE  (Energy Select Sector SPDR)
```

---

## Project Structure

```
stock_radar/
├── config/
│   ├── settings.py          # Central constants and paths
│   └── universe.py          # Stock and ETF universe
├── data/
│   ├── ingestion/
│   │   ├── market_data.py   # yfinance wrapper
│   │   ├── news_fetcher.py  # NewsAPI / Finnhub wrapper
│   │   └── sector_data.py   # Sector ETF performance
│   └── storage/
│       └── cache.py         # CSV cache with validity checks
├── features/
│   ├── price_features.py
│   ├── volume_features.py
│   ├── sector_features.py
│   ├── sentiment_features.py
│   └── feature_pipeline.py
├── models/
│   ├── trainer.py
│   ├── predictor.py
│   ├── ranker.py
│   └── artifacts/
├── sentiment/
│   ├── analyzer.py
│   └── aggregator.py
├── pipeline/
│   ├── daily_runner.py
│   └── scheduler.py
├── reports/
│   ├── formatter.py
│   ├── explainer.py
│   └── output/
├── tests/
├── notebooks/
├── utils.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Build Phases

| Phase | Status | Description |
|-------|--------|-------------|
| 1 | 🔨 In Progress | Market data ingestion, caching, validation |
| 2 | ⏳ Planned | Feature engineering (price, volume, sector) |
| 3 | ⏳ Planned | ML ranking model (XGBoost / LightGBM) |
| 4 | ⏳ Planned | News sentiment analysis (VADER / FinBERT) |
| 5 | ⏳ Planned | Automation and daily reporting |
| 6 | 💡 Future | Backtesting engine |
| 7 | 💡 Future | Market regime detection |
| 8 | 💡 Future | LLM news summarization |
| 9 | 💡 Future | Streamlit dashboard |

---

## Data Sources

| Data | Source | Library |
|------|--------|---------|
| Price & volume history | Yahoo Finance | `yfinance` |
| News headlines | NewsAPI / Finnhub | `requests` |
| Sector performance | Yahoo Finance (ETFs) | `yfinance` |

---

## Stock & ETF Universe

- **Stocks:** S&P 100 components
- **Sector ETFs:** XLK, XLE, XLV, GDX, XLF, XLI, XLY
- **Broad Market ETFs:** SPY (benchmark), QQQ, IWM
- **Benchmark:** SPY

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/priom-mahatab/stock-radar.git
cd stock-radar
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```
NEWS_API_KEY=your_key_here
FINNHUB_KEY=your_key_here
```

### 5. Run the pipeline

```bash
python pipeline/daily_runner.py
```

---

## Key Design Decisions

**Cache layer:** All market data is cached as CSV files locally. The cache is invalidated after 4:30 PM ET each trading day, ensuring the pipeline always uses the most recent closing data without redundant API calls.

**No circular dependencies:** The cache module never fetches data. The fetcher never caches. Each module has a single responsibility.

**Time-series cross-validation:** The ML model is trained using a time-based train/test split, never a random split, to prevent data leakage from future prices into training.

**Explainable outputs:** Every recommendation includes human-readable reasons derived directly from the features that drove the model's score.

---

## Requirements

```
yfinance
pandas
numpy
scikit-learn
xgboost
lightgbm
vaderSentiment
transformers
requests
python-dotenv
apscheduler
```

---

## Disclaimer

AI Market Radar is a personal learning project. Nothing in this system constitutes financial advice. All outputs are for research and educational purposes only.

---

## License

MIT
```