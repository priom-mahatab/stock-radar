from reports.explainer import explain
import datetime
import os
from config.settings import REPORTS_FOLDER

def format_report(top_stocks, top_etfs) -> str:
    filename = os.path.join(REPORTS_FOLDER, f"{datetime.date.today()}.md")

    report = []
    report.append("AI Market Radar")
    report.append(f"Date: {datetime.date.today()}")
    report.append("\nTop stocks to research:")

    for ticker, row in top_stocks.iterrows():
        report.extend(explain(ticker, row))

    report.append("\nTop ETFs to watch:")
    for etf, row in top_etfs.iterrows():
        report.append(f"\t- {etf}")

    result = "\n".join(report)

    with open(filename, "w") as f:
        f.write(result)

    return result
