''' ARIMA Model ''' # pylint: disable=invalid-name
import streamlit as st
import pages.src.utilities as utl #pylint: disable=import-error
import pages.src.visualizations as vis

#----- Setting Page Configuration -----#
st.set_page_config(page_title='ARIMA')\

#----- Session State Configuration -----#
session_state = utl.get_session_state()
if 'p' not in session_state:
    session_state.p = 1

if 'd' not in session_state:
    session_state.d = 1

if 'q' not in session_state:
    session_state.q = 1

if 'forecast_days' not in session_state:
    session_state.forecast_days = 30

#----- Sidebar Configuration -----#
st.sidebar.title('ARIMA Model Implementation')
st.sidebar.markdown('''
## Table of Contents:
1. [Introduction](#introduction)
2. [Theory behind ARIMA](#theory-behind-arima)
3. [Data Preprocessing](#data-preprocessing-for-arima)
    * [Stationarity](#stationarity)
    * [Order of Autoregressinve Model (q)](#order-of-autoregressive-model-q)
    * [Order of Moving Average (p)](#order-of-moving-average-p)
4. [Model Building](#model-building)
5. [Forecasting](#forecasting)
''')

#----- Introduction -----#
st.title('ARIMA Model Implementation')
st.header('Introduction')
st.write('''
The ARIMA model stands for AutoRegressive Integrated Moveing Average. It is a popular statistical method used for time series forecasting.\n
In this section, we will explain how the ARIMA model works and how it can be applied to forecast Apple stock prices.
''')

#----- ARIMA Theory -----#
st.header('Theory Behind ARIMA')
st.write('''
ARIMA consists of three main components:
1. **AutoRegressive (AR)**: This component uses the dependency between an observation and a number of lagged observations.

2. **Integrated (I)**: This part involved differencing the raw observations to make the timeseries stationary.

3. **Moving Average (MA)**: This component uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.

\nThe ARIMA(p, d, q) model is defined as:
''')

# ARIMA Equation
st.latex(r'''
y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + ... + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + ... + \theta_q \epsilon_{t-q} + \epsilon_t
''')

#----- Data Preprocessing -----#
st.header('Data Preprocessing for ARIMA')

# Displaying Dataset
st.write('Dataset Overview:')
st.dataframe(utl.df, use_container_width=True)

#--- Stationarity ---#
st.subheader('Stationarity')
st.write('''
A stationarity time series has statistical properties, such as mean and variance, that are constant over time.\n
We use the Augmented Dickey-Fuller (ADF) test to check for stationarity.
''')

# Hypothesis Test
st.write('**Hypothesis Test to evaluate Stationarity**:')
st.write('''
* **Null Hypothesis**: Time Series is Non-Stationary.
* **Alternative Hypothesis**: Time Series is Stationary.
''')
st.write('''
**If** the `p-value` of the test is less than the significance level of `0.05`,\
         
**Then** we can reject the Null Hypothesis and conclude that the time series is indeed stationary.
''')

# Displaying Stationarity Code
stationarity_test = st.expander('See Code:')
stationarity_test.code('''
    from statsmodels.tsa.stattools import adfuller
    
    adf_result = adfuller(df['Close'])
    print(f'ADF Statistic: {adf_result[0]:.2f}')
    print(f'p-value: {adf_result[1]:.2f}')

    if adf_result[1] > 0.05:
        print('Accept Null Hypothesis: Data is non-stationary')
    else:
        print('Reject Null Hypothesis: Data is stationary')
''')

# Conducting Hypothesis Test
if utl.arima_stationarity_test(utl.df) == 'non-stationary':
    st.success('Accept Null Hypothesis: Data is non-stationary')
else:
    st.error('Reject Null Hypothesis: Data is stationary')

# Differencing
st.write('If the series is not stationary, we difference it.')
st.write('''
We can find the difference by subtracting the previous value from the current value. Now if we just difference once, we might not get a stationary series so we might need to do that multiple times.
''')
st.write('''
So, for simplicity we will use `pmdarima` library to find the Differenceing (d):
''')

# Displaying Code for Differencing Calculations
differencing = st.expander('See Code:')
differencing.code('''
from pmdarima.arima.utils import ndiffs
        
print('Differencing: \\nd = ', ndiffs(df['Close'], test='adf'))
''')

# Calculating Differencing
st.code(f'd = {utl.arima_differencing(utl.df)}')

#--- Order of Autoregressive Model ---#
st.subheader('Order of Autoregressive Model (q)')
st.write('''
We can find out the required number of AutoRegresssive Model by instpecting the Partial Autocorrelations (PACF) plot.\n
The Partial Auto Correlations represents the correlation between the series and its lags.
''')

# Displaying Code for PACF Plot
pacf_plot = st.expander('See Code:')
pacf_plot.code('''
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf

diff = df['Close'].diff().dropna()
plot_pacf(diff)
plt.show()
''')

# PACF Plot
st.plotly_chart(vis.autocorrelation_plot(utl.df, plot_pacf=True))
st.write('''
We can observe that the lag point 7 is significant as it is just above the significance line.\n
Therefore, let's consider:
''')
st.code('q = 7')

#--- Order of Moving Average ---#
st.subheader('Order of Moving Average (p)')
st.write('''
Order of Moving Average refers to the number of lagged forecast errors that should go into the ARIMA model.\n
We can look at the ACF plot to define the number of MA terms.
''')

# Displaying Code for ACF Plot
acf_plot = st.expander('See Code:')
acf_plot.code('''
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

diff = df['Close'].diff().dropna()
plot_acf(diff)
plt.show()
''')

# ACF Plot
st.plotly_chart(vis.autocorrelation_plot(utl.df, plot_pacf=False))
st.write('''
We can observe that the lag point 2 is  just at the significance line.\n
Therefore, let's consider:
''')
st.code('p = 2')

#----- Model Building -----#
st.header('Model Building')
st.write('''
Using the Identified Parameters, we will build the ARIMA model.
''')

session_state.p = st.number_input('Enter value for p:', min_value=0, value=2)
session_state.d = st.number_input('Enter value for d:', min_value=0, value=1)
session_state.q = st.number_input('Enter value for q:', min_value=0, value=7)

# Fitting Model
if st.button('Fit Model: ARIMA'):
    train, test, forecast = utl.arima_fit_model(
        utl.df,
        p=session_state.p,
        d=session_state.d,
        q=session_state.q
        )

    #----- Model Evaluation -----#
    st.header('Model Evaluation')
    st.write('''
    We will evaluate the model using metrics such as RMSE and visualize the residuals to check the model adequacy.
    ''')
    st.plotly_chart(vis.model_visulization(train=train, test=test, forecast=forecast))

#----- Forecasting -----#
st.header('Forecasting')
st.write('''
We use the fitted model to frecast the next 30 days of stock prices.
''')
session_state.forecast_days = st.slider(
    'Enter Forecaste Days',
    min_value=10,
    max_value=30,
    value=30
    )

if st.button('Forecast'):
    forecast_values = utl.arima_forecast(
        steps=session_state.forecast_days,
        p=session_state.p,
        d=session_state.d,
        q=session_state.q
        )
    st.plotly_chart(vis.final_forecast(forecast=forecast_values))
