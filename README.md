# 🍽️ AI-Powered Restaurant Demand Forecasting & Inventory Optimization

## 📌 Project Overview
This project builds an end-to-end **time-series machine learning system** to forecast daily restaurant demand.  

The goal is to help restaurants:
- Reduce food waste 📉  
- Optimize inventory 📦  
- Improve operational efficiency ⚙️  

---

## 🚀 Business Problem
Restaurants often rely on intuition or static spreadsheets to plan inventory.

This leads to:
- ❌ Over-ordering → Food waste  
- ❌ Under-ordering → Lost revenue  

👉 This project solves it using **AI-driven demand forecasting**.

---

## 🎯 Objectives
- Predict daily sales demand using historical data  
- Capture trends, seasonality, and spikes  
- Minimize prediction error (MAE, RMSE)  
- Convert predictions into business insights  

---

## 🧠 Key Features

### 🔹 Advanced Feature Engineering
- Date-based features (day, month, weekend)
- Lag features (7, 14, 30 days)
- Rolling statistics (mean, std)
- Trend analysis

### 🔹 Multiple Machine Learning Models
- Linear Regression (Baseline)
- Random Forest
- XGBoost (Primary Model)
- Prophet (Time-series model)

### 🔹 Time-Series Techniques
- Time-based train-test split
- TimeSeries Cross Validation
- Hyperparameter tuning

### 🔹 Model Explainability
- Feature Importance
- SHAP analysis

---

## 🛠️ Tech Stack
- Python 🐍
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn, Plotly
- Prophet (optional)

---

## 📂 Project Structure

ai-demand-forecasting-restaurant/
│
├── data/
├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_modeling.ipynb
│ ├── 04_evaluation.ipynb
│
├── src/
├── models/
├── outputs/
│ ├── plots/
│ ├── predictions.csv
│
├── requirements.txt
├── README.md
├── .gitignore


---

## 📊 Workflow

1. Data Cleaning & EDA  
2. Feature Engineering  
3. Model Training  
4. Hyperparameter Tuning  
5. Evaluation & Visualization  
6. Business Insights  

---

## 📈 Model Evaluation

| Model            | MAE | RMSE |
|------------------|-----|------|
| Linear Regression|     |      |
| Random Forest    |     |      |
| XGBoost          |     |      |

👉 XGBoost performed best in capturing demand patterns.

---

## 📉 Business Impact

- 📉 Reduced over-ordering  
- 📦 Improved inventory planning  
- 💰 Increased revenue opportunities  

---

## 🔥 Key Learnings

- Time-series forecasting techniques  
- Feature engineering for demand prediction  
- Model comparison and tuning  
- Translating ML output into business decisions  

---

## 🚀 Future Improvements

- Add real-time dashboard (Streamlit)
- Integrate weather & holiday APIs
- Deploy model for live predictions

---

## 👩‍💻 Author


---

## ⭐ If you like this project
Give it a ⭐ on GitHub!