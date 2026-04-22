# 🍽️ AI-Powered Restaurant Demand Forecasting & Inventory Optimization

## 🚀 Overview

An end-to-end **time-series machine learning system** that predicts daily restaurant demand to enable **data-driven inventory and operations planning**.

This project transforms raw transactional data into **actionable forecasts**, helping businesses reduce waste, optimize stock, and improve profitability.

---

## 💼 Business Problem

Restaurants operate with **perishable inventory and uncertain demand**.

Traditional approaches rely on:

* Static spreadsheets
* Gut-based decision making

This results in:

* ❌ Over-ordering → food waste & higher costs
* ❌ Under-ordering → stockouts & lost revenue

---

## 🎯 Solution

This project builds a **machine learning forecasting pipeline** that:

* Predicts daily demand using historical sales
* Captures **trend, seasonality, and promotions**
* Uses **advanced feature engineering + ensemble models**
* Outputs actionable insights for inventory planning

---

## 🧠 Key Capabilities

### 🔹 Advanced Feature Engineering

* 📅 Calendar features (day, month, weekend flags)
* 🔁 Lag features (1, 7, 14, 28 days)
* 📊 Rolling statistics (mean, std, min, max)
* ⚡ Exponential Moving Averages (EMA)
* 📈 Trend & momentum features

---

### 🔹 Machine Learning Models

* Linear Regression (baseline)
* Random Forest Regressor
* XGBoost Regressor ⭐ (primary model)
* Prophet (time-series baseline)

---

### 🔹 Time-Series Best Practices

* ⏳ Time-based train/test split (no leakage)
* 🔄 TimeSeries Cross Validation
* ⚙️ Hyperparameter tuning
* 📉 Evaluation using MAE & RMSE

---

### 🔹 Model Explainability

* Feature importance analysis
* Correlation analysis
* SHAP (planned / optional)

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **XGBoost**
* **Matplotlib, Seaborn, Plotly**
* **Prophet**

---

## 📂 Project Structure

```
ai-demand-forecasting-restaurant/
│
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_evaluation.ipynb
│
├── src/
├── models/
├── outputs/
│   ├── plots/
│   ├── engineered_features.csv
│   ├── predictions.csv
│
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🔄 Workflow

1. 📊 Data Cleaning & Time-Series EDA
2. 🧠 Feature Engineering (lag, rolling, EMA)
3. 🤖 Model Training (LR, RF, XGBoost)
4. ⚙️ Hyperparameter Tuning
5. 📉 Evaluation (MAE, RMSE)
6. 📈 Business Insights & Visualization

---

## 📊 Model Performance

| Model             | MAE | RMSE |
| ----------------- | --- | ---- |
| Linear Regression |     |      |
| Random Forest     |     |      |
| XGBoost ⭐         |     |      |

👉 XGBoost outperformed others by capturing **non-linear demand patterns and seasonality**.

---

## 📈 Key Insights

* 📅 Strong weekly seasonality (weekend spikes)
* 📈 Upward sales trend over time
* 🔁 Lag features were the most predictive
* ⚡ EMA captured short-term demand shifts effectively

---

## 💰 Business Impact

* 📉 Reduced food waste through accurate forecasting
* 📦 Improved inventory planning
* 📊 Better decision-making for managers
* 💡 Transition from reactive → proactive operations

---

## 🔮 Future Improvements

* 📊 Interactive dashboard using Streamlit
* 🌦️ Integrate external data (weather, events)
* 🚀 Deploy model as an API
* 📡 Real-time demand prediction system

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
