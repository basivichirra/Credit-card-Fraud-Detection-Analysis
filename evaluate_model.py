import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, average_precision_score

data = pd.read_csv("creditcard_sample.csv")

data = data.dropna()

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

predictions = model.predict(X_test_scaled)

fraud_probability = model.predict_proba(X_test_scaled)[:, 1]

print("\nMODEL EVALUATION")
print("=" * 50)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

pr_auc = average_precision_score(y_test, fraud_probability)

print("\nPR-AUC:", round(pr_auc, 4))