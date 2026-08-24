from risk_engine import calculate_risk

tests = [0.10, 0.55, 0.90]

for probability in tests:
    result = calculate_risk(probability)
    print(f"Probability: {probability}")
    print(result)
    print()