import datetime
from config.settings import MARKET_HOLIDAYS

def get_last_valid_trading_date(lookback=0):
        valid_date = datetime.date.today()
        while (valid_date in MARKET_HOLIDAYS) or (valid_date.weekday() > 4):
            valid_date = valid_date - datetime.timedelta(days=1)
        for _ in range(lookback):
            valid_date -= datetime.timedelta(days=1)
            while (valid_date in MARKET_HOLIDAYS) or (valid_date.weekday() > 4):
                valid_date -= datetime.timedelta(days=1)
        return valid_date