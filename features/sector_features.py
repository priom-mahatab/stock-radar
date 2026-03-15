import pandas as pd

def compute_sector_features(ticker, df, sector_df) -> dict:
    try:
        closing_price = df["Close"]
        sector_closing_price = sector_df["Close"]
        return_5d = (closing_price - closing_price.shift(5)) / closing_price.shift(5)
        sector_momentum = (sector_closing_price - sector_closing_price.shift(5)) / sector_closing_price.shift(5)
        relative_strength = return_5d - sector_momentum

        features = {
            "ticker": ticker,
            "sector_momentum": sector_momentum.iloc[-1],
            "relative_strength": relative_strength.iloc[-1]
        }

        return features

    except Exception as e:
        print(f"Error computing features for {ticker}: {str(e)}")
        return None
