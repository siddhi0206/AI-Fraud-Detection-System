import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

random.seed(42)

vendors = [
    "Amazon", "Flipkart", "Swiggy", "Zomato",
    "Myntra", "Reliance", "PhonePe", "Google Pay",
    "Paytm", "Unknown"
]

merchant_categories = [
    "Shopping",
    "Food",
    "Travel",
    "Electronics",
    "Transfer"
]

locations = [
    "Pune",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

device_types = [
    "Android",
    "iPhone",
    "Laptop",
    "Desktop",
    "Unknown Device"
]

transaction_types = [
    "Online",
    "POS",
    "Transfer"
]

rows = []

start_date = datetime(2024,1,1)

for i in range(50000):

    timestamp = start_date + timedelta(
        days=random.randint(0,180),
        hours=random.randint(0,23),
        minutes=random.randint(0,59)
    )

    vendor = random.choice(vendors)
    location = random.choice(locations)
    device = random.choice(device_types)
    payment = random.choice(payment_methods)
    transaction_type = random.choice(transaction_types)

    amount = random.randint(100,120000)

    previous_transactions = random.randint(0,50)

    average_amount = random.randint(1000,40000)

    fraud_score = 0

    # -------------------------
    # Fraud Rules
    # -------------------------

    # Unknown Vendor
    if vendor == "Unknown":
        fraud_score += 30

    # High Amount
    if amount > 50000:
        fraud_score += 30

    # Night Transaction
    if timestamp.hour >= 22 or timestamp.hour <= 5:
        fraud_score += 15

    # Unknown Device
    if device == "Unknown Device":
        fraud_score += 10

    # New Customer
    if previous_transactions < 5:
        fraud_score += 10

    # Different Location
    if location in ["Delhi","Bangalore"]:
        fraud_score += 5

    # Large Difference from Average
    if amount > average_amount * 3:
        fraud_score += 15

    # Transfer
    if transaction_type == "Transfer":
        fraud_score += 5

    # Credit Card
    if payment == "Credit Card":
        fraud_score += 5

    # -------------------------
    # Final Label
    # -------------------------

  
    fraud_label = 1 if fraud_score >= 75 else 0
    rows.append({

        "transaction_id": str(uuid.uuid4())[:12],

        "customer_id": f"CUST{random.randint(1000,9999)}",

        "transaction_time": timestamp,

        "amount": amount,

        "vendor": vendor,

        "merchant_category": random.choice(merchant_categories),

        "location": location,

        "transaction_type": transaction_type,

        "payment_method": payment,

        "device_type": device,

        "previous_transactions": previous_transactions,

        "average_amount": average_amount,

        "fraud_label": fraud_label

    })

df = pd.DataFrame(rows)

df.to_csv("transactions.csv", index=False)

print(df.head())

print("\nTotal Transactions :", len(df))
print("Fraud Transactions :", df["fraud_label"].sum())
print("Fraud Percentage :",
      round(df["fraud_label"].mean()*100,2), "%")