''' Project Landing Page '''# pylint: disable=invalid-name
import streamlit as st

st.set_page_config(page_title='Home')

st.title('Apple Stock Analysis and Forecasting Dashboard')

st.subheader('**Welcome to the Apple Stock Analysis and Forecasting Dashboard**')

st.write('''
This interactive dashboard provides a comprehensive analysis and forecast of Apple Inc. (AAPL) stock prices. Utilizing historical data and advanced statistical models, this platform aims to help you make informed investment decisions by providing accurate and insightful forecasts.
''')

st.header('Project Overview')

st.subheader('Objective')

st.write('''
Our primary objective is to forecast the next 30 days of Apple stock prices. To achieve this, we employ a variety of statistical and machine learning models, as well as deep learning techniques. Each model is meticulously explained on individual pages, providing insights into their methodologies, strengths, and limitations. The final page presents the combined forecasting output, offering a clear and concise prediction for the upcoming month.
''')

st.subheader('Key Features')

st.write('''
* **Time Series Analysis**: In-depth analysis of historical stock data to identify trends and patterns.\
         
* **Multiple Forecasting Models**: Comparison and evaluation of different statistical, machine learning, and deep learning models.\
         
* **Interactive Visualizations**: Dynamic charts and graphs to visualize strock price trends, forecasts, and model performance.\
         
* **Model Explanantions**: Detailed explanations of each forecasting model, including the underlying principles and performance metrics.\
         
* **Final Forecasting Output**: Consolidated forecast for the next 30 days, based on the best-performing models.
''')

st.header('Analysis and Models')

st.subheader('Historical Data Analysis')

st.write('''
We begin with a thorough exploration of historical stock prices, examining trends, seasonality, and other time series characteristics. This analysis sets thefoundation for building robust forecasting models.
''')

st.subheader('Forecasting Models')
st.write('''
1. **Statistical Models**:\
         
    * **ARIMA (AutoRegressive Integrated Moving Average)**: A popular statistical method for time series forecasting.\
         
    * **Exponential Smoothing**: Methods like Holt-Winters to capture trends and seasonality.\
         
    * **Facebook Prophet**: Prophet is an open-source tool form Facebook used for forecasting time series data, based on a decomposable additive model where non-linear trends fit with seasonality.\
         
2. **Machine Learning Models**:\
         
    * **Random Forest**: A versatile model that can handle non-linear relationships in the data.\
         
    * **Support Vector Regression (SVR)**: Effective for capturing complex patterns in stock prices.\
         
3. **Deep Learing Models**:\
         
    * **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) well-suited for sequential data.\
         
    * **GRU (Gated Recurrent Unit)**: Another RNN variant that is simpler and faster than LSTM.\
         
Each model is presented on a dedicated page with detailed explanations, visualizations of the forecasting process, and performance metrics to help you understand their effectiveness and limitations.
''')

st.subheader('Final Forecasting Output')

st.write('''
The final page aggregates the forecasts from all models, providing a comprehensive prediction for the next 30 days. This page also includes a discussion of the combined forecast, highlighting the most reliable models and any consensus among them.
''')

st.header('How to Use This Dashboard')

st.write('''
1. **Explore Historical Data**: Start with the historical data analysis to understand past trends and patterns in Apple stock prices.\
         
2. **Review Forecasting Models**: Visit each model's page to learn about the different forecasting techniques used.\
         
3. **Check the Final Forecast**: Go to the final forecasting output page to see the predicted stock prices for the next 30 days.
''')

st.header('Get Started')

st.write('''
Begin your exploration by navigating through the pages using the sidebar. Dive deep into the analysis and gain valuable insights to aid your investment decisions.
''')
