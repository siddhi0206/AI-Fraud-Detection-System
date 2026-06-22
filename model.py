import pandas as pd
import pymysql
from sklearn.ensemble import IsolationForest

# ---------------------------
# Load Data
# ---------------------------
def load_data():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="admin@123",
        database="fraud_db"
    )
    df = pd.read_sql("SELECT * FROM transactions", conn)
    conn.close()
    return df

# ---------------------------
# Feature Engineering
# ---------------------------
def add_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['hour'] = df['date'].dt.hour
    df['is_night'] = df['hour'].apply(lambda x: 1 if x < 6 else 0)
    df['high_amount'] = df['amount'].apply(lambda x: 1 if x > 50000 else 0)
    return df

# ---------------------------
# ML Model
# ---------------------------
def apply_ml_model(df):
    model = IsolationForest(contamination=0.05)
    df['fraud_flag'] = model.fit_predict(df[['amount']])
    return df

# ---------------------------
# Rule-Based Detection
# ---------------------------
def apply_rules(df):
    avg_amount = df['amount'].mean()
    df['rule_flag'] = df.apply(
        lambda row: 1 if (row['amount'] > avg_amount * 3 or row['vendor'] == "Unknown") else 0,
        axis=1
    )
    return df

# ---------------------------
# Location Risk
# ---------------------------
def location_risk(df):
    loc_counts = df['location'].value_counts()
    df['location_risk'] = df['location'].apply(lambda x: 1 if loc_counts[x] < 5 else 0)
    return df

# ---------------------------
# Final Detection
# ---------------------------
def final_detection(df):
    df['final_flag'] = df.apply(
        lambda row: 1 if (row['fraud_flag'] == -1 or row['rule_flag'] == 1) else 0,
        axis=1
    )
    return df

# ---------------------------
# Risk Score
# ---------------------------
def calculate_risk(df):
    def score(row):
        s = 0
        if row['fraud_flag'] == -1:
            s += 40
        if row['vendor'] == "Unknown":
            s += 20
        if row['high_amount'] == 1:
            s += 20
        if row['is_night'] == 1:
            s += 10
        if row['location_risk'] == 1:
            s += 10
        return s

    df['risk_score'] = df.apply(score, axis=1)
    return df

# ---------------------------
# Explainable AI
# ---------------------------
def add_reason(df):
    def reason(row):
        reasons = []
        if row['fraud_flag'] == -1:
            reasons.append("Anomaly detected")
        if row['vendor'] == "Unknown":
            reasons.append("Unknown vendor")
        if row['high_amount'] == 1:
            reasons.append("High amount")
        if row['is_night'] == 1:
            reasons.append("Night transaction")
        if row['location_risk'] == 1:
            reasons.append("Unusual location")

        return ", ".join(reasons) if reasons else "Normal Transaction"

    df['reason'] = df.apply(reason, axis=1)
    return df

# ---------------------------
# Decision Engine
# ---------------------------
def add_decision(df):
    def decision(score):
        if score >= 80:
            return "BLOCK"
        elif score >= 40:
            return "VERIFY (OTP)"
        else:
            return "APPROVE"

    df['decision'] = df['risk_score'].apply(decision)
    return df

# ---------------------------
# Pipeline
# ---------------------------
def run_pipeline():
    df = load_data()
    original_df = df.copy()

    df = add_features(df)
    df = apply_ml_model(df)
    df = apply_rules(df)
    df = location_risk(df)
    df = final_detection(df)
    df = calculate_risk(df)
    df = add_reason(df)
    df = add_decision(df)

    return original_df, df