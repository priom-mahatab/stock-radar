from features.feature_pipeline import build_feature_matrix
from config.settings import CACHE_FOLDER
from data.storage.cache import MarketCache
from data.ingestion.market_data import MarketData
from models.predictor import predict
from models.trainer import build_training_data, train_model
from models.ranker import ranker
from reports.formatter import format_report

def main():
    market_cache = MarketCache(CACHE_FOLDER)
    market_data = MarketData(market_cache)

    training_df = build_training_data(market_data)
    train_model(training_df)

    feature_matrix = build_feature_matrix(market_data)
    scored_df = predict(feature_matrix)
    top_stocks, top_etfs = ranker(scored_df)

    result = format_report(top_stocks, top_etfs)
    print(result)

if __name__ == "__main__":
    main()

