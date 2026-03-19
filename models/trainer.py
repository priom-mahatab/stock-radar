from config.universe import SECTOR_MAPPING, SP100_TICKERS
import pandas as pd
import xgboost as xgb
import joblib
from features.price_features import compute_price_features
from features.sector_features import compute_sector_features
from features.volume_features import compute_volume_features

def build_training_data(market_data):
    
    ticker_to_sector = {}
    for etf, tickers in SECTOR_MAPPING.items():
        for ticker in tickers:
            ticker_to_sector[ticker] = etf
    results = []
    spy_df = market_data.get_price_data("SPY")

    for ticker in SP100_TICKERS:
        data = market_data.get_price_data(ticker)
        sector = ticker_to_sector.get(ticker)
        sector_df = market_data.get_price_data(sector)
        dates = data.index[:-5]
        for date in dates:
            label_dates = data.index[data.index > date][:5]
            df_slice = data[data.index <= date]
            sector_df_slice = sector_df[sector_df.index <= date]
            price_features = compute_price_features(ticker, df_slice)
            volume_features = compute_volume_features(ticker, df_slice)        
            sector_features = compute_sector_features(ticker, df_slice, sector_df_slice)

            start_price = data.loc[date, "Close"] # Get the closing price on the current date
            end_price = data.loc[label_dates[-1], "Close"] # Get the closing price 5 days after the current date
            stock_return = (end_price - start_price) / start_price
            spy_return = spy_df.loc[label_dates[-1], "Close"] / spy_df.loc[date, "Close"] - 1 # Calculate SPY return over the same period
            label = 1 if stock_return > spy_return and stock_return > 0 else 0

            if price_features and volume_features and sector_features:
                features = {**price_features, **volume_features, **sector_features} # Combine all features into a single dictionary
                features["date"] = date
                features["label"] = label
                results.append(features)

    return pd.DataFrame(results).set_index(["date", "ticker"])


def train_model(df):
    dates = df.index.get_level_values("date").unique().sort_values()
    cutoff = dates[int(len(dates) * 0.8)]
    train = df[df.index.get_level_values("date") <= cutoff]
    test = df[df.index.get_level_values("date") > cutoff]
    X_train = train.drop(columns=["label"])
    y_train = train["label"]
    X_test = test.drop(columns=["label"])
    y_test = test["label"]

    model = xgb.XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)

    print("Model evaluation:" + str(model.score(X_test, y_test)))
    joblib.dump(model, 'models/artifacts/xgb_model.pkl')

    return model