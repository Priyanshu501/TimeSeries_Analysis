''' Contains all the Visualizations '''
import numpy as np
import plotly as px
import plotly.express as exp
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import pacf, acf
import pages.src.utilities as utl #pylint: disable=import-error

#----- EDA: Histograms/Density Plot -----#

# Distribution of Closing Prices
density_plot = px.hist_frame(utl.df, x='Close', nbins=30)
density_plot.update_layout(title = 'Distribution of Closing Prices')

#----- EDA: Line Plots -----#

# Stock Data Overview

## Initializing Subplots
line_plots = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=('Open Prices', 'High Prices', 'Low Prices', 'Close Prices')
)
## Plot: Open Prices
line_plots.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Open'],
        mode='lines',
        name='Open'
    ),
    row=1,
    col=1
)
## Plot: High Prices
line_plots.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['High'],
        mode='lines',
        name='High'
    ),
    row=1,
    col=2
)
## Plot: Low Prices
line_plots.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Low'],
        mode='lines',
        name='Low'
    ),
    row=2,
    col=1
)
## Plot: Close Prices
line_plots.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Close'],
        mode='lines',
        name='Close'
    ),
    row=2,
    col=2
)

## Update xaxis properties
line_plots.update_xaxes(title_text="Date", row=1, col=1)
line_plots.update_xaxes(title_text="Date", row=1, col=2)
line_plots.update_xaxes(title_text="Date", row=2, col=1)
line_plots.update_xaxes(title_text="Date", row=2, col=2)

## Update yaxis properties
line_plots.update_yaxes(title_text="Open", row=1, col=1)
line_plots.update_yaxes(title_text="High", row=1, col=2)
line_plots.update_yaxes(title_text="Low", row=2, col=1)
line_plots.update_yaxes(title_text="Close", row=2, col=2)

## Update title and height
line_plots.update_layout(title_text = 'Stock Data Overview', height=700)

# Volatitlity between 2012-2013 and 2016-2017

## Initializing Subplots
line_plots2 = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=('AAPL Close Price (2012-2013)', 'AAPL Close Price (2016-2017)')
)
## Filtering Data
temp1 = utl.df['2012-01-01':'2013-12-31']
temp2 = utl.df['2016-01-01':'2017-12-31']

## Plot: AAPL Close Price (2012-2013)
line_plots2.add_trace(
    go.Scatter(
        x=temp1.index,
        y=temp1['Close'],
        mode='lines',
        name='Close Prices from 2012 to 2013'
    ),
    row=1,
    col=1,
)
## Plot: AAPL Close Price (2016-2017)
line_plots2.add_trace(
    go.Scatter(
        x=temp2.index,
        y=temp2['Close'],
        mode='lines',
        name='Close Prices from 2016 to 2017'
    ),
    row=2,
    col=1
)

## Update xaxis properties
line_plots2.update_xaxes(title_text="Date", row=1, col=1)
line_plots2.update_xaxes(title_text="Date", row=2, col=1)

## Update yaxis properties
line_plots2.update_yaxes(title_text="Close", row=1, col=1)
line_plots2.update_yaxes(title_text="Close", row=2, col=1)

## Update title and height
line_plots2.update_layout(title_text = 'Volatility between 2012-2013 and 2016-2017', height = 700)

# Precentage Change in Close Price

## Calculating Percentage Change
utl.df['pct_change'] = utl.df['Close'].pct_change(periods=1) * 100

## Line Plot
pct_change = px.plot(utl.df['pct_change'], kind='line')
pct_change.update_layout(title = 'Percentage Change in Close Price')
pct_change.update_xaxes(title= 'Date')
pct_change.update_yaxes(title='Percentage Change')

## KDE Plot
kde_plot = px.hist_frame(utl.df, x='pct_change', nbins=30)
kde_plot.update_layout(title = 'Distribution of Percentage Change in Close Price')
kde_plot.update_xaxes(title= 'Percentage Change')
kde_plot.update_yaxes(title='Distribution')

#----- EDA: Volume Plots -----#

# Volume Traded over Time

## Line Plot
volume_plot = px.plot(utl.df['Volume'], kind='line')
volume_plot.update_layout(title = 'Volume Traded over Time')
volume_plot.update_xaxes(title= 'Date')
volume_plot.update_yaxes(title='Volume')

# Correlation in Volume and Close Price

## Scatter Plot
volume_correlation = exp.scatter(
    utl.df,
    x='Volume',
    y='Close',
    title='Correlation between Volume and Close Price',
    labels={'Volume': 'Volume', 'Close': 'Close Price'},
)

#----- EDA: Close vs Adj. Close Price -----#

# AAPL Close Price vs Adj Close

## Initializing Graph Object Plots
price_plot = go.Figure()

## Trace: Close Price
price_plot.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Close'],
        mode='lines',
        name='Close Price',
    )
)
## Trace: Adj. Close
price_plot.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Adj Close'],
        mode='lines',
        name='Adj. Close'
    )
)

## Update axes titles
price_plot.update_xaxes(title='Date')
price_plot.update_yaxes(title='Price')

## Update title
price_plot.update_layout(title_text = 'AAPL Close Price vs Adj Close')


#----- EDA: Significant Adjustments -----#

# Comparision of Close and Adj. Prices

## Initializing Subplots
diff_in_prices = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=('Close vs Adj. Close', 'Difference between Close and Adj Close')
)
## Plot: Close vs Adj.Close

### Trace: Close Prices
diff_in_prices.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Close'],
        mode='lines',
        name='Close Prices'
    ),
    row=1,
    col=1,
)
### Trace: Adj Close Prices
diff_in_prices.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=utl.df['Adj Close'],
        mode='lines',
        name='Adj Close Prices'
    ),
    row=1,
    col=1,
)

