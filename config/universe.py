SP100_TICKERS = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "BRK-B", "LLY",
    "AVGO", "TSLA", "WMT", "JPM", "V", "UNH", "XOM", "ORCL", "MA",
    "COST", "HD", "PG", "JNJ", "ABBV", "BAC", "KO", "MRK", "CVX",
    "CRM", "NFLX", "AMD", "PEP", "TMO", "ACN", "LIN", "MCD", "CSCO",
    "ABT", "GE", "DHR", "TXN", "AXP", "PM", "ADBE", "IBM", "CAT",
    "GS", "INTU", "ISRG", "QCOM", "VZ", "RTX", "SPGI", "T", "PFE",
    "NEE", "AMGN", "BLK", "HON", "CMCSA", "UNP", "LOW", "DE", "NOW",
    "SYK", "MS", "C", "BMY", "BKNG", "GILD", "CI", "PLD", "TJX",
    "UPS", "SO", "DUK", "ZTS", "AON", "CL", "REGN", "CME",
    "BSX", "BDX", "EOG", "MO", "MDLZ", "ETN", "ITW", "HCA", "WM",
    "FCX", "PSA", "APD", "MCO", "USB", "PNC", "TGT", "EMR", "NSC", "SHW",
]

SECTOR_ETFS = {
    # Your requested sectors
    "XLK":  ("Technology Select Sector SPDR",       "technology"),
    "XLE":  ("Energy Select Sector SPDR",            "energy"),
    "XLV":  ("Health Care Select Sector SPDR",       "healthcare"),
    "GDX":  ("VanEck Gold Miners ETF",               "metals_mining"),  # Gold/metal miners

    # High-prominence broad market ETFs
    "SPY":  ("SPDR S&P 500 ETF",                     "broad_market"),   # Benchmark — always include
    "QQQ":  ("Invesco Nasdaq-100 ETF",               "tech_growth"),    # Nasdaq-heavy, high signal
    "IWM":  ("iShares Russell 2000 ETF",             "small_cap"),      # Small cap risk appetite

    # Additional prominent sector ETFs worth tracking
    "XLF":  ("Financial Select Sector SPDR",         "financials"),     # Banks, insurance
    "XLI":  ("Industrial Select Sector SPDR",        "industrials"),    # Defense, manufacturing
    "XLU":  ("Utilities Select Sector SPDR",          "utilities"),      # Utilities, infrastructure
    "XLY":  ("Consumer Discretionary Select Sector", "consumer_disc"),  # Retail, autos

    "XLP":  ("Consumer Staples Select Sector SPDR", "consumer_staples"),  # Food, beverages
    "XLB":  ("Materials Select Sector SPDR",         "materials"),      # Chemicals, metals (non-gold)
    "XLC":  ("Communication Services Select Sector SPDR", "communication"),  # Telecom, media
    "XLRE": ("Real Estate Select Sector SPDR",      "real_estate"),     # REITs, real estate
}


SECTOR_MAPPING = {
    "XLK": [  # Technology
        "AAPL", "MSFT", "NVDA", "AVGO", "ORCL", "CRM", "AMD", "ADBE",
        "CSCO", "TXN", "QCOM", "IBM", "INTU", "NOW", "ACN"
    ],
    "XLV": [  # Health Care
        "LLY", "UNH", "JNJ", "ABBV", "MRK", "TMO", "ABT", "DHR", "PFE", "HCA",
        "AMGN", "ISRG", "SYK", "BMY", "GILD", "CI", "BSX", "BDX", "REGN", "ZTS"
    ],
    "XLU": [  # Utilities
        "NEE", "SO", "DUK"
    ],
    "XLF": [  # Financials
        "BRK-B", "JPM", "V", "MA", "BAC", "GS", "MS", "SPGI",
        "BLK", "CME", "USB", "PNC", "AON", "MCO", "AXP", "C"
    ],
    "XLE": [  # Energy
        "XOM", "CVX", "EOG"
    ],
    "XLI": [  # Industrials
        "DE", "GE", "HON", "UNP", "RTX", "CAT", "ETN", "ITW", "EMR", "NSC", "UPS", "WM"
    ],
    "XLY": [  # Consumer Discretionary
        "AMZN", "TSLA", "MCD", "BKNG", "TJX", "LOW", "HD", "NKE", "TGT"
    ],
    "XLP": [  # Consumer Staples (using XLP as proxy)
        "WMT", "PG", "KO", "PEP", "COST", "PM", "MDLZ", "CL", "MO"
    ],
    "XLB": [  # Materials (using XLB as proxy, GDX too narrow for these)
        "LIN", "APD", "SHW", "FCX"
    ],
    "XLC": [  # Communication Services (using XLC as proxy)
        "GOOGL", "META", "NFLX", "CMCSA", "T", "VZ"
    ],
    "XLRE": [  # Real Estate (using XLRE as proxy)
        "PLD", "PSA"
    ],
}

# --- WATCHLIST ETFs ---
# These are the ETFs the system can RECOMMEND (output)
# Separate from SECTOR_ETFS which are used as *features/signals*
RECOMMENDABLE_ETFS = ["SPY", "QQQ", "IWM", "GDX", "XLK", "XLE", "XLV", "XLF", "XLY", "XLP", "XLB", "XLC", "XLRE"]

# Used to compute relative performance for all stocks
BENCHMARK = "SPY"