from models.trainer import build_training_data, train_model
from models.predictor import predict
from models.ranker import ranker
from features.feature_pipeline import build_feature_matrix
from config.settings import CACHE_FOLDER
from data.storage.cache import MarketCache
from data.ingestion.market_data import MarketData

# build training data and train model
market_cache = MarketCache(CACHE_FOLDER)
market_data = MarketData(market_cache)
training_df = build_training_data(market_data)
model = train_model(training_df)

# run today's prediction
feature_matrix = build_feature_matrix(market_data)
scored_df = predict(feature_matrix)
top_stocks, top_etfs = ranker(scored_df)

print(top_stocks)
print(top_etfs)