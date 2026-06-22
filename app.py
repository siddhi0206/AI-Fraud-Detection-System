import streamlit as st
from dashboard import show_dashboard
from predict import predict_transaction
from risk_score import calculate_risk
from alerts import send_alert
from logger import log_transaction

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("💳 AI-Powered Real-Time Fraud Detection System")
st.markdown("Detect fraudulent transactions using Machine Learning")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("📝 Transaction Details")

transaction = {}

transaction["transaction_id"] = st.sidebar.text_input(
    "Transaction ID",
    "TXN1001"
)

transaction["customer_id"] = st.sidebar.text_input(
    "Customer ID",
    "CUST1001"
)

transaction["transaction_time"] = st.sidebar.text_input(
    "Transaction Time",
    "2024-06-20 22:30:00"
)

transaction["amount"] = st.sidebar.number_input(
    "Amount",
    min_value=0.0,
    value=5000.0
)

transaction["vendor"] = st.sidebar.selectbox(
    "Vendor",
    [
        "Amazon",
        "Flipkart",
        "Reliance",
        "Myntra",
        "Unknown"
    ]
)

transaction["merchant_category"] = st.sidebar.selectbox(
    "Merchant Category",
    [
        "Shopping",
        "Food",
        "Travel",
        "Electronics"
    ]
)

transaction["location"] = st.sidebar.selectbox(
    "Location",
    [
        "Pune",
        "Mumbai",
        "Delhi",
        "Bangalore"
    ]
)

transaction["transaction_type"] = st.sidebar.selectbox(
    "Transaction Type",
    [
        "UPI",
        "Card",
        "Transfer"
    ]
)

transaction["payment_method"] = st.sidebar.selectbox(
    "Payment Method",
    [
        "UPI",
        "Credit Card",
        "Debit Card"
    ]
)

transaction["device_type"] = st.sidebar.selectbox(
    "Device Type",
    [
        "Android",
        "iPhone",
        "Laptop",
        "Desktop",
        "Unknown Device"
    ]
)

transaction["previous_transactions"] = st.sidebar.slider(
    "Previous Transactions",
    0,
    100,
    5
)

transaction["average_amount"] = st.sidebar.number_input(
    "Average Amount",
    value=10000.0
)

predict_btn = st.sidebar.button("🚀 Predict Fraud")

# -----------------------------
# DASHBOARD
# -----------------------------
show_dashboard()

st.divider()

# -----------------------------
# PREDICTION
# -----------------------------
if predict_btn:

    prediction, probability = predict_transaction(transaction)

    risk = calculate_risk(
        transaction,
        probability
    )

    log_transaction(
        transaction,
        prediction,
        probability,
        risk,
        risk["decision"]
    )

    st.header("Prediction Result")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

    with c2:
        st.metric(
            "Risk Score",
            risk["risk_score"]
        )

    with c3:
        st.metric(
            "Decision",
            risk["decision"]
        )

    st.divider()

    st.subheader("Alert")

    if risk["decision"] == "BLOCK":
        st.error(send_alert(risk))

    elif risk["decision"] == "VERIFY (OTP)":
        st.warning(send_alert(risk))

    else:
        st.success(send_alert(risk))

    st.divider()

    st.subheader("Reason")

    for reason in risk["reasons"]:
        st.write("✔", reason)
