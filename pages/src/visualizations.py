''' Contains all the Visualizations '''
import pandas as pd
import numpy as np
import plotly as px
import plotly.express as exp
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import pacf, acf
import src.utilities as utl #pylint: disable=import-error

# Importing Dataset
data = pd.read_csv('../data/AAPL.csv')
df = utl.preprocessing(data)
stock_data = df

# Line Plots and Histograms
density_plot = px.hist_frame(stock_data, x='Close', nbins=30)
density_plot.update_layout(title = 'Distribution of Closing Prices')

# Observations from Line Plots
line_plots = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=('Open Prices', 'High Prices', 'Low Prices', 'Close Prices')
)

line_plots.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Open'],
        mode='lines',
        name='Open'
    ),
    row=1,
    col=1
)

line_plots.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['High'],
        mode='lines',
        name='High'
    ),
    row=1,
    col=2
)

line_plots.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Low'],
        mode='lines',
        name='Low'
    ),
    row=2,
    col=1
)

line_plots.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Close'],
        mode='lines',
        name='Close'
    ),
    row=2,
    col=2
)

# Update xaxis properties
line_plots.update_xaxes(title_text="Date", row=1, col=1)
line_plots.update_xaxes(title_text="Date", row=1, col=2)
line_plots.update_xaxes(title_text="Date", row=2, col=1)
line_plots.update_xaxes(title_text="Date", row=2, col=2)

# Update yaxis properties
line_plots.update_yaxes(title_text="Open", row=1, col=1)
line_plots.update_yaxes(title_text="High", row=1, col=2)
line_plots.update_yaxes(title_text="Low", row=2, col=1)
line_plots.update_yaxes(title_text="Close", row=2, col=2)

# Update title and height
line_plots.update_layout(title_text = 'Stock Data Overview', height=700)

# Observations from Line Plots 2
line_plots2 = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=('AAPL Close Price (2012-2013)', 'AAPL Close Price (2016-2017)')
)

temp1 = stock_data['2012-01-01':'2013-12-31']
temp2 = stock_data['2016-01-01':'2017-12-31']

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

# Update xaxis properties
line_plots2.update_xaxes(title_text="Date", row=1, col=1)
line_plots2.update_xaxes(title_text="Date", row=2, col=1)

# Update yaxis properties
line_plots2.update_yaxes(title_text="Close", row=1, col=1)
line_plots2.update_yaxes(title_text="Close", row=2, col=1)

# Update title and height
line_plots2.update_layout(title_text = 'Volatility between 2012-2013 and 2016-2017', height = 700)


# Daily Percentage Changes in closing price
stock_data['pct_change'] = stock_data['Close'].pct_change(periods=1) * 100

pct_change = px.plot(stock_data['pct_change'], kind='line')
pct_change.update_layout(title = 'Percentage Change in Close Price')
pct_change.update_xaxes(title= 'Date')
pct_change.update_yaxes(title='Percentage Change')

# KDE Plot
kde_plot = px.hist_frame(stock_data, x='pct_change', nbins=30)
kde_plot.update_layout(title = 'Distribution of Percentage Change in Close Price')
kde_plot.update_xaxes(title= 'Percentage Change')
kde_plot.update_yaxes(title='Distribution')

# Pattern in Volume
volume_plot = px.plot(stock_data['Volume'], kind='line')
volume_plot.update_layout(title = 'Volume Traded over Time')
volume_plot.update_xaxes(title= 'Date')
volume_plot.update_yaxes(title='Volume')

# Correlation in Volume
volume_correlation = exp.scatter(
    stock_data,
    x='Volume',
    y='Close',
    title='Correlation between Volume and Close Price',
    labels={'Volume': 'Volume', 'Close': 'Close Price'},
)

# Close vs Adj. Close Price
price_plot = go.Figure()
price_plot.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Close'],
        mode='lines',
        name='Close Price',
    )
)

