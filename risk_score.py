from datetime import datetime


def calculate_risk(transaction, probability):
    """
    Calculate risk score based on ML probability and business rules.
    """

    # -------------------------
    # Base Score from ML Model
    # -------------------------
    score = probability * 50

    # -------------------------
    # Extract Transaction Hour
    # -------------------------
    try:
        if isinstance(transaction["transaction_time"], datetime):
            hour = transaction["transaction_time"].hour
        else:
            hour = datetime.strptime(
                str(transaction["transaction_time"]),
                "%Y-%m-%d %H:%M:%S"
            ).hour
    except Exception:
        hour = 12  # Default (daytime)

    # -------------------------
    # Business Rules
    # -------------------------
    if transaction["amount"] > 50000:
        score += 20

    if transaction["vendor"] == "Unknown":
        score += 10

    if transaction["device_type"] == "Unknown Device":
        score += 5

    if transaction["previous_transactions"] < 5:
        score += 5

    if hour >= 22 or hour <= 5:
        score += 5

    if transaction["location"] in ["Delhi", "Bangalore"]:
        score += 5

    # Maximum score = 100
    score = min(100, round(score))

    # -------------------------
    # Decision Engine
    # -------------------------
    if score >= 80:
        decision = "BLOCK"
    elif score >= 50:
        decision = "VERIFY (OTP)"
    else:
        decision = "APPROVE"

    # -------------------------
    # Explainability
    # -------------------------
    reasons = []

    if transaction["amount"] > 50000:
        reasons.append("High transaction amount")

    if transaction["vendor"] == "Unknown":
        reasons.append("Unknown vendor")

    if transaction["device_type"] == "Unknown Device":
        reasons.append("Unknown device")

    if transaction["previous_transactions"] < 5:
        reasons.append("Low previous transactions")

    if hour >= 22 or hour <= 5:
        reasons.append("Night transaction")

    if transaction["location"] in ["Delhi", "Bangalore"]:
        reasons.append("Risky location")

    if len(reasons) == 0:
        reasons.append("Normal transaction")

    return {
        "risk_score": score,
        "decision": decision,
        "reasons": reasons
    }


# -------------------------
# Test
# -------------------------
if __name__ == "__main__":

    sample = {
        "transaction_time": "2024-07-20 23:15:00",
        "amount": 85000,
        "vendor": "Unknown",
        "location": "Delhi",
        "device_type": "Unknown Device",
        "previous_transactions": 2
    }

    probability = 0.95

    result = calculate_risk(sample, probability)

    print("\n========== RESULT ==========")
    print("Risk Score :", result["risk_score"])
    print("Decision   :", result["decision"])
    print("Reasons    :")
    for reason in result["reasons"]:
        print("-", reason)