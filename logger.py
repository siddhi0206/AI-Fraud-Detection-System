import os
import pandas as pd
from datetime import datetime

LOG_FILE = "prediction_logs.csv"

columns = [
    "timestamp",
    "customer_id",
    "amount",
    "vendor",
    "location",
    "prediction",
    "probability",
    "risk_score",
    "decision"
]

if not os.path.exists(LOG_FILE):
    pd.DataFrame(columns=columns).to_csv(LOG_FILE, index=False)


def log_transaction(
        transaction,
        prediction,
        probability,
        risk,
        decision
):

    row = {
        "timestamp": datetime.now(),
        "customer_id": transaction["customer_id"],
        "amount": float(transaction["amount"]),
        "vendor": transaction["vendor"],
        "location": transaction["location"],
        "prediction": int(prediction),
        "probability": round(float(probability) * 100, 2),
        "risk_score": int(risk["risk_score"]),   
        "decision": decision
    }

    df = pd.read_csv(LOG_FILE)

    df = pd.concat(
        [df, pd.DataFrame([row])],
        ignore_index=True
    )

    df.to_csv(LOG_FILE, index=False)