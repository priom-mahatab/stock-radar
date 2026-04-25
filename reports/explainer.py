from config.settings import VOLUME_SPIKE_THRESHOLD, MOMENTUM_THRESHOLD, SENTIMENT_THRESHOLD, RELATIVE_STRENGTH_THRESHOLD

def explain(ticker, features) -> list[str]:
    reasons = []
    if features["return_5d"] >= MOMENTUM_THRESHOLD:
        reasons.append(f"{ticker}: Strong 5-day return ({features['return_5d']:.1f})")

    if features["volume_spike"] > VOLUME_SPIKE_THRESHOLD:
        reasons.append(f"{ticker}: Unusual volume ({features['volume_spike']:.1%})x 30-day average")

    if features["sentiment_score"] > SENTIMENT_THRESHOLD:
        reasons.append("{ticker}: Positive news sentiment")

    if features["relative_strength"] > RELATIVE_STRENGTH_THRESHOLD:
        reasons.append(f"{ticker}: Outperforming sector by {features['relative_strength']:.1%}")
    
    if not reasons:
        reasons.append("Ranked highly by ML model")

    return reasons
