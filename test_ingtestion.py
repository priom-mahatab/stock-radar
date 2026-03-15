from config.settings import CACHE_FOLDER
from data.storage.cache import MarketCache
from config.universe import SP100_TICKERS
from data.ingestion.market_data import MarketData
from data.validation import validate_price_df

market_cache = MarketCache(CACHE_FOLDER)
market_data = MarketData(market_cache)
success = []
fails = []

for ticker in SP100_TICKERS:
    try:
        data = market_data.get_price_data(ticker)
        valid_data = validate_price_df(ticker, data)
        if valid_data:
            success.append(ticker)
        else:
            fails.append((ticker, "Invalid data"))

    except Exception as e:
        fails.append((ticker, str(e)))
        continue


print(f"Successful tickers: {len(success)}")
print(f"Unsuccessful tickers: {len(fails)}")
for fail in fails:
    print(f"{fail[0]} failed because of {fail[1]}")



