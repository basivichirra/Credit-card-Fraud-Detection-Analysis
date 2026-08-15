CREATE DATABASE fraud_project;
USE fraud_project;
CREATE TABLE transactions (
transaction_id INT AUTO_INCREMENT PRIMARY KEY,
transaction_time INT,
amount FLOAT,
v1 FLOAT,
v2 FLOAT,
v3 FLOAT,
v4 FLOAT,
v5 FLOAT,
v6 FLOAT,
v7 FLOAT,
v8 FLOAT,
v9 FLOAT,
v10 FLOAT,
v11 FLOAT,
v12 FLOAT,
v13 FLOAT,
v14 FLOAT,
v15 FLOAT,
v16 FLOAT,
v17 FLOAT,
v18 FLOAT,
v19 FLOAT,
v20 FLOAT,
v21 FLOAT,
v22 FLOAT,
v23 FLOAT,
v24 FLOAT,
v25 FLOAT,
v26 FLOAT,
v27 FLOAT,
v28 FLOAT,
fraud_label INT
);
select count(*) from transactions;
SELECT *
FROM transactions
WHERE amount IS NULL;
SELECT transaction_id, COUNT(*)
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
SELECT
ROUND(SUM(fraud_label)/COUNT(*)*100,4) fraud_rate
FROM transactions;
SELECT
fraud_label,
COUNT(*) transactions
FROM transactions
GROUP BY fraud_label;
SELECT
transaction_id,
amount
FROM transactions
ORDER BY amount DESC
LIMIT 10;
SELECT
FLOOR(transaction_time/3600) hour,
COUNT(*) fraud_cases
FROM transactions
WHERE fraud_label = 1
GROUP BY hour;
SELECT
transaction_id,
amount
FROM transactions
WHERE amount >
(
SELECT AVG(amount)*3 FROM transactions
);
WITH fraud_summary AS (
SELECT
fraud_label,
COUNT(*) transactions
FROM transactions
GROUP BY fraud_label
)

SELECT
fraud_label,
transactions,
ROUND(transactions * 100 /
(SELECT SUM(transactions) FROM fraud_summary),2) percentage
FROM fraud_summary;
SELECT
transaction_id,
amount,
RANK() OVER(ORDER BY amount DESC) AS transaction_rank
FROM transactions
LIMIT 10;
SELECT
transaction_id,
amount,
AVG(amount) OVER() AS overall_avg
FROM transactions
LIMIT 10;
SELECT
transaction_id,
amount,
CASE
WHEN amount > 2000 THEN 'High Risk'
WHEN amount BETWEEN 500 AND 2000 THEN 'Medium Risk'
ELSE 'Low Risk'
END AS risk_level
FROM transactions;
CREATE VIEW fraud_summary_view AS
SELECT
fraud_label,
COUNT(*) transactions
FROM transactions
GROUP BY fraud_label;