import joblib
import os
from config.settings import MODELS_FOLDER

MODEL_URL = os.path.join(MODELS_FOLDER, "xgb_model.pkl")

def load_model():
    model = joblib.load(MODEL_URL)
    return model

def predict(df):
    model = load_model()
    probability_scores = model.predict_proba(df)[:, 1] # label 0 = did not outperform, label 1 = outperformed, we choose label 1
    df["scores"] = probability_scores
    return df