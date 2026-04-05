from config.settings import STOCKS_OUTPUT_COUNT, ETF_OUTPUT_COUNT
from config.universe import RECOMMENDABLE_ETFS

def ranker(df):
    etf_mask = df.index.isin(RECOMMENDABLE_ETFS)
    etfs = df[etf_mask]
    stocks = df[~etf_mask]

    stocks = stocks.sort_values("score", ascending=False)
    etfs = etfs.sort_values("score", ascending=False)

    top_stocks = stocks.head(STOCKS_OUTPUT_COUNT)
    top_etfs = etfs.head(ETF_OUTPUT_COUNT)

    return top_stocks, top_etfs