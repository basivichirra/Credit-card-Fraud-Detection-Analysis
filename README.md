
# AI-Powered Fraud Detection Analysis

## Project Overview
This project analyzes financial transactions and detects fraudulent activity using SQL, Machine Learning, and Power BI dashboards.

The goal of the project is to identify fraud patterns, predict high-risk transactions, and visualize fraud insights through an interactive dashboard.

---

## Tools & Technologies

- Python
- SQL
- Power BI
- Machine Learning
- Data Visualization

Python was used for model development, SQL for transaction analysis, and the dashboard was built in :contentReference[oaicite:0]{index=0}.

---

## Dataset

The dataset used in this project is the **Credit Card Fraud Detection Dataset**.

Total Transactions: 284,807  
Fraudulent Transactions: 492  

Due to GitHub file size limitations, only a sample dataset is included in this repository.

Full dataset available at:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Dataset Features:
- Time
- Transaction Amount
- PCA transformed features (V1–V28)
- Class (0 = Normal, 1 = Fraud)

---

## Project Workflow

1. Data exploration using SQL
2. Fraud pattern analysis
3. Machine learning fraud prediction
4. Fraud probability calculation
5. Power BI dashboard visualization

---

## Machine Learning Model

The fraud prediction model was built using  
:contentReference[oaicite:1]{index=1} in :contentReference[oaicite:2]{index=2}.

Steps included:
- Data preprocessing
- Train-test split
- Model training
- Fraud probability prediction
- Risk classification

Model Accuracy:
~99%

---

## Power BI Dashboard

The dashboard provides an overview of fraud patterns and AI predictions.

Dashboard Features:

Fraud Analytics Overview
- Fraud vs Normal Transactions
- Transaction Amount Distribution
- Fraud Transactions Over Time
- Risk Category Analysis

AI Fraud Detection
- Fraud Probability Distribution
- Risk Level Distribution
- Predicted vs Actual Fraud
- High Risk Transaction Identification

## Power BI Dashboard Preview

### Fraud Analytics Overview
![Dashboard](images/dashboard_overview.png)

### AI Fraud Detection
![Dashboard](images/ai_fraud_dashboard.png)
---

## Repository Structure
fraud-detection-analytics
│
├── dataset
│ └── creditcard_sample.csv

├── python
│ └── fraud_detection_model.py

├── sql
│ └── fraud_analysis.sql

├── results
│ └── fraud_predictions_sample.csv

├── images
│ └── dashboard_preview.png

└── README.md


---

## Key Insights

- Fraud transactions represent only ~0.17% of total transactions.
- High-value transactions tend to have higher fraud probability.
- Most transactions fall into the low-risk category.
- The machine learning model successfully identifies fraudulent activity with high accuracy.

---

## Author
Thanuj Reddy Gopu  
Data Analyst / Machine Learning Enthusiast
