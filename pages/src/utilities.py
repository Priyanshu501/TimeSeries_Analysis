''' Contains all the necessary functions for Statistical Calculations '''
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from pmdarima.arima.utils import ndiffs
import streamlit as st

def preprocessing(data):
    ''' Data Preprocessing '''
    # Converting Date Colume to Date Time Format
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

    # Setting Date columne as Index
    data = data.set_index('Date').rename_axis(None)
    return data

df = preprocessing(pd.read_csv('../data/AAPL.csv'))

def arima_stationarity_test(data):
    ''' Checking Stationarity of the Data '''
    adf_result = adfuller(data['Close'])
    st.code(f'ADF Statistic: {adf_result[0]:.2f}')
    st.code(f'p-value: {adf_result[1]:.2f}')

    if adf_result[1] > 0.05:
        return 'non-stationary'
    else:
        return 'stationary'

def arima_differencing(data):
    ''' Calculates Differencing '''
    return ndiffs(data['Close'], test='adf')
