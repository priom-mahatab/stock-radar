from sentiment.analyzer import analyze_headlines
from data.ingestion.news_fetcher import fetch_news

def get_ticker_sentiment(ticker, cache) -> float:
    """Fetches recent news for a ticker and returns its average sentiment score.

    Returns a compound VADER score in [-1.0, +1.0], or 0.0 if no news is found.
    """
    headlines = fetch_news(ticker, cache)
    score = analyze_headlines(headlines)

    return score