## Plot: Difference between Close and Adj Close

### Calculating Difference in Close between Adj Close
temp3 = utl.df['Close'] - utl.df['Adj Close']

### Plot: Difference
diff_in_prices.add_trace(
    go.Scatter(
        x=utl.df.index,
        y=temp3,
        mode='lines',
        name='Difference (Close - Adj Close)'
    ),
    row=2,
    col=1
)

## Update xaxis properties
diff_in_prices.update_xaxes(title_text="Date", row=1, col=1)
diff_in_prices.update_xaxes(title_text="Date", row=2, col=1)

## Update yaxis properties
diff_in_prices.update_yaxes(title_text="Close", row=1, col=1)
diff_in_prices.update_yaxes(title_text="Difference", row=2, col=1)

## Update title and height
diff_in_prices.update_layout(title_text = 'Comparision of Close and Adj. Prices', height = 700)

#----- EDA: Decomposition of Timeseries -----#

# Calculating Decompositions
decompositions = seasonal_decompose(utl.df['Close'], model='additive', period=365)

# Plot: Trend
trend = exp.line(decompositions.trend)

## Update xaxis properties
trend.update_xaxes(title_text = 'Date')
trend.update_yaxes(title_text='Price')

## Update title
trend.update_layout(title_text='Trend')

# Plot: Seasonality
seasonality = exp.line(decompositions.seasonal)

## Update xaxis properties
seasonality.update_xaxes(title_text = 'Date')

## Update Title
seasonality.update_layout(title_text='Seasonality')

# Plot: Cyclic Variations

## Calculating Cyclic Variations
cyclic_variation = decompositions.trend - decompositions.trend.rolling(window=365, center=True).mean() # pylint: disable=line-too-long

## Line Plot
cyclic = exp.line(cyclic_variation)

## Update xaxis properties
cyclic.update_xaxes(title_text = 'Date')

## Update Title
cyclic.update_layout(title_text='Cyclic Variations')

# Plot: Residuals/Noise
residuals = exp.line(decompositions.resid)

## Update xaxis properties
residuals.update_xaxes(title_text = 'Date')

## Update Title
residuals.update_layout(title_text='Residuals (Noise)')

#----- ARIMA: ACF and PACF Plots -----#

def autocorrelation_plot(series, plot_pacf=False, alpha=0.05):
    ''' Creates an ACF or PACF plot '''

    # Toggle to plot ACF or PACF
    if plot_pacf:
        corr_array = pacf(series['Close'].diff().dropna(), alpha=alpha)
    else:
        corr_array = acf(series['Close'].diff().dropna(), alpha=alpha)

    # Filtering required data
    lower_y = corr_array[1][:,0] - corr_array[0]
    upper_y = corr_array[1][:,1] - corr_array[0]

    # Initializing Graph Objects Plot
    fig = go.Figure()

    # Plotting Lines using Loop
    for x in range(len(corr_array[0])):
        fig.add_scatter(
            x=(x,x),
            y=(0,corr_array[0][x]),
            mode='lines',
            line_color='#3f3f3f'
            )

    # Plotting Markers
    fig.add_scatter(
        x=np.arange(len(corr_array[0])),
        y=corr_array[0],
        mode='markers',
        marker_color='#1f77b4',
        marker_size=12
        )

    # Creating Lag Plot Area: Positive Scale
    fig.add_scatter(
        x=np.arange(len(corr_array[0])),
        y=upper_y,
        mode='lines',
        line_color='rgba(255,255,255,0)'
        )

    # Creating Lag Plot Area: Negative Scale
    fig.add_scatter(
        x=np.arange(len(corr_array[0])),
        y=lower_y,
        mode='lines',
        fillcolor='rgba(32, 146, 230,0.3)',
        fill='tonexty',
        line_color='rgba(255,255,255,0)'
        )

    fig.update_traces(showlegend=False)
    fig.update_xaxes(range=[-1,42])
    fig.update_yaxes(zerolinecolor='#000000')

    # Updating Title based on Toggle Value
    if plot_pacf:
        title = 'Partial Autocorrelation (PACF)'
    else:
        title = 'Autocorrelation (ACF)'

    # Plot Title
    fig.update_layout(title=title)

    return fig

#----- Model Evaluation Plot (Train, Test & Forecast) -----#

def model_visulization(train, test, forecast):
    ''' Model Evaluation using Train, Test & Forecasted Values '''

    # Initializing Graph Objects Plot
    fig = go.Figure()

    # Plot: Train Data
    fig.add_trace(
        go.Scatter(
            x=train.index,
            y=train['Close'],
            mode='lines',
            name='Train'
        )
    )
    # Plot: Test Data
    fig.add_trace(
        go.Scatter(
            x=test.index,
            y=test['Close'],
            mode='lines',
            name='Test'
        )
    )
    # Plot: Forecast Data
    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast['Forecast'],
            mode='lines',
            name='Forecasted Values',
            line=dict(dash='dot')
        )
    )

    # Update axes titles
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Price')

    # Update title
    fig.update_layout(title_text = 'Model Evaluation')

    return fig

#----- Model Forecast -----#

def final_forecast(forecast, train=utl.df):
    ''' Visulizes the Forecasted Data '''

    # Initializing Graph Objects Plot
    fig = go.Figure()

    # Plot: Original Data
    fig.add_trace(
        go.Scatter(
            x=train.index,
            y=train['Close'],
            mode='lines',
            name='Original Data'
        )
    )
    # Plot: Forecasted Values
    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast['Forecast'],
            mode='lines',
            name='Forecasted Values',
            line=dict(color='firebrick')
        )
    )

    # Update axes titles
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Price')

    # Update title
    fig.update_layout(title_text = 'Forecast')

    return fig
