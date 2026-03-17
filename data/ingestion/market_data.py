from config.settings import PRICE_HISTORY_DAYS, CALENDAR_DAYS_FETCH
import yfinance as yf
import datetime as dt

class MarketData:
    def __init__(self, cache):
        self.cache = cache

    
    def get_price_data(self, ticker):
        if self.cache.is_valid(ticker, "prices"):
            return self.cache.load(ticker, "prices")
        else:
            price_data = yf.download(tickers=ticker, start=dt.date.today() - dt.timedelta(days=CALENDAR_DAYS_FETCH), end=dt.date.today() + dt.timedelta(days=1), multi_level_index=False, auto_adjust=True)
            self.cache.save(ticker, "prices", price_data)
            return price_data