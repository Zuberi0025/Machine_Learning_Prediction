import streamlit as st
import numpy as np
import pandas as pd
from model_utils import load_model
from visualization import plot_prediction_context
from prediction import make_prediction,get_historical_context,get_historical_average

def show(df):
    """Display the prediction page"""
    st.header("Temp predictions")
    #Chek if the model exit
    
    #show the used model
    st.info(f"Using{st.session_state['model_type']} for prediction")
    
    #Prediction Input
    st.subheader("select date for prediction")
    pred_year=st.slider("Year",2010,2100,2025)
    pred_month=st.slider("month",1,12,6)
    
    #Make prediction
    if st.button("Predict temperature"):
        model=st.session_state['model']
        prediction=make_prediction(model,pred_year,pred_month)
        #Dipslay results
        st.success(f"Predicted temperatures for {pred_year}-{pred_month:02d}:{prediction:.2f}")
        
        #Historical compare
        hist_avg=get_historical_average(df,pred_month)
        st.write(f"historical average for month{pred_month}:{hist_avg:.2f}")
        
        #Calculate the difference
        diff=prediction-hist_avg
        if diff >0:
            st.write(f"Prediction is {diff:.2f} **higher** than the historical average")  
        else:
            st.write(f"Prediction is {abs(diff):.2f} **lower** than the historical average")
            
        #VISUALIZE
        st.subheader("Prediction in historical context")
        
        #Get the context
        hist_temps=get_historical_context(df,pred_month)
        
        #Plot
        fig=plot_prediction_context(hist_temps,pred_year,pred_month,prediction)
        st.pyplot(fig)                  