# =========================
# AI DEMAND FORECASTING DASHBOARD (ELITE VERSION)
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
# LOAD MODEL (optional)
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
# MAIN
# -------------------------
if file:
    df = pd.read_csv(file)
    df.columns = df.columns.str.lower()

    # Auto detect
    date_col = [c for c in df.columns if "date" in c][0]
    demand_col = [c for c in df.columns if "sales" in c or "demand" in c][0]

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

        if prophet_available:
            model_df = df[[date_col, demand_col]].rename(
                columns={date_col: "ds", demand_col: "y"}
            )

            m = Prophet()
            m.fit(model_df)

            future = m.make_future_dataframe(periods=forecast_days)
            forecast = m.predict(future)

            fig = px.line(forecast, x="ds", y="yhat", title="Forecast")
            st.plotly_chart(fig, use_container_width=True)

            forecast_df = forecast[["ds", "yhat"]]

        else:
            st.warning("Prophet not installed → using fallback")

            df["ma"] = df[demand_col].rolling(5).mean()

            future_dates = pd.date_range(df[date_col].max(), periods=forecast_days)
            avg = df[demand_col].tail(5).mean()

            forecast_df = pd.DataFrame({
                "ds": future_dates,
                "yhat": [avg] * forecast_days
            })

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df[date_col], y=df[demand_col], name="Actual"))
            fig.add_trace(go.Scatter(x=forecast_df["ds"], y=forecast_df["yhat"],
                                     name="Forecast", line=dict(dash="dash")))
            st.plotly_chart(fig, use_container_width=True)

    # =========================
    # TAB 3: ML PREDICTION
    # =========================
    with tab3:
        st.subheader("ML Model Prediction (XGBoost)")

        if model is not None:
            st.success("Model loaded successfully")

            try:
                # Simple demo: use last rows
                sample = df.tail(30).copy()
                X = sample.select_dtypes(include=[np.number]).drop(columns=[demand_col], errors='ignore')

                preds = model.predict(X)
                sample["prediction"] = preds

                fig = px.line(sample, x=date_col, y=[demand_col, "prediction"],
                              title="Actual vs ML Prediction")
                st.plotly_chart(fig, use_container_width=True)

            except:
                st.warning("Feature mismatch with trained model")

        else:
            st.error("No trained model found")

    # =========================
    # TAB 4: DATA
    # =========================
    with tab4:
        st.dataframe(df.tail(100))

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Data", csv, "data.csv")

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
    - Forecast supports inventory optimization decisions
    """)

else:
    st.info("👈 Upload a CSV to begin")

else:
    st.info("👈 Upload a CSV file to get started")

# =========================
# END
# =========================
