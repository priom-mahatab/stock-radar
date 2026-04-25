from config.universe import SECTOR_MAPPING, SP100_TICKERS
import pandas as pd
import xgboost as xgb
import joblib
import os
from config.settings import MODELS_FOLDER

# Path where the trained model will be persisted
MODEL_URL = os.path.join(MODELS_FOLDER, "xgb_model.pkl")

from features.price_features import compute_price_features
from features.sector_features import compute_sector_features
from features.volume_features import compute_volume_features
from features.sentiment_features import compute_sentiment_features

def build_training_data(market_data):
    # Build a reverse lookup from ticker -> sector ETF
    ticker_to_sector = {}
    for etf, tickers in SECTOR_MAPPING.items():
        for ticker in tickers:
            ticker_to_sector[ticker] = etf
    results = []
    # SPY is used as the market benchmark for computing relative labels
    spy_df = market_data.get_price_data("SPY")

    for ticker in SP100_TICKERS:
        data = market_data.get_price_data(ticker)
        sector = ticker_to_sector.get(ticker)
        sector_df = market_data.get_price_data(sector)
        # Sentiment features are ticker-level and don't vary by date, so compute once
        sentiment_features = compute_sentiment_features(ticker, market_data.cache) or {}

        # Exclude the last 5 dates since we need a 5-day forward window for labeling
        dates = data.index[:-5]
        for date in dates:
            # The label horizon: the 5 trading days immediately after the current date
            label_dates = data.index[data.index > date][:5]
            # Only use data up to and including the current date to avoid lookahead
            df_slice = data[data.index <= date]
            sector_df_slice = sector_df[sector_df.index <= date]
            price_features = compute_price_features(ticker, df_slice)
            volume_features = compute_volume_features(ticker, df_slice)
            sector_features = compute_sector_features(ticker, df_slice, sector_df_slice)
            start_price = data.loc[date, "Close"]
            end_price = data.loc[label_dates[-1], "Close"]
            stock_return = (end_price - start_price) / start_price
            # SPY return over the same 5-day window, used as the outperformance threshold
            spy_return = spy_df.loc[label_dates[-1], "Close"] / spy_df.loc[date, "Close"] - 1
            # Label is 1 if the stock both outperforms SPY and has a positive absolute return
            label = 1 if stock_return > spy_return and stock_return > 0 else 0

            if price_features and volume_features and sector_features:
                # Merge all feature groups; sentiment features may be empty if unavailable
                features = {**price_features, **volume_features, **sector_features, **(sentiment_features or {})}
                features["date"] = date
                features["label"] = label
                results.append(features)

    return pd.DataFrame(results).set_index(["date", "ticker"])


def train_model(df):
    # Chronological 80/20 train-test split to prevent future data leaking into training
    dates = df.index.get_level_values("date").unique().sort_values()
    cutoff = dates[int(len(dates) * 0.8)]
    train = df[df.index.get_level_values("date") <= cutoff]
    test = df[df.index.get_level_values("date") > cutoff]
    X_train = train.drop(columns=["label"])
    y_train = train["label"]
    X_test = test.drop(columns=["label"])
    y_test = test["label"]

    model = xgb.XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
    # lstm
    model.fit(X_train, y_train)

    print("Model evaluation:" + str(model.score(X_test, y_test)))
    # Persist the trained model so it can be loaded for inference without retraining
    joblib.dump(model, MODEL_URL)

    return model
