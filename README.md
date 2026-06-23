#  AI-Powered Real-Time Fraud Detection System

## Project Overview

The AI-Powered Real-Time Fraud Detection System is a Machine Learning application that detects fraudulent financial transactions using historical transaction data and intelligent risk analysis.

The system combines:
- Machine Learning (Random Forest)
- Anomaly Detection (Isolation Forest)
- Rule-Based Fraud Detection
- Risk Score Calculation
- Explainable AI
- Interactive Streamlit Dashboard

---

#  Features

-  Real-Time Fraud Prediction
-  Random Forest Machine Learning Model
-  Isolation Forest Anomaly Detection
-  Intelligent Risk Scoring
-  Explainable AI (Reasons for Prediction)
-  Fraud Alert System
-  Transaction Logging
-  Interactive Dashboard
-  CSV Report Download
-  MySQL Database Integration

---

#  Technologies Used

- Python 3.13
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- MySQL
- PyMySQL
- Joblib
- Faker

---

# Project Structure

AI-Fraud-Detection-System
│
├── app.py
├── dashboard.py
├── predict.py
├── train_model.py
├── database.py
├── config.py
│
├── models/
│   ├── fraud_model.pkl
│   ├── isolation_model.pkl
│   └── encoders.pkl
│
├── data/
│   ├── transactions.csv
│   └── feature_importance.csv
│
├── README.md
└── .gitignore
---

#  Dataset

Synthetic Dataset Generated using Python & Faker

**Total Transactions:** 50,000

### Dataset Features

- Transaction ID
- Customer ID
- Transaction Time
- Amount
- Vendor
- Merchant Category
- Location
- Transaction Type
- Payment Method
- Device Type
- Previous Transactions
- Average Amount
- Fraud Label

---

#  Machine Learning Models

### Random Forest Classifier

Used for supervised fraud prediction.

### Isolation Forest

Used for anomaly detection.

---

#  Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 98.84% |
| Precision | 93.55% |
| Recall | 91.39% |
| F1 Score | 92.46% |
| ROC-AUC | 99.83% |

---

#  Risk Score Calculation

Risk score is calculated using:

| Condition | Score |
|-----------|-------|
| ML Fraud Probability | Up to 50 |
| Amount > ₹50,000 | +20 |
| Unknown Vendor | +10 |
| Unknown Device | +5 |
| Previous Transactions < 5 | +5 |
| Night Transaction | +5 |
| High-Risk Location | +5 |

### Decision Rules

| Risk Score | Decision |
|------------|----------|
| 0 – 49 | APPROVE |
| 50 – 79 | VERIFY (OTP) |
| 80 – 100 | BLOCK |

---

#  Dashboard Features

The Streamlit dashboard provides:

- Live Fraud Prediction
- Fraud Probability
- Risk Score
- Decision Engine
- Explainable AI
- Fraud Alerts
- Prediction History
- Interactive Charts
- Download Prediction Logs

---

#  Installation

### Clone Repository

```bash
git clone https://github.com/siddhi0206/AI-Fraud-Detection-System.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

#  Run the Project

### Generate Dataset

```bash
python generate_data.py
```

### Create Database & Import Data

```bash
python database.py
```

### Train Models

```bash
python train_model.py
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---
