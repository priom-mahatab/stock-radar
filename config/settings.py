import os
import datetime
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CACHE_FOLDER = os.path.join(BASE_DIR, "data/cache")
REPORTS_FOLDER = os.path.join(BASE_DIR, "reports/output")
MODELS_FOLDER = os.path.join(BASE_DIR, "models/artifacts")

MARKET_CLOSE_HOUR = 16
MARKET_CLOSE_MINUTE = 0
MARKET_TIMEZONE = "America/New_York"

STOCKS_OUTPUT_COUNT = 5
ETF_OUTPUT_COUNT = 2
PRICE_HISTORY_DAYS = 200
CALENDAR_DAYS_FETCH = 300
MARKET_CLOSE_BUFFER_MINUTES = 30
SENTIMENT_WINDOW_DAYS = 3

VOLUME_SPIKE_THRESHOLD = 1.5
MOMENTUM_THRESHOLD = 0.05
SENTIMENT_THRESHOLD = 0.07
RELATIVE_STRENGTH_THRESHOLD = 0.02

load_dotenv()

FINNHUB_KEY = os.getenv("FINNHUB_KEY")

MARKET_HOLIDAYS = {
    datetime.date(2026, 1,  1),   # New Year's Day
    datetime.date(2026, 1, 20),   # MLK Day
    datetime.date(2026, 2, 17),   # Presidents' Day
    datetime.date(2026, 4, 18),   # Good Friday
    datetime.date(2026, 5, 26),   # Memorial Day
    datetime.date(2026, 6, 19),   # Juneteenth
    datetime.date(2026, 7,  4),   # Independence Day
    datetime.date(2026, 9,  1),   # Labor Day
    datetime.date(2026, 11, 27),  # Thanksgiving
    datetime.date(2026, 12, 25),  # Christmas
    datetime.date(2027, 1,  1),   # New Year's Day
    datetime.date(2027, 1, 19),   # MLK Day
    datetime.date(2027, 2, 16),   # Presidents' Day
    datetime.date(2027, 4,  3),   # Good Friday
    datetime.date(2027, 5, 25),   # Memorial Day
    datetime.date(2027, 6, 19),   # Juneteenth
    datetime.date(2027, 7,  3),   # Independence Day (observed)
    datetime.date(2027, 9,  7),   # Labor Day
    datetime.date(2027, 11, 26),  # Thanksgiving
    datetime.date(2027, 12, 25),  # Christmas
}