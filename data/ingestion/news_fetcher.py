import requests
import time
from datetime import datetime, timedelta
from config.settings import SENTIMENT_WINDOW_DAYS, FINNHUB_KEY

def fetch_news(ticker, cache) -> list[str]:

    if cache.is_valid(ticker, "news"):
        df = cache.load(ticker, "news")
        return df["headline"].tolist()

    now = datetime.today()
    past_date = now - timedelta(days=SENTIMENT_WINDOW_DAYS)
    url = "https://finnhub.io/api/v1/company-news"
    params= {
        'symbol': ticker,
        'from': past_date.strftime("%Y-%m-%d"),
        'to': now.strftime("%Y-%m-%d"),
        'token': FINNHUB_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json()
        headlines = [article["headline"] for article in articles]
        time.sleep(1.0)
        return headlines
    else:
        print(f"Failed to fetch news for {ticker}: {response.status_code}")
        return []
