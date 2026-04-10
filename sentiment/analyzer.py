from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_headlines(headlines: list[str]) -> float:
    """Returns the average VADER compound sentiment score across all headlines.

    Compound score ranges from -1.0 (most negative) to +1.0 (most positive).
    Returns 0.0 if no headlines are provided.
    """
    analyzer = SentimentIntensityAnalyzer()
    score = 0
    if not headlines:
        return 0.0

    for headline in headlines:
        # Compound score is a normalized aggregate of positive, negative, and neutral scores
        score += analyzer.polarity_scores(headline)["compound"]

    # Average across all headlines to smooth out individual outliers
    return score / len(headlines)
