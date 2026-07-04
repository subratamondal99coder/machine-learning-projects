import streamlit as st
import joblib
import os
import pandas as pd
# Page settings
st.set_page_config(page_title="House Price Predictor",page_icon="🏠",layout="wide")
# Load train model
current_dir=os.path.dirname(__file__)
model_path=os.path.join(current_dir,"house_model.pkl")
model=joblib.load(model_path)
st.title("🏠House Price Predictor")
st.caption("Al-powered house price prediction using Machine Learning")
st.sidebar.title("ℹ️About")
st.sidebar.info("""🏡 This app predicts house prices using a machine learning model built with Scikit-Learn.Devoloper:👨‍💻 Subrata Mondal""")
st.divider()
with st.container():
    st.subheader("🏡 Enter House Details")
area=st.number_input("📏Area (sq ft)", min_value=500, max_value=10000,value=1500)
bedrooms=st.slider("🛏️Bedrooms",1,10,13)
age=st.slider("🏠House Age(years)",0,100,5)
predict=st.button("Predict price")
if predict:
    with st.spinner("🤖 Predicting price..."):
     data=pd.DataFrame({"Area":[area],"Bedrooms":[bedrooms],"Age":[age]})
     prediction=model.predict(data)
     st.success(f"💰Estimated House Price:₹{prediction[0]:,.0f}") 
st.markdown("---")
st.markdown("""<div style='text-align:center'>Made with 💖 using Python,Scikit-Learn and Streamlit</div>""",unsafe_allow_html=True)