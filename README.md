# 🛡️ AI Fraud Detection System

An AI-powered Fraud Detection System built using **Python**, **Machine Learning**, **Streamlit**, and **MySQL**. This application analyzes financial transactions, predicts fraudulent activities, calculates risk scores, and provides an interactive dashboard for monitoring fraud.

---

##  Project Overview

The AI Fraud Detection System is designed to identify suspicious financial transactions using machine learning algorithms. It helps organizations reduce fraud by providing real-time predictions, transaction monitoring, and visual analytics.

---

##  Features

-  Detect fraudulent transactions using Machine Learning
-  Interactive dashboard built with Streamlit
-  Fraud alerts for high-risk transactions
-  Risk score calculation
-  Feature engineering for improved predictions
-  MySQL database integration
-  Prediction logging
-  Feature importance analysis
-  Isolation Forest for anomaly detection

---

##  Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- MySQL
- Joblib
- Pickle
- Git & GitHub

---

##  Project Structure

```
AI-Fraud-Detection-System/
│
├── app.py
├── dashboard.py
├── alerts.py
├── predict.py
├── model.py
├── train_model.py
├── database.py
├── config.py
├── logger.py
├── feature_engineering.py
├── risk_score.py
├── generate_data.py
│
├── fraud_model.pkl
├── isolation_model.pkl
├── encoders.pkl
│
├── feature_importance.csv
├── model_metrics.json
├── transactions.csv
├── prediction_logs.csv
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/siddhi0206/AI-Fraud-Detection-System.git
```

### 2. Navigate to the project folder

```bash
cd AI-Fraud-Detection-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

##  Machine Learning Models

This project uses:

- Random Forest Classifier
- Isolation Forest (Anomaly Detection)

The models are trained to identify fraudulent transactions based on transaction features.

---

##  Output

The application provides:

- Fraud Prediction
- Fraud Probability
- Risk Score
- Transaction Logs
- Interactive Dashboard
- Feature Importance Analysis

---

## 📂 Dataset

The project includes a sample transaction dataset for demonstration purposes.

---
