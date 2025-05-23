import streamlit as st
from pages import data_exploration,model_training,prediction_page
from data_utilis import load_data
#set configurations
st.set_page_config(
    page_title="Climate Trend Prediction",page_icon='',layout="wide"
)
#LOAD DATA
df=load_data()
#Give the title and desciption
st.title("Climate Trend Analyis and Prediction")
st.markdown(" Analysis historical temperature and predict future trends")
st.sidebar.title("RESOURCES")
page=st.sidebar.radio("Go to",['Data Exploration','Model Training','Prediction'])

data_exploration.show(df)
model_training.show(df)
prediction_page.show(df)  