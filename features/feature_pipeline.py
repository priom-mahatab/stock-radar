import pandas as pd
from config.universe import SP100_TICKERS, RECOMMENDABLE_ETFS, SECTOR_MAPPING
from features.price_features import compute_price_features
from features.volume_features import compute_volume_features
from features.sector_features import compute_sector_features
from data.validation import validate_price_df

def build_feature_matrix(market_data) -> pd.DataFrame:

    features = []
    
    ticker_to_sector = {}
    for etf, tickers in SECTOR_MAPPING.items():
        for ticker in tickers:
            ticker_to_sector[ticker] = etf
    
    for ticker in SP100_TICKERS:
        price = market_data.get_price_data(ticker)
        if validate_price_df(ticker, price):
            price_features = compute_price_features(ticker, price)
            volume_features = compute_volume_features(ticker, price)
            sector = ticker_to_sector.get(ticker)
            if not sector:
                combined = {**price_features, **volume_features}
                features.append(combined)
                continue
            sector_price = market_data.get_price_data(sector)
            sector_features = compute_sector_features(ticker, price, sector_price)

            combined = {**price_features, **volume_features, **sector_features}
            features.append(combined)
    
    for ticker in RECOMMENDABLE_ETFS:
        price = market_data.get_price_data(ticker)
        if validate_price_df(ticker, price):
            price_features = compute_price_features(ticker, price)
            volume_features = compute_volume_features(ticker, price)

            combined = {**price_features, **volume_features}
            features.append(combined)

    if not features:
        raise ValueError("No tickers passed validation — feature matrix is empty.")
    return pd.DataFrame(features).set_index("ticker")
    