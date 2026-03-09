from config.settings import PRICE_HISTORY_DAYS
from utils import get_last_valid_trading_date
import pandas as pd

def validate_price_df(ticker, df) -> bool:
    row_count = df.shape[0]
    if (row_count < PRICE_HISTORY_DAYS):
        print(f"{row_count} cannot be less than {PRICE_HISTORY_DAYS}")
        return False
    
    if (df.isnull().values.any()):
        print(f"Data contains null values")
        return False
    
    most_recent_date = pd.to_datetime(df.index).max().date()
    if (most_recent_date < get_last_valid_trading_date()):
        print(f"Most recent data is outdated")
        return False
    
    return True