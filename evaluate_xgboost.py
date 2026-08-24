import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, average_precision_score

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

predictions = model.predict(X_test)

fraud_probability = model.predict_proba(X_test)[:, 1]

print("\nXGBOOST MODEL EVALUATION")
print("=" * 50)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

pr_auc = average_precision_score(y_test, fraud_probability)

print("\nPR-AUC:", round(pr_auc, 4))