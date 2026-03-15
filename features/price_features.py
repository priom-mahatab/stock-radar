import pandas as pd

def compute_price_features(ticker, df) -> dict:
    try :
        closing_price = df["Close"]
        return_1d = (closing_price - closing_price.shift(1)) / closing_price.shift(1)
        return_5d = (closing_price - closing_price.shift(5)) / closing_price.shift(5)
        return_20d = (closing_price - closing_price.shift(20)) / closing_price.shift(20)
        distance_50ma = (closing_price - closing_price.rolling(window=50).mean()) / closing_price.rolling(window=50).mean()
        volatility = return_1d.rolling(window=20).std()

        features = {
            "ticker": ticker,
            "return_1d": return_1d.iloc[-1],
            "return_5d": return_5d.iloc[-1],
            "return_20d": return_20d.iloc[-1],
            "distance_50ma": distance_50ma.iloc[-1],
            "volatility": volatility.iloc[-1]
        }

        return features
    except Exception as e:
        print(f"Error computing features for {ticker}: {str(e)}")
        return None