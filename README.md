# AI Risk Manager

AI-powered credit card fraud detection and risk analysis system using XGBoost, FastAPI, SHAP explainability, and an interactive web dashboard.

## Overview

AI Risk Manager analyzes credit card transactions and estimates the probability of fraud.

The system converts the model prediction into an easy-to-understand risk decision:

- Low Risk → APPROVE
- Medium Risk → REVIEW
- High Risk → BLOCK

It also provides the top factors influencing each prediction using SHAP explainability.

## Features

- Credit card fraud detection
- XGBoost machine learning model
- Fraud probability prediction
- Risk score from 0–100
- Automated risk classification
- APPROVE / REVIEW / BLOCK decisions
- SHAP-based risk factor explanation
- FastAPI REST API
- Interactive web dashboard
- Real transaction demo scenarios
- Recent transaction history
- Normal, suspicious, and fraudulent transaction testing

## Machine Learning

The project uses the Credit Card Fraud Detection dataset.

Dataset size:

- Total transactions: 284,807
- Legitimate transactions: 284,315
- Fraudulent transactions: 492

### Model

The final prediction model is XGBoost.

Model evaluation:

- PR-AUC: 0.8731

Confusion Matrix:

```text
[[56857     7]
 [   18    80]]

The model is designed for highly imbalanced fraud detection data.

## Risk Engine

The predicted fraud probability is converted into a risk score and decision.

| Fraud Probability | Risk Level | Decision |
|---|---|---|
| < 30% | Low Risk | APPROVE |
| 30% – 59% | Medium Risk | REVIEW |
| ≥ 60% | High Risk | BLOCK |

## Explainability

SHAP is used to explain individual predictions.

Example:

```text
TOP RISK FACTORS

V14 → increased fraud risk
V10 → increased fraud risk
V12 → increased fraud risk
V26 → decreased fraud risk
V4 → increased fraud risk.
```

## Project Structure

```text
Credit-card-Fraud-Detection-Analysis/
│
├── dashboard/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   ├── fraud_model_xgb.pkl
│   ├── fraud_model.pkl
│   ├── scaler_full.pkl
│   └── scaler.pkl
│
├── main.py
├── risk_engine.py
├── explain_prediction.py
├── fraud_detection_model.py
├── predict_transaction.py
├── train_xgboost.py
├── train_full_model.py
├── evaluate_xgboost.py
├── evaluate_full_model.py
├── evaluate_model.py
├── threshold_tuning.py
├── test_risk_engine.py
├── fraud_analysis.sql
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset

The full `creditcard.csv` dataset is not included in the repository because of its large file size.

Place the downloaded dataset in the project root as:

```text
creditcard.csv
```

## Run the API

```bash
uvicorn main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Health Check

```text
GET /
```

### Predict Transaction

```text
POST /predict
```

Example:

```json
{
  "fraud_probability": 0.9889,
  "risk_score": 99,
  "risk_level": "High Risk",
  "decision": "BLOCK"
}
```

### Demo Transactions

```text
GET /demo/normal
GET /demo/suspicious
GET /demo/fraud
```

These endpoints select real transactions from the dataset for demonstration.

## Dashboard

Open:

```text
dashboard/index.html
```

The dashboard provides:

- Fraud probability
- Risk score
- Risk level
- Decision
- Transaction amount
- Transaction time
- Normal payment demo
- Suspicious payment demo
- Fraudulent payment demo
- Top SHAP risk factors
- Recent transaction history

## Technologies

- Python
- Pandas
- Scikit-learn
- XGBoost
- SHAP
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript
- SQL

## Project Goal

The goal of AI Risk Manager is to demonstrate how machine learning can be integrated into a practical fraud detection and risk management system.

Instead of only returning a fraud prediction, the system provides an actionable decision and an explanation of the factors influencing the prediction.

## Disclaimer

This project is for educational and demonstration purposes and should not be used as a production financial fraud detection system without additional validation, security, monitoring, and compliance controls.