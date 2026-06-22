import joblib
import pandas as pd
from feature_engineering import create_features

# -----------------------------
# Load Saved Models
# -----------------------------

rf_model = joblib.load("fraud_model.pkl")
encoders = joblib.load("encoders.pkl")

# -----------------------------
# Features used during training
# -----------------------------

FEATURES = [
    "amount",
    "vendor",
    "merchant_category",
    "location",
    "transaction_type",
    "payment_method",
    "device_type",
    "previous_transactions",
    "average_amount",
    "hour",
    "is_weekend",
    "is_night",
    "high_amount",
    "amount_difference",
    "frequent_customer"
]

# -----------------------------
# Prediction Function
# -----------------------------

def predict_transaction(transaction):

    df = pd.DataFrame([transaction])

    df = create_features(df)

    categorical_columns = [

        "vendor",

        "merchant_category",

        "location",

        "transaction_type",

        "payment_method",

        "device_type",

        "day_of_week"

    ]

    # Encode categorical values
    for col in categorical_columns:

        encoder = encoders[col]

        value = df.loc[0, col]

        if value not in encoder.classes_:

            # Handle unseen values
            value = encoder.classes_[0]

        df[col] = encoder.transform([value])

    X = df[FEATURES]

    prediction = rf_model.predict(X)[0]

    probability = rf_model.predict_proba(X)[0][1]

    return prediction, probability


# -----------------------------
# Test Prediction
# -----------------------------

if __name__ == "__main__":

    sample = {

        "transaction_id": "TXN1002",

        "customer_id": "CUST9001",

        "transaction_time": "2024-07-20 23:45:00",

        "amount": 95000,

        "vendor": "Unknown",

        "merchant_category": "Electronics",

        "location": "Delhi",

        "transaction_type": "Transfer",

        "payment_method": "Credit Card",

        "device_type": "Unknown Device",

        "previous_transactions": 1,

        "average_amount": 5000

    }

    prediction, probability = predict_transaction(sample)

    print("\nPrediction :", prediction)

    print("Fraud Probability :", round(probability * 100, 2), "%")

    