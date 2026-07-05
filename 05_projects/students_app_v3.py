import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
# Load model
Base_Dir= os.path.dirname(os.path.abspath(__file__))
model=joblib.load(os.path.join(Base_Dir,"students_model_v3.pkl"))
# Page config
st.set_page_config(page_title="Students Marks Predictor",page_icon="🎓",layout="wide")
# Title
st.title("🎓Students Marks Predictor")
st.markdown("AL-powered marks prediction using Machine Learning")
st.markdown("---")
# Sidebar
st.sidebar.header("ℹ️About")
st.sidebar.info("""This app predicts students marks using Multiple Linear Regression.
Features used:
- Study Hours
- Sleep Hours
- Attendance %
Developer : Subrata Mondal""")
# Two coloums layout
col1,col2=st.columns(2)
with col1:
    st.header("📚Enter Students Details")
    hours=st.slider("📖Study Hours",min_value=1,max_value=12,value=6)
    sleep=st.slider("😴Sleep Hours",min_value=4,max_value=10,value=7)
    attendance=st.slider("🏫Attendance %",min_value=50,max_value=100,value=80)
with col2:
    st.header("📊Your Input Summary")
# Show input as bar chart
fig,ax=plt.subplots(figsize=(5,3))
categories=["Study\nHours","Sleep\nHours","Attendance\n(%)"]
values=[hours,sleep,attendance]
colors=["#FF6B6B","#4ECDC4","#45B7D1"]
bars=ax.bar(categories,values,color=colors)
ax.set_title("Your Input Values")
ax.set_ylabel("Value")
# Add value label bars
for bar,value in zip(bars,values):
    ax.text(bar.get_x()+ bar.get_width()/2,bar.get_height()+0.5,str(value),ha="center",fontsize=12)
st.pyplot(fig)
st.markdown("---")
# Predict button
if st.button("🎯Predict My Marks!",use_container_width=True):
    # Mark prediction
    new_data=pd.DataFrame({"Hours":[hours],"Sleep":[sleep],"Attendance":[attendance]})
    prediction=model.predict(new_data)[0]
    # Keep marks between 0 to 100
    prediction=model.predict(new_data)[0]
    ptediction=max(0,min(100,prediction))
    marks=min(100,round(float(prediction),2))
    # Show result
    st.markdown("---")
    col3,col4=st.columns(2)
    with col3:
        st.success(f"📊Predicted Marks:{marks}")  
        # Performance message
        if marks>=85:
            st.balloons()  
            st.info("🌟Outstanding performance!")
        elif marks>=70:
            st.info("👍Good performance!")
        elif marks>=50:
            st.warning("📖Average-study more!")
        else:
            st.error("⚠️Need significant improvement!")
    with col4:
        # Gauge chart
        fig2,ax2=plt.subplots(figsize=(4,3))
        colors_bar=["red","orange","yellow","green"]
        ranges=[25,25,25,25,25]
        ax2.barh(['Score'],[marks],color="blue",height=0.5)
        ax2.set_xlim(0,100)
        ax2.axvline(x=marks,color="red",linestyle="--",linewidth=2)
        ax2.set_title(f"Score:{marks}/100")
        ax2.set_xlabel("Marks")
        ax2.set_ylabel("Score")
        st.pyplot(fig2)
# Footer
st.markdown("---")
st.markdown("<center>Made with 💖 using python, Sciket-learn & Streamlet | Developer: Subrata Mondal</center>",unsafe_allow_html=True)
