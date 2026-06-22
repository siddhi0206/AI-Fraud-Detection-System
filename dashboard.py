import pandas as pd
import streamlit as st
import plotly.express as px

def show_dashboard():

    st.title("📊 AI Fraud Detection Dashboard")

    try:
        df = pd.read_csv("prediction_logs.csv")
        df["risk_score"] = pd.to_numeric(df["risk_score"], errors="coerce")
        df["prediction"] = pd.to_numeric(df["prediction"], errors="coerce")

        df = df.dropna()

        df["risk_score"] = df["risk_score"].astype(int)
        df["prediction"] = df["prediction"].astype(int)

        # ==========================
        # KPI CARDS
        # ==========================

        total = len(df)
        fraud = len(df[df["prediction"] == 1])
        approved = len(df[df["decision"] == "APPROVE"])
        high_risk = len(df[df["risk_score"] >= 80])

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("💳 Total Transactions", total)
        col2.metric("🚨 Fraud Detected", fraud)
        col3.metric("✅ Approved", approved)
        col4.metric("🔴 High Risk", high_risk)

        st.divider()

        # ==========================
        # CHARTS
        # ==========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Decision Distribution")

            fig = px.pie(
                df,
                names="decision",
                hole=0.45,
                title="Decision Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:

            st.subheader("Vendor Distribution")

            fig = px.bar(
                df["vendor"].value_counts().reset_index(),
                x="vendor",
                y="count",
                labels={
                    "vendor":"Vendor",
                    "count":"Transactions"
                },
                title="Vendor Wise Transactions"
            )

            st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # RISK SCORE
        # ==========================

        st.subheader("Risk Score Distribution")

        fig = px.histogram(
            df,
            x="risk_score",
            nbins=20,
            title="Risk Score"
        )

        st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # METRICS
        # ==========================

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Average Risk Score",
            round(df["risk_score"].mean(),2)
        )

        c2.metric(
            "Maximum Risk",
            round(df["risk_score"].max(),2)
        )

        c3.metric(
            "Minimum Risk",
            round(df["risk_score"].min(),2)
        )

        st.divider()

        # ==========================
        # HISTORY
        # ==========================

        st.subheader("📜 Prediction History")

        df = df.sort_values(
            "timestamp",
            ascending=False
        )

        st.dataframe(
            df,
            use_container_width=True,
            height=400
        )

        # ==========================
        # DOWNLOAD
        # ==========================

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Prediction History",
            csv,
            "prediction_history.csv",
            "text/csv"
        )

    except FileNotFoundError:

        st.warning("prediction_logs.csv not found.")

    except Exception as e:

        st.error(f"Error : {e}")