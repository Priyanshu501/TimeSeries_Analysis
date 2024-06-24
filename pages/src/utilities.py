''' Contains all the necessary functions for Statistical Calculations '''
import os
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from pmdarima.arima.utils import ndiffs
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

def preprocessing(data):
    ''' Data Preprocessing '''
    # Converting Date Colume to Date Time Format
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

    # Setting Date columne as Index
    data = data.set_index('Date').rename_axis(None)
    return data

df = preprocessing(pd.read_csv('./data/AAPL.csv'))

def arima_stationarity_test(data):
    ''' Checking Stationarity of the Data '''
    adf_result = adfuller(data['Close'] * 0.80)
    st.code(f'ADF Statistic: {adf_result[0]:.2f}')
    st.code(f'p-value: {adf_result[1]:.2f}')

    if adf_result[1] > 0.05:
        return 'non-stationary'
    else:
        return 'stationary'

def arima_differencing(data):
    ''' Calculates Differencing '''
    return ndiffs(data['Close'], test='adf')

def arima_fit_model(data, p=1, d=1, q=1):
    ''' Train ARIMA Model '''

    # Standardizing Data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['Close']])
    scaled_df = pd.DataFrame(scaled_data, columns=['Close'])
    scaled_df.index = data.index

    # Splitting into train and test sets
    size = int(len(scaled_df['Close']) * 0.80)
    train, test = scaled_df[:size], scaled_df[size:]

    # Fitting Model
    model = ARIMA(train, order=(p, d, q))
    fitted_model = model.fit()
    st.success('Training Successful')
    st.write(fitted_model.summary())
    st.write('\n')

    # Evaluating using MAE and MSE
    steps = int(len(test))
    predictions = fitted_model.forecast(steps, exog=None)

    mae = mean_absolute_error(test, predictions)
    mse = mean_squared_error(test, predictions)

    # Print MAE and MSE
    st.subheader('Model Metrics:')
    st.code(f'Mean Absolute Error: {mae:.3f}')
    st.code(f'Mean Squared Error: {mse:.3f}')

    # Creating Forecast
    forecast_values = fitted_model.forecast(steps)
    forecast_values = scaler.inverse_transform(forecast_values.values.reshape(-1,1))
    forecast_df = pd.DataFrame(forecast_values, index=test.index, columns=['Forecast'])

    original_train = data.iloc[:size]
    original_test = data.iloc[size:]

    # Exporting Model
    directory = 'src/models'
    os.makedirs(directory, exist_ok=True)
    model_path = os.path.join(directory, 'arima.joblib')
    joblib.dump(fitted_model, model_path)

    return original_train, original_test, forecast_df

def forecast(model, steps, data=df):
    ''' Forecasts the Stock Prices '''
    model_path = 'src/models/' + model + '.joblib'
    model = joblib.load(model_path)
    forecasted_values = model.forecast(steps=steps)

    scaler = StandardScaler()
    scaler.fit_transform(data[['Close']])
    forecasted_values = scaler.inverse_transform(forecasted_values.values.reshape(-1,1))

    forecasts_dates = pd.date_range(
        start = data.index[-1] + pd.Timedelta(days=1),
        periods = steps,
        freq = 'D'
    )

    forecasts_df = pd.DataFrame(
        forecasted_values,
        index = forecasts_dates,
        columns=['Forecast']
        )

    return forecasts_df
