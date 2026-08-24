from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import shap

from risk_engine import calculate_risk

app = FastAPI(title="AI Risk Manager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/fraud_model_xgb.pkl")
explainer = shap.TreeExplainer(model)

data = pd.read_csv("creditcard.csv")
FEATURE_COLUMNS = [column for column in data.columns if column != "Class"]


class Transaction(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {
        "message": "AI Risk Manager is running"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    if len(transaction.features) != len(FEATURE_COLUMNS):
        return {
            "error": f"Expected {len(FEATURE_COLUMNS)} features",
            "received": len(transaction.features)
        }

    features = pd.DataFrame(
        [transaction.features],
        columns=FEATURE_COLUMNS
    )

    fraud_probability = model.predict_proba(features)[0][1]

    risk = calculate_risk(fraud_probability)

    shap_values = explainer.shap_values(features)

    importance = pd.DataFrame({
        "feature": FEATURE_COLUMNS,
        "impact": shap_values[0]
    })

    importance["absolute_impact"] = importance["impact"].abs()

    importance = importance.sort_values(
        "absolute_impact",
        ascending=False
    )

    risk_factors = []

    for _, row in importance.head(5).iterrows():

        direction = (
            "increased"
            if row["impact"] > 0
            else "decreased"
        )

        risk_factors.append({
            "feature": row["feature"],
            "impact": round(float(row["impact"]), 4),
            "effect": direction
        })

    return {
        "fraud_probability": round(
            float(fraud_probability),
            4
        ),
        "risk_score": risk["risk_score"],
        "risk_level": risk["risk_level"],
        "decision": risk["decision"],
        "risk_factors": risk_factors
    }


@app.get("/demo/{scenario}")
def demo_transaction(scenario: str):

    if scenario not in [
        "normal",
        "suspicious",
        "fraud"
    ]:
        return {
            "error": "Invalid scenario"
        }

    if scenario == "normal":

        candidates = data[data["Class"] == 0]

        features = candidates[FEATURE_COLUMNS]

        probabilities = model.predict_proba(
            features
        )[:, 1]

        candidates = candidates.copy()

        candidates["fraud_probability"] = probabilities

        transaction = candidates.sort_values(
            "fraud_probability",
            ascending=True
        ).iloc[0]

    elif scenario == "suspicious":

        candidates = data[data["Class"] == 0]

        features = candidates[FEATURE_COLUMNS]

        probabilities = model.predict_proba(
            features
        )[:, 1]

        candidates = candidates.copy()

        candidates["fraud_probability"] = probabilities

        suspicious_candidates = candidates[
            (candidates["fraud_probability"] >= 0.30) &
            (candidates["fraud_probability"] < 0.60)
        ]

        if len(suspicious_candidates) == 0:
            return {
                "error": "No suitable suspicious transaction found"
            }

        suspicious_candidates["distance"] = (
            suspicious_candidates["fraud_probability"] - 0.45
        ).abs()

        transaction = suspicious_candidates.sort_values(
            "distance",
            ascending=True
        ).iloc[0]

    else:

        candidates = data[data["Class"] == 1]

        features = candidates[FEATURE_COLUMNS]

        probabilities = model.predict_proba(
            features
        )[:, 1]

        candidates = candidates.copy()

        candidates["fraud_probability"] = probabilities

        transaction = candidates.sort_values(
            "fraud_probability",
            ascending=False
        ).iloc[0]

    features = transaction[
        FEATURE_COLUMNS
    ].tolist()

    return {
        "features": features,
        "actual_class": int(transaction["Class"]),
        "fraud_probability": round(
            float(transaction["fraud_probability"]),
            4
        )
    }