price_plot.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Adj Close'],
        mode='lines',
        name='Adj. Close'
    )
)

# Update axes titles
price_plot.update_xaxes(title='Date')
price_plot.update_yaxes(title='Price')

# Update title
price_plot.update_layout(title_text = 'AAPL Close Price vs Adj Close')


# Significant Adjustments
diff_in_prices = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=('"Close" vs "Adj. Close"', 'Difference between Close and Adj Close')
)

diff_in_prices.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Close'],
        mode='lines',
        name='Close Prices'
    ),
    row=1,
    col=1,
)

diff_in_prices.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=stock_data['Adj Close'],
        mode='lines',
        name='Adj Close Prices'
    ),
    row=1,
    col=1,
)

temp3 = stock_data['Close'] - stock_data['Adj Close']

diff_in_prices.add_trace(
    go.Scatter(
        x=stock_data.index,
        y=temp3,
        mode='lines',
        name='Difference (Close - Adj Close)'
    ),
    row=2,
    col=1
)

# Update xaxis properties
diff_in_prices.update_xaxes(title_text="Date", row=1, col=1)
diff_in_prices.update_xaxes(title_text="Date", row=2, col=1)

# Update yaxis properties
diff_in_prices.update_yaxes(title_text="Close", row=1, col=1)
diff_in_prices.update_yaxes(title_text="Difference", row=2, col=1)

# Update title and height
diff_in_prices.update_layout(title_text = 'Comparision of Close and Adj. Prices', height = 700)

# Decomposition Plots
decompositions = seasonal_decompose(stock_data['Close'], model='additive', period=365)

# Decomposition: Trend
trend = exp.line(decompositions.trend)

# Update xaxis properties
trend.update_xaxes(title_text = 'Date')
trend.update_yaxes(title_text='Price')

# Update title
trend.update_layout(title_text='Trend')

# Decomposition: Seasonality
seasonality = exp.line(decompositions.seasonal)

# Update xaxis properties
seasonality.update_xaxes(title_text = 'Date')

# Update Title
seasonality.update_layout(title_text='Seasonality')

# Decomposition: Cyclic Variations
cyclic_variation = decompositions.trend - decompositions.trend.rolling(window=365, center=True).mean() # pylint: disable=line-too-long

cyclic = exp.line(cyclic_variation)

# Update xaxis properties
cyclic.update_xaxes(title_text = 'Date')

# Update Title
cyclic.update_layout(title_text='Cyclic Variations')

# Decomposition: Residuals/Noise
residuals = exp.line(decompositions.resid)

# Update xaxis properties
residuals.update_xaxes(title_text = 'Date')

# Update Title
residuals.update_layout(title_text='Residuals (Noise)')

def autocorrelation_plot(series, plot_pacf=False, alpha=0.05):
    ''' Creates an ACF or PACF plot '''
    if plot_pacf:
        corr_array = pacf(series['Close'].diff().dropna(), alpha=alpha)
    else:
        corr_array = acf(series['Close'].diff().dropna(), alpha=alpha)

    lower_y = corr_array[1][:,0] - corr_array[0]
    upper_y = corr_array[1][:,1] - corr_array[0]

    fig = go.Figure()

    for x in range(len(corr_array[0])):
        fig.add_scatter(
            x=(x,x),
            y=(0,corr_array[0][x]),
            mode='lines',
            line_color='#3f3f3f'
            )

    fig.add_scatter(
        x=np.arange(len(corr_array[0])),
        y=corr_array[0],
        mode='markers',
        marker_color='#1f77b4',
        marker_size=12
        )

    fig.add_scatter(
        x=np.arange(len(corr_array[0])),
        y=upper_y,
        mode='lines',
        line_color='rgba(255,255,255,0)'
        )

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

    if plot_pacf:
        title = 'Partial Autocorrelation (PACF)'
    else:
        title = 'Autocorrelation (ACF)'

    fig.update_layout(title=title)

    return fig
