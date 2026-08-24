import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(
    max_iter=10000,
    class_weight="balanced"
)

model.fit(X_train_scaled, y_train)

joblib.dump(model, "models/fraud_model_full.pkl")
joblib.dump(scaler, "models/scaler_full.pkl")

print("Full dataset model trained successfully")
print("Model saved successfully")
print("Scaler saved successfully")