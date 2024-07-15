## Introduction

This project provides a comprehensive analysis and forecast of Apple Stock Prices, utilizing historical data and advanced statistical models and neural networks.

## Objective

Primary objective is to forecast the following 30 days of Stock Prices. To achieve this, a variety of statistical and deep learning models are implemented. Each model is briefly explained in individual notebooks, providing insights into their methodologies, strengths, and limitations.

## Analysis and Models Implemented

### Exploratory Data Analysis (EDA):

A thorough exploration of historical stock prices, examining trends, seasonality, and other time series characteristics. This analysis sets the foundation for building robust forecasting models.

### Forecasting Models:

#### Statistical Models:
* **ARIMA (AutoRegressive Integrated Moving Average)**: A popular statistical method for time series forecasting.

* **SARIMA (Seasonal AutoRegressive Integrated Moving Average)**: It is a powerful extension of ARIMA that captures seasonality in time series data.

* **Exponential Smoothing**: Methods like Holt-Winters to captures trends and seasonality.

* **Prophet**: Prophet is an open-source tool from Facebook used for forecasting time series data, based on a decomposable additive model where non-linear trends fit with seasonality.

* **GARCH**: The GARCH model effectively captures the volatility clustering observed in financial time series data.

#### Deep Learning Models:
* **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) well-suited for sequential data.

* **GRU (Gated Recurrent Unit)**: Another RNN variant that is simpler and faster than LSTM.
