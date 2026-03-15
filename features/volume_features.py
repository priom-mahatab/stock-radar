import pandas as pd

def compute_volume_features(ticker, df) -> dict:
    try:
        volume = df["Volume"]
        volume_spike = volume / volume.rolling(window=30).mean()
        relative_volume = volume / volume.rolling(window=5).mean()


        features = {
            "ticker": ticker,
            "volume_spike": volume_spike.iloc[-1],
            "relative_volume": relative_volume.iloc[-1]
        }

        return features
    
    except Exception as e:
        print(f"Error computing features for {ticker}: {str(e)}")
        return None