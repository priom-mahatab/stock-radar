from sentiment.aggregator import get_ticker_sentiment

def compute_sentiment_features(ticker) -> dict:
    try:
        if not ticker:
            return None
        
        sentiment_score = get_ticker_sentiment(ticker)
        return {"sentiment_score" : sentiment_score}
    
    except Exception as e:
        print(f"Error computing sentiment for {ticker}: {str(e)}")
        return None