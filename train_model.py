import pandas as pd
import joblib
import json

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import IsolationForest

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

from database import load_data
from feature_engineering import create_features

# =====================================
# LOAD DATA
# =====================================

print("=" * 60)
print("Loading Data...")
print("=" * 60)

df = load_data()

print("Total Records :", len(df))

# =====================================
# FEATURE ENGINEERING
# =====================================

print("\nCreating Features...")

df = create_features(df)

# =====================================
# ENCODE CATEGORICAL FEATURES
# =====================================

categorical_columns = [

    "vendor",

    "merchant_category",

    "location",

    "transaction_type",

    "payment_method",

    "device_type",

    "day_of_week"

]

encoders = {}

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    encoders[column] = encoder

# =====================================
# FEATURES
# =====================================

features = [

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

X = df[features]

y = df["fraud_label"]

# =====================================
# TRAIN TEST SPLIT
# =====================================

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("Training Records :", len(X_train))
print("Testing Records  :", len(X_test))

# =====================================
# RANDOM FOREST MODEL
# =====================================

print("\nTraining Random Forest Model...")

rf = RandomForestClassifier(

    n_estimators=300,

    max_depth=15,

    min_samples_split=5,

    class_weight="balanced",

    random_state=42,

    n_jobs=-1

)

rf.fit(X_train, y_train)

print("Training Completed.")

# =====================================
# PREDICTIONS
# =====================================

prediction = rf.predict(X_test)

probability = rf.predict_proba(X_test)[:, 1]

# =====================================
# METRICS
# =====================================

accuracy = accuracy_score(y_test, prediction)

precision = precision_score(y_test, prediction)

recall = recall_score(y_test, prediction)

f1 = f1_score(y_test, prediction)

roc = roc_auc_score(y_test, probability)

# =====================================
# PRINT RESULTS
# =====================================

print("\n" + "=" * 60)

print("MODEL PERFORMANCE")

print("=" * 60)

print(f"Accuracy  : {accuracy:.4f}")

print(f"Precision : {precision:.4f}")

print(f"Recall    : {recall:.4f}")

print(f"F1 Score  : {f1:.4f}")

print(f"ROC-AUC   : {roc:.4f}")

print("\nConfusion Matrix")

print(confusion_matrix(y_test, prediction))

print("\nClassification Report")

print(classification_report(y_test, prediction))

# =====================================
# FEATURE IMPORTANCE
# =====================================

importance = pd.DataFrame({

    "Feature": features,

    "Importance": rf.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print("\nTop Important Features\n")

print(importance)

# =====================================
# SAVE MODELS
# =====================================

joblib.dump(rf, "fraud_model.pkl")

joblib.dump(encoders, "encoders.pkl")

print("\nRandom Forest Model Saved")

# =====================================
# ISOLATION FOREST
# =====================================

print("\nTraining Isolation Forest...")

iso = IsolationForest(

    contamination=0.05,

    random_state=42

)

iso.fit(X)

joblib.dump(iso, "isolation_model.pkl")

print("Isolation Forest Saved")

# =====================================
# SAVE METRICS
# =====================================

metrics = {

    "accuracy": float(accuracy),

    "precision": float(precision),

    "recall": float(recall),

    "f1_score": float(f1),

    "roc_auc": float(roc)

}

with open("model_metrics.json", "w") as f:

    json.dump(metrics, f, indent=4)

print("\nModel Metrics Saved")

# =====================================
# SAVE FEATURE IMPORTANCE
# =====================================

importance.to_csv(

    "feature_importance.csv",

    index=False

)

print("Feature Importance Saved")

print("\nAll Models Saved Successfully.")

print("=" * 60)