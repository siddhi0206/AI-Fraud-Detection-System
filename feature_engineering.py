import pandas as pd


# -----------------------------
# Feature Engineering Function
# -----------------------------
def create_features(df):

    # Convert datetime
    df["transaction_time"] = pd.to_datetime(df["transaction_time"])

    # Hour
    df["hour"] = df["transaction_time"].dt.hour

    # Day of Week
    df["day_of_week"] = df["transaction_time"].dt.day_name()

    # Weekend
    df["is_weekend"] = df["transaction_time"].dt.weekday >= 5

    # Night Transaction
    df["is_night"] = df["hour"].apply(
        lambda x: 1 if x >= 22 or x <= 5 else 0
    )

    # High Amount
    df["high_amount"] = (
    df["amount"] > (df["average_amount"] * 2)
    ).astype(int)

    # Amount Difference
    df["amount_difference"] = (
        df["amount"] - df["average_amount"]
    )

    # Frequent Customer
    df["frequent_customer"] = (
        df["previous_transactions"] > 20
    ).astype(int)

    return df