import joblib
import pandas as pd
import shap

model = joblib.load("models/fraud_model_xgb.pkl")

data = pd.read_csv("creditcard_sample.csv")
feature_columns = [column for column in data.columns if column != "Class"]

sample = data[feature_columns].iloc[[0]]

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(sample)

importance = pd.DataFrame({
    "feature": feature_columns,
    "impact": shap_values[0]
})

importance["absolute_impact"] = importance["impact"].abs()

importance = importance.sort_values(
    "absolute_impact",
    ascending=False
)

print("\nTOP RISK FACTORS")
print("=" * 40)

for _, row in importance.head(5).iterrows():
    direction = "increased" if row["impact"] > 0 else "decreased"

    print(
        f"{row['feature']}: "
        f"{direction} fraud risk "
        f"(impact: {row['impact']:.4f})"
    )