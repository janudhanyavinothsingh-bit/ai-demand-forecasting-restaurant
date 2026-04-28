# =========================
# AI DEMAND FORECASTING DASHBOARD (PRODUCTION VERSION)
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle

st.set_page_config(page_title="AI Demand Forecasting", layout="wide")

# -------------------------
# HEADER
# -------------------------
st.title("🍽️ AI Demand Forecasting Dashboard")
st.markdown("Advanced ML + Time-Series Forecasting System")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header("⚙️ Controls")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
forecast_days = st.sidebar.slider("Forecast Days", 7, 90, 30)

# -------------------------
# LOAD MODEL
# -------------------------
@st.cache_resource
def load_model():
    try:
        with open("models/xgboost_best_model.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return None

model = load_model()

# -------------------------
# MAIN APP
# -------------------------
if file:
    df = pd.read_csv(file)
    df.columns = df.columns.str.lower()

    # -------------------------
    # SAFE COLUMN DETECTION
    # -------------------------
    date_candidates = [c for c in df.columns if "date" in c]
    if not date_candidates:
        st.error("❌ No 'date' column found.")
        st.stop()
    date_col = date_candidates[0]

    demand_candidates = [c for c in df.columns if "sales" in c or "demand" in c]
    if not demand_candidates:
        st.error(f"❌ No 'sales' or 'demand' column found.\n\nColumns: {list(df.columns)}")
        st.stop()
    demand_col = demand_candidates[0]

    # Convert & sort
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col)

    # -------------------------
    # TABS
    # -------------------------
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Overview", "📈 Forecast", "🤖 ML Prediction", "📂 Data"
    ])

    # =========================
    # TAB 1: OVERVIEW
    # =========================
    with tab1:
        st.subheader("Business Metrics")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Demand", int(df[demand_col].sum()))
        col2.metric("Average Demand", round(df[demand_col].mean(), 2))
        col3.metric("Peak Demand", int(df[demand_col].max()))

        fig = px.line(df, x=date_col, y=demand_col, title="Demand Trend")
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # TAB 2: FORECAST
    # =========================
    with tab2:
        st.subheader("Time-Series Forecast")

        # Moving Average Forecast
        df["ma"] = df[demand_col].rolling(5).mean()

        future_dates = pd.date_range(df[date_col].max(), periods=forecast_days)
        avg = df[demand_col].tail(5).mean()

        forecast_df = pd.DataFrame({
            "ds": future_dates,
            "yhat": [avg] * forecast_days
        })

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df[date_col], y=df[demand_col],
            name="Actual"
        ))
        fig.add_trace(go.Scatter(
            x=forecast_df["ds"], y=forecast_df["yhat"],
            name="Forecast",
            line=dict(dash="dash")
        ))

        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # TAB 3: ML PREDICTION
    # =========================
    with tab3:
        st.subheader("ML Model Prediction (XGBoost)")

        if model is not None:
            st.success("Model loaded successfully")

            try:
                sample = df.tail(30).copy()

                # Only numeric features
                X = sample.select_dtypes(include=[np.number]).drop(columns=[demand_col], errors='ignore')

                preds = model.predict(X)
                sample["prediction"] = np.maximum(preds, 0)

                fig = px.line(
                    sample,
                    x=date_col,
                    y=[demand_col, "prediction"],
                    title="Actual vs Predicted"
                )
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.warning(f"⚠️ Feature mismatch: {e}")

        else:
            st.error("❌ No trained model found in /models folder")

    # =========================
    # TAB 4: DATA
    # =========================
    with tab4:
        st.subheader("Raw Data")

        st.dataframe(df.tail(100))

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Data", csv, "data.csv")

    # =========================
    # BUSINESS INSIGHTS
    # =========================
    st.markdown("---")
    st.subheader("💼 AI Insights")

    trend = "increasing 📈" if df[demand_col].iloc[-1] > df[demand_col].iloc[0] else "decreasing 📉"

    st.markdown(f"""
    - Demand trend is **{trend}**
    - Peak demand: **{int(df[demand_col].max())} units**
    - Average demand: **{int(df[demand_col].mean())} units**
    - Forecast helps optimize inventory and reduce waste
    """)

# -------------------------
# NO FILE UPLOADED
# -------------------------
else:
    st.info("👈 Upload a CSV file to begin")

# =========================
# END
# =========================
