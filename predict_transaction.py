import joblib
import pandas as pd

from risk_engine import calculate_risk

model = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")

data = pd.read_csv("creditcard_sample.csv")

X = data.drop("Class", axis=1)

sample = X.iloc[[0]]

sample_scaled = scaler.transform(sample)

fraud_probability = model.predict_proba(sample_scaled)[0][1]

risk = calculate_risk(fraud_probability)

print("Fraud Probability:", round(fraud_probability, 4))
print("Risk Score:", risk["risk_score"])
print("Risk Level:", risk["risk_level"])
print("Decision:", risk["decision"])