import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os

# Page config
st.set_page_config(
    page_title="Students Marks Predictor",
    page_icon="🎯",
    layout="wide")

# Custom CSS for dark theme
st.markdown("""
<style>
    .main {background-color: #0e1117;}
    .stButton>button {
        background-color: transparent;
        color: #00bfff;
        border: 2px solid #00bfff;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00bfff;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "students_model_v3.pkl"))

# Calculate R2
data = pd.read_csv(os.path.join(BASE_DIR, "students_score_multi.csv"))
X = data[["Hours", "Sleep", "Attendance"]]
y = data["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
r2 = round(float(model.score(X_test, y_test)) * 100, 2)

# Sidebar
st.sidebar.markdown("## ℹ️ About")
st.sidebar.markdown("""
This app predicts students
marks using Multiple Linear
Regression.

**Features used:**
- Study Hours
- Sleep Hours
- Attendance %

**Developer:**

Subrata Mondal
""")

# Title
st.markdown("## 🎯 Predict My Marks!")
st.markdown("---")

# Three input columns
col1, col2, col3 = st.columns(3)

with col1:
    hours = st.number_input(
        "📘 Enter study hours:",
        min_value=0.0,
        max_value=24.0,
        value=10.0,
        step=0.5)

with col2:
    sleep = st.number_input(
        "😴 Enter sleep hours:",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5)

with col3:
    attendance = st.number_input(
        "🏫 Enter attendance percentage:",
        min_value=0.0,
        max_value=100.0,
        value=90.0,
        step=1.0)

st.markdown("")

# Predict button
if st.button("🎯 Predict My Marks!"):
    
    # Prediction
    new_data = pd.DataFrame({
        "Hours": [hours],
        "Sleep": [sleep],
        "Attendance": [attendance]
    })
    
    prediction = model.predict(new_data)[0]
    prediction = max(0, min(100, prediction))
    marks = round(float(prediction), 1)
    
    # Result
    st.success(f"📊 Predicted Marks: {marks}")
    
    # Performance message
    if marks >= 85:
        st.info("🌟 Outstanding performance!")
        st.balloons()
    elif marks >= 70:
        st.info("👍 Good performance!")
    elif marks >= 50:
        st.warning("📖 Average performance!")
    else:
        st.error("⚠️ Need improvement!")
    
    st.markdown("")
    
    # Two chart columns
    chart1, chart2 = st.columns(2)
    
    with chart1:
        # Feature comparison bar chart
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        fig1.patch.set_facecolor('#1a1a2e')
        ax1.set_facecolor('#1a1a2e')
        
        features = ["Study\nHours", 
                   "Sleep\nHours", 
                   "Attendance\n(%)"]
        values = [hours, sleep, attendance]
        colors = ["#FF4444", "#44FF44", "#4488FF"]
        
        bars = ax1.bar(features, values, 
                      color=colors, width=0.5)
        
        for bar, val in zip(bars, values):
            ax1.text(
                bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.5,
                str(val),
                ha='center',
                color='white',
                fontsize=11,
                fontweight='bold'
            )
        
        ax1.set_title('Feature Comparison', 
                     color='white', fontsize=13)
        ax1.set_ylabel('Values', color='white')
        ax1.tick_params(colors='white')
        ax1.spines['bottom'].set_color('white')
        ax1.spines['left'].set_color('white')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        
        st.pyplot(fig1)
    
    with chart2:
        # Score chart
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        fig2.patch.set_facecolor('#1a1a2e')
        ax2.set_facecolor('#1a1a2e')
        
        ax2.barh(['Score'], [marks],
                color='#4488FF',
                height=0.5)
        ax2.set_xlim(0, 100)
        ax2.axvline(x=marks, 
                   color='red',
                   linestyle='--',
                   linewidth=2)
        
        ax2.set_title(f'Score: {marks}/100',
                     color='white', fontsize=13)
        ax2.set_xlabel('Marks', color='white')
        ax2.tick_params(colors='white')
        ax2.spines['bottom'].set_color('white')
        ax2.spines['left'].set_color('white')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ using python, scikit-learn & Streamlit | Developer: Subrata Mondal</center>",
    unsafe_allow_html=True)

