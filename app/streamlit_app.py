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
    # -------------------------
# FORECASTING (SIMPLE + STABLE)
# -------------------------
st.subheader("🔮 Forecast")

forecast_days = st.slider("Forecast Days", 7, 90, 30)

# Moving average forecast
df["forecast"] = df[demand_col].rolling(window=5).mean()

future_dates = pd.date_range(df[date_col].max(), periods=forecast_days)

last_avg = df[demand_col].tail(5).mean()
future_values = [last_avg] * forecast_days

forecast_df = pd.DataFrame({
    "ds": future_dates,
    "yhat": future_values
})

# Plot
fig3, ax3 = plt.subplots()
ax3.plot(df[date_col], df[demand_col], label="Actual")
ax3.plot(forecast_df["ds"], forecast_df["yhat"],
         linestyle="dashed", label="Forecast")

ax3.legend()
ax3.grid()

st.pyplot(fig3)

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
