import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

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

model = joblib.load("models/fraud_model_xgb.pkl")

probabilities = model.predict_proba(X_test)[:, 1]

thresholds = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]

print("\nTHRESHOLD COMPARISON")
print("=" * 80)
print("Threshold | Precision | Recall | F1 | False Positives | False Negatives")
print("-" * 80)

for threshold in thresholds:

    predictions = (probabilities >= threshold).astype(int)

    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    false_positives = ((predictions == 1) & (y_test == 0)).sum()
    false_negatives = ((predictions == 0) & (y_test == 1)).sum()

    print(
        f"{threshold:9.2f} | "
        f"{precision:9.3f} | "
        f"{recall:6.3f} | "
        f"{f1:4.3f} | "
        f"{false_positives:15} | "
        f"{false_negatives:16}"
    )