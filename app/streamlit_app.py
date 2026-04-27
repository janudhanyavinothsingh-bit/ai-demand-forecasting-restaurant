# =========================
# AI DEMAND FORECASTING DASHBOARD (ADVANCED - SINGLE CELL)
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Try Prophet (fallback if not installed)
try:
    from prophet import Prophet
    prophet_available = True
except:
    prophet_available = False

st.set_page_config(page_title="AI Demand Forecasting", layout="wide")

# -------------------------
# HEADER
# -------------------------
st.title("📊 AI Demand Forecasting Dashboard")
st.markdown("Upload your dataset → Analyze → Forecast → Download insights")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header("⚙️ Controls")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# -------------------------
# MAIN LOGIC
# -------------------------
if file:
    df = pd.read_csv(file)

    # Normalize column names
    df.columns = df.columns.str.lower()

    # Try to detect columns automatically
    date_col = [col for col in df.columns if "date" in col][0]
    demand_col = [col for col in df.columns if "demand" in col or "sales" in col][0]

    # Convert date
    df[date_col] = pd.to_datetime(df[date_col])

    # Optional product column
    product_col = None
    for col in df.columns:
        if "product" in col or "item" in col:
            product_col = col

    # Sidebar filters
    if product_col:
        product = st.sidebar.selectbox("Select Product", df[product_col].unique())
        df = df[df[product_col] == product]

    date_range = st.sidebar.date_input("Select Date Range",
                                       [df[date_col].min(), df[date_col].max()])

    df = df[(df[date_col] >= pd.to_datetime(date_range[0])) &
            (df[date_col] <= pd.to_datetime(date_range[1]))]

    df = df.sort_values(date_col)

    # -------------------------
    # KPIs
    # -------------------------
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Demand", int(df[demand_col].sum()))
    col2.metric("Average Demand", round(df[demand_col].mean(), 2))
    col3.metric("Max Demand", int(df[demand_col].max()))

    # -------------------------
    # DEMAND PLOT
    # -------------------------
    st.subheader("📈 Demand Trend")

    fig, ax = plt.subplots()
    ax.plot(df[date_col], df[demand_col])
    ax.set_xlabel("Date")
    ax.set_ylabel("Demand")
    ax.grid()

    st.pyplot(fig)

    # -------------------------
    # FORECASTING
    # -------------------------
    st.subheader("🔮 Forecast")

    forecast_days = st.slider("Forecast Days", 7, 90, 30)

    forecast_df = None

    if prophet_available:
        try:
            model_df = df[[date_col, demand_col]].rename(
                columns={date_col: "ds", demand_col: "y"}
            )

            model = Prophet()
            model.fit(model_df)

            future = model.make_future_dataframe(periods=forecast_days)
            forecast = model.predict(future)

            forecast_df = forecast[["ds", "yhat"]]

            fig2 = model.plot(forecast)
            st.pyplot(fig2)

        except Exception as e:
            st.warning("Prophet failed, using fallback model.")
            prophet_available = False

    if not prophet_available:
        # Moving average fallback
        df["forecast"] = df[demand_col].rolling(window=5).mean()

        future_dates = pd.date_range(df[date_col].max(), periods=forecast_days)

        last_avg = df[demand_col].tail(5).mean()
        future_values = [last_avg] * forecast_days

        forecast_df = pd.DataFrame({
            "ds": future_dates,
            "yhat": future_values
        })

        fig3, ax3 = plt.subplots()
        ax3.plot(df[date_col], df[demand_col], label="Actual")
        ax3.plot(forecast_df["ds"], forecast_df["yhat"], linestyle="dashed", label="Forecast")
        ax3.legend()
        ax3.grid()

        st.pyplot(fig3)

    # -------------------------
    # DOWNLOAD
    # -------------------------
    st.subheader("📥 Download Forecast")

    csv = forecast_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Forecast CSV", csv, "forecast.csv", "text/csv")

else:
    st.info("👈 Upload a CSV file to get started")

# =========================
# END
# =========================