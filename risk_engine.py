def calculate_risk(fraud_probability):

    risk_score = round(fraud_probability * 100)

    if fraud_probability >= 0.60:
        risk_level = "High Risk"
        decision = "BLOCK"

    elif fraud_probability >= 0.30:
        risk_level = "Medium Risk"
        decision = "REVIEW"

    else:
        risk_level = "Low Risk"
        decision = "APPROVE"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "decision": decision
    }