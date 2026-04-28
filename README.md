# 🍽️ AI-Powered Restaurant Demand Forecasting & Inventory Optimization

 **Live Application:**  
https://ai-demand-forecasting-restaurant-voumagqjbw5bydbd9dpxrp.streamlit.app/

---

## 📌 Overview

This project delivers a **production-oriented, end-to-end time-series machine learning system** to forecast daily restaurant demand and optimize inventory planning. It combines advanced feature engineering, robust model training, and an interactive dashboard to convert raw sales data into actionable business insights.

---

##  Problem Statement

Restaurants often rely on intuition or static spreadsheets for demand planning, resulting in:

- Over-ordering → Increased food waste  
- Under-ordering → Lost revenue  

This project addresses the problem using **data-driven demand forecasting models**.

---

##  Methodology

Data → EDA → Feature Engineering → Model Training → Evaluation → Deployment


### 🔹 Exploratory Data Analysis
- Trend and seasonality detection  
- Weekly and monthly demand patterns  
- Data cleaning and validation  

### 🔹 Feature Engineering
- Lag features (7, 14, 30 days)  
- Rolling statistics (mean, std)  
- Calendar features (weekend, month-end)  
- Exponential moving averages  
- Trend-based signals  

### 🔹 Model Development
- Linear Regression (baseline)  
- Random Forest Regressor  
- **XGBoost (Best Performing Model)**  
- TimeSeriesSplit cross-validation  

### 🔹 Evaluation Metrics
- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- MAPE (Mean Absolute Percentage Error)  

---

## 🏆 Model Performance

**Best Model: XGBoost**

- MAE  → Low daily prediction error  
- RMSE → Handles large deviations effectively  
- MAPE → ~85–90% forecasting accuracy  

📌 The model captures both short-term fluctuations and long-term trends effectively.

---

##  Key Insights

- Strong weekly seasonality with weekend spikes  
- Lag features (especially 7-day) are highly predictive  
- Clear upward demand trend over time  
- External factors moderately influence demand  

---

## 📂 Project Structure

ai-demand-forecasting-restaurant/

│
├── app/
│ └── streamlit_app.py
│
├── notebooks/
│ ├── week1_eda.ipynb
│ ├── week2_feature_engineering.ipynb
│ ├── week3_model_training.ipynb
│ └── week4_evaluation.ipynb
│
├── data/
│ ├── train.csv
│ └── test.csv
│
├── outputs/
│ ├── engineered_features.csv
│ └── plots/
│
├── models/ # ignored (trained models)
├── requirements.txt
├── main.py
└── README.md


---

## 🖥️ Streamlit Dashboard

The deployed application includes:

- CSV dataset upload  
- Interactive demand visualization  
- Time-series forecasting  
- ML-based predictions (XGBoost)  
- KPI metrics (MAE, Accuracy)  
- Forecast download functionality  

---

##  Run Locally
git clone https://github.com/janudhanyavinothsingh-bit/ai-demand-forecasting-restaurant.git
cd ai-demand-forecasting-restaurant
pip install -r requirements.txt
streamlit run app/streamlit_app.py

---

##  Business Impact
Reduced over-ordering and waste
Improved inventory planning
Better demand visibility
Data-driven decision making

---

##  Key Learnings
Time-series forecasting techniques
Feature engineering for demand prediction
Model comparison and optimization
Building deployable ML dashboards

---

##  Future Improvements
Weather & holiday data integration
Real-time prediction APIs
Deep learning models (LSTM)
MLOps pipeline for automation


