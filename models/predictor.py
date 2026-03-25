import joblib
MODEL_URL = "./artifacts/xgb_model.pkl"

def load_model():
    model = joblib.load(MODEL_URL)
    return model

def predict(df):
    model = load_model()
    probability_scores = model.predict_proba(df)[:, 1]
    df["scores"] = probability_scores
    return df