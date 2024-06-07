import streamlit as st
import pandas as pd
from utilities import preprocessing
from visualizations import *

# Importing Dataset
data = pd.read_csv('../data/AAPL.csv')
stock_data = preprocessing(data)

# Title
st.title('Exploratory Data Analysis', )

# Overview
st.header('Overview:')
st.write('''We are analyzing Apple Stock (AAPL) Prices from 2012 to 2019.\
         
         The Dataset includes daily stock prices and trading volumn.''')

# Objective
st.header('Objective:')
st.write('''
        1. Understanding the stock price movements over the period of time.\
         
        2. Identify key components such as trends, seasonality, cyclic variations, and noise in the time series data.
        ''')

# Dataset Overview
st.header('Dataset Overview')
st.write('''
        The dataset comprises AAPL stock prices from **January 2012** to **December 2019**.\n\
         
         In includes daily records with the following columns:\
         
         * **Date:** The specific trading day.\
         
         * **Open:** The stock's opening price on that day.\
         
         * **High:** The highest price reached during the trading day.\
         
         * **Low:** The lowest price reached during the trading day.\
         
         * **Close:** The stock's closing price on that day.\
         
         * **Adj Close:** The adjusted closing price, accounting for stock splits and dividends.\
         
         * **Volume:** The number of shares traded on that day.
''')
view_dataset = st.expander("View Dataset")
view_dataset.dataframe(stock_data, use_container_width=True)

# Statistical Description
st.header('Statistical Overview')
st.write(stock_data.describe())
statistical_observations = st.expander("See Explanation")
statistical_observations.subheader('Key Oberservations: Open, High, Low, Close')
statistical_observations.write('''
         * Average closely falls around 126 to 128.\
         
         * Standard Deviation is around 50 to 51. Indicating consistent fluctuations in the stock's price throughout the trading day.\
         
         * Highest recorded price is 291.5 and Lowest price is 55.0. Indicating High Variability in prices.
         ''')
statistical_observations.subheader('Key Observations: Volume')
statistical_observations.write('''
         * Average Trading Volume is approximately 59.5 million shares.\
         
         * Standard Deviation if 46.8 million.\
         
         * Highest Recorded Volume of 376.53 million and Lowest is 11.36 million.\
         
         * High Variabilit, Reflecting periods of both very high and very low trading activitiy.\
                               
         ''')

# Visualizations
st.header('Visualizations')

# Density Plot
st.subheader('Line Plots and Histograms')
st.plotly_chart(density_plot, use_container_width=True)

histogram_observations = st.expander('See Interpretation')
histogram_observations.write('''
                             Observations:\
                             
                             * Distribution is right-skewed with a long tail towards higher prices, this indicates positive price changes are more frequent.\
                             
                             * There is significant variability in the closing prices over the time period.
''')

# Stock Data Overview
st.subheader('Observations from Line Plots' )
st.plotly_chart(line_plots, use_container_width=True)

stock_data_obs = st.expander('See Interpretation')
stock_data_obs.write('''
                     Interpretations:\
                     
                     * Overall strong consistently upward trend. Indicating overall growth and Increasing value over the period.\
                     
                     * Overall High Variability in Price Ranges.\
                     
                     * As we can see all line plots follow a consistent pattern
''')

st.plotly_chart(line_plots2, use_container_width=True)

stock_data_obs2 = st.expander('See Interpretation')
stock_data_obs2.write('''
                      Interpretations:\
                      
                      * **Volatility**: The 2012-2013 period was marked by higher volatility compared to 2016-2017.

                      * **Recovery and Growth**: While 2012-2013 saw a sharp decline followed by a recovery, 2016-2017 was characterized by steady growth, indicating a period of sustained positive performance for Apple stock.
''')

# Daily Percentage Changes in Closing Prices
st.plotly_chart(pct_change, use_container_width=True)
st.plotly_chart(kde_plot, use_container_width=True)

per_change = st.expander('See Interpretation')
per_change.write('''
                 Interpretations:\
                 
                 * It indicates daily fluctuations in stock prices.\
                 
                 * Highest Positive close price change is 8.87% which indicates a recovery or positive sentiment in the market.\
                 
                 * Highest Negative close price change is -12.35579 % which indicates negative or bad market conditions or any other reasons.\
                 
                 * Average Daily Price change is 0.092%.\
                 
                 * On Average Daily Price Change (STD) (with 68% confidence interval) is +- 1.612 %, therefore, stock is consistant and is stable to invest.\
                 
                 * Average Daily Percentage fluctuation is less.
''')

# Volume Traded over time
st.subheader('Volume Traded over Time')
st.plotly_chart(volume_plot)
