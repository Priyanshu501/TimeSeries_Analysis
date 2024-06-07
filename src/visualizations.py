import pandas as pd
import plotly as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from utilities import preprocessing

# Importing Dataset
data = pd.read_csv('../data/AAPL.csv')
stock_data = preprocessing(data)

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
line_plots2.update_xaxes(title_text="Date", row=1, col=1)

# Update yaxis properties
line_plots2.update_yaxes(title_text="Close", row=2, col=1)
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