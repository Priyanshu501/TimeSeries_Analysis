''' Exploratory Data Analysis ''' # pylint: disable=invalid-name
import streamlit as st
import pages.src.utilities as utl
import pages.src.visualizations as vis

st.set_page_config(page_title='Exploratory Data Analysis')

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

st.dataframe(utl.df, use_container_width=True)

# Statistical Description
st.header('Statistical Overview')
st.write(utl.df.describe())

st.write('Key Oberservations: (Open, High, Low, Close)')
st.write('''
         * Average closely falls around 126 to 128.\
         
         * Standard Deviation is around 50 to 51. Indicating consistent fluctuations in the stock's price throughout the trading day.\
         
         * Highest recorded price is 291.5 and Lowest price is 55.0. Indicating High Variability in prices.
         ''')
st.write('Key Observations: (Volume)')
st.write('''
         * Average Trading Volume is approximately 59.5 million shares.\
         
         * Standard Deviation if 46.8 million.\
         
         * Highest Recorded Volume of 376.53 million and Lowest is 11.36 million.\
         
         * High Variabilit, Reflecting periods of both very high and very low trading activitiy.\
                               
         ''')

# Visualizations
st.header('Visualizations')

# Density Plot
st.subheader('Line Plots and Histograms')
st.plotly_chart(vis.density_plot, use_container_width=True)

st.write('''
        Observations:\
        
        * Distribution is right-skewed with a long tail towards higher prices, this indicates positive price changes are more frequent.\
        
        * There is significant variability in the closing prices over the time period.
''')

# Stock Data Overview
st.subheader('Observations from Line Plots' )
st.plotly_chart(vis.line_plots, use_container_width=True)

st.write('''
                     Interpretations:\
                     
                     * Overall strong consistently upward trend. Indicating overall growth and Increasing value over the period.\
                     
                     * Overall High Variability in Price Ranges.\
                     
                     * As we can see all line plots follow a consistent pattern
''')

st.plotly_chart(vis.line_plots2, use_container_width=True)

st.write('''
                      Interpretations:\
                      
                      * **Volatility**: The 2012-2013 period was marked by higher volatility compared to 2016-2017.

                      * **Recovery and Growth**: While 2012-2013 saw a sharp decline followed by a recovery, 2016-2017 was characterized by steady growth, indicating a period of sustained positive performance for Apple stock.
''')

# Daily Percentage Changes in Closing Prices
st.plotly_chart(vis.pct_change, use_container_width=True)
st.plotly_chart(vis.kde_plot, use_container_width=True)

st.write('''
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
st.plotly_chart(vis.volume_plot, use_container_width=True)

st.write('''
                 Interpretations:\
                 
                 * Range of Volume from 11.3M to 376.5M.\
                 
                 * The trading volume experienced significant fluctuations in 2012, indicating periods of high trading activity.\
                 
                 * As we see, Starting from 2017, there is a noticable decrease in trading volume, results reduced fluctuations, suggesting more stable trading activity in recent years.\
                 
                 * As trading volume increases, the closing price tends to decrease, suggesting selling pressure.
''')

st.plotly_chart(vis.volume_correlation, use_container_width=True)

st.write('''
                             Interpretations:\
                             
                             * Negative Correlation: As trading volume increases, the closing price tends to decrease, suggesting selling pressure.\

                             * High trading volumes are associated with lower closing prices.
''')

# Close Prices vs Adj Close Prices
st.subheader('Close Prices vs Adj. Close Prices')
st.plotly_chart(vis.price_plot, use_container_width=True)

st.write('''
                  Interpretations:\
                  
                  * The 'Adj Close' accounts for dividends and stock splits.\
                  
                  * Close price shows actual transaction price, whereas Adj. Close reflects the true value after accounting for corporate actions.
''')

# Significant Adjustments
st.subheader('Significant Adjustements')
st.plotly_chart(vis.diff_in_prices, use_container_width=True)

st.write('''
                 Observations:\
                 
                 * Adjustments represent impact of dividends and stock splits over the period.\
                 
                 * There are Significant Adjustments around 2012-2013.\
                 
                 * Decrease in the Latter years, indicate fewer major corporate actions.
''')

# Decomposition of Time Series
st.subheader('Decomposition of TimeSeries')
st.plotly_chart(vis.trend, use_container_width=True)

st.write('''
                          Interpretation:\

                          * The trend component captures the long-term progression of the series. It shows the general direction in which the data is moving over a long period, ignoring short-term fluctuations and noise.\

                          * The trend line is generally upward from 2012 to 2020, indicating a consistent long-term increase in the AAPL stock price. There are periods of acceleration, especially from 2017 onward, where the stock price increases at a faster rate.
''')

st.plotly_chart(vis.seasonality, use_container_width=True)

st.write('''
                          Interpretation:\

                          * Seasonality refers to the repeated patterns or cycles observed at regular intervals due to seasonal factors. This component is consistent and predictable over the time period.\

                          * The seasonal component shows a regular, recurring pattern on an annual basis. There are noticeable peaks and troughs each year, indicating that certain times of the year consistently experience higher or lower prices. This pattern repeats roughly every year, showing the impact of seasonal factors on the stock price.
''')

st.plotly_chart(vis.cyclic, use_container_width=True)

st.write('''
                          Interpretation:\

                          * Cyclic Variations capture fluctuations that occur at irregular intervals, often influenced by economic cycles, market conditions, or other external factors. Unlike seasonality, cyclic variations do not have a fixed period.\

                          * The cyclic component shows longer-term fluctuations that are not as regular as seasonal effects. For instance, there is a noticeable cyclic peak around 2018 and a trough around 2015, indicating periods of economic or market cycles affecting the stock price.
''')

st.plotly_chart(vis.residuals, use_container_width=True)

st.write('''
                          Interpretation:\

                          * The residual component captures the remaining variability in the data after removing the trend, seasonal, and cyclic components. It represents the irregular, random fluctuations in the series.\

                          * The residuals show high-frequency variability that does not follow any predictable pattern. Periods with larger residuals indicate times of higher volatility or unexpected events impacting the stock price. For example, there is significant noise in the data around 2018 and again towards the end of 2019.
''')
