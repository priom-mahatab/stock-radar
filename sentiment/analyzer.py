from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_headlines(headlines: list[str]) -> float:
    analyzer = SentimentIntensityAnalyzer()
    score = 0
    if not headlines:
        return 0.0
    
    for headline in headlines:
        score += analyzer.polarity_scores(headline)["compound"]
    
    return score / len(headlines)
