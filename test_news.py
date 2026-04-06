from data.ingestion.news_fetcher import fetch_news

headlines = fetch_news("AAPL")
print(headlines)