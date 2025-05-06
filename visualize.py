import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_time_series(df1):
    fig,ax=plt.subplots(figsize=(8,5))
    ax.plot(df1['Year'],df1['Rainfall'])
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall(mm)")
    ax.set_title("Monthly Rainfall")
    ax.grid(True)
    return fig
def plot_seasonal_pattern(df1):
    
    """"Monthly temp distribution"""
    fig,ax=plt.subplots(figsize=(8,5))
    sns.boxplot(x='Month',y="Rainfall",data=df1,ax=ax)
    ax.set_xlabel("month")
    ax.set_ylabel("Rainfall")
    ax.set_title("Monthly Rainfall distribution")
    ax.grid(True)
    return fig


def plot_yearly_trends(df1):
    year_avg=df1.groupby('Year')['Rainfall'].mean().reset_index()
    fig,ax=plt.subplots(figsize=(8,5))
    ax.plot(year_avg['Year'],year_avg['Rainfall'],marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall(mm)")
    ax.set_title("Total Yearly Rainfall")
    ax.grid(True)
    return fig
    
def plot_actual_vs_predicted(y_test,y_pred):
    """Plot the actual vs predicted values"""
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(y_test,y_pred,alpha=0.7)
    ax.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)],'r--')
    ax.set_xlabel("Actual Rainfall")
    ax.set_ylabel("Predicted Rainfall")
    ax.set_title("Actual Vs Predicted Rainfall")
    return fig
 
def plot_prediction_context(hist_temps,pred_year,pred_month,prediction):
    years_hist,temp_hist=zip(*hist_temps)
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(years_hist,temp_hist,label=f"Historical(month{pred_month})",color="red")
    ax.plot(years_hist,temp_hist,'b--',alpha=0.6)
    ax.scatter([pred_year],[prediction],color='blue',s=100,label='prediction')
    return fig
     