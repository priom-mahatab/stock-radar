import os
from zoneinfo import ZoneInfo
import pandas as pd
import datetime
from config.settings import MARKET_CLOSE_HOUR
from config.settings import MARKET_CLOSE_BUFFER_MINUTES
from config.settings import MARKET_HOLIDAYS
from utils import get_last_valid_trading_date

class MarketCache:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.prices_path = os.path.join(self.base_dir, "prices")
        self.news_path = os.path.join(self.base_dir, "news")

        os.makedirs(self.prices_path, exist_ok=True)
        os.makedirs(self.news_path, exist_ok=True)

    def _get_file_path(self, ticker, data_type):
        if data_type == "prices":
            folder = self.prices_path
        elif data_type == "news":
            folder = self.news_path
        
        else:
            raise ValueError(f'{data_type} is invalid')

        desired_path = os.path.join(folder, f"{ticker}.csv")
        return desired_path
        
    def save(self, ticker, data_type, df):
        file_path = self._get_file_path(ticker, data_type)
        df.to_csv(file_path)

    def load(self, ticker, data_type):
        file_path = self._get_file_path(ticker, data_type)
        if not (os.path.exists(file_path)):
            raise FileNotFoundError(f"Cache file not found: {file_path}")
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        return df

    def is_valid(self, ticker, data_type):
        file_path = self._get_file_path(ticker, data_type)
        if not os.path.exists(file_path):
            return False
    
        df = self.load(ticker, data_type)
        most_recent_date = pd.to_datetime(df.index).max().date()
        ny_time = datetime.datetime.now(ZoneInfo("America/New_York"))

        if ny_time.hour > MARKET_CLOSE_HOUR or (ny_time.hour == MARKET_CLOSE_HOUR and ny_time.minute >= MARKET_CLOSE_BUFFER_MINUTES):
            return most_recent_date == datetime.date.today()
        
        return most_recent_date == get_last_valid_trading_date()
        