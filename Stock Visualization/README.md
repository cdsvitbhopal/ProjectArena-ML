# Visualize Stock Market Data With Python Plotly using yfinance api

Welcome to the comprehensive guide on visualizing stock market data using the Plotly library in Python, powered by the Yahoo Finance (yfinance) API.

In the ever-evolving landscape of finance, data visualization has become an essential tool for investors, analysts, and traders alike.

Plotly, a versatile graphing library, combined with the extensive financial data provided by the yfinance API, offers a powerful platform to gain insights and make informed decisions.

The script allows users to input a stock ticker symbol and a date range, and it will then generate a candlestick chart of the stock's historical prices.

## Prerequisites

To run this script, you will need the following:

- Python 3.6 or later
- The yfinance library
- The Plotly library

You can install these dependencies using the following commands:

```
pip install yfinance
pip install plotly
```

## Import Libraries

```python
import yfinance as yf
import plotly.graph_objects as plt
```

## Exploring yfinance API

There are two main modules, the **Ticker()** and the **Download()** module.

The **Ticker()** lets us interact with any stock symbol to get some information on the fly.

```python
apple = yf.Ticker('AAPL')
print(apple)
print(apple.info)
```

> After importing yfinance, we can start a ticker for any stock symbol.  
> I am choosing **AAPL** to create a ticker for **Apple** (line 1).  
> Printing out the ticker itself (line 2) just returns a ticker object that you can further interact with.

Let’s try to **print** _apple.info_ which returns a long list of company & stock information about Apple.

```
 {'address1': 'One Apple Park Way', 'city': 'Cupertino', 'state': 'CA', 'zip': '95014', 'country': 'United States', 'phone': '408 996 1010', 'website': 'https://www.apple.com', 'industry': 'Consumer Electronics', 'industryDisp': 'Consumer Electronics', 'sector': 'Technology', 'sectorDisp': 'Technology', 'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, and HomePod. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.', }

```

There are various more useful _methods_ like

- **apple.actions** providing an overview of past dividends & stock splits
- **apple.history** (period=max) providing historical market data
- **apple.calendar** proving details about the next events
  and much more.

You can find more details on the **_[yfinance documentation](https://pypi.org/project/yfinance/)._**

Let's take a closer look at the **Download()** module. With the download module, we can request detailed stock data for a defined period.

It takes three arguments:

- the ticker name (APPL)
- start & end date or a period (like 1 day)
- an interval (optional)

```python
data = yf.download(tickers='AAPL', period='1d', interval='1m')
print(data)
```

It will render the output like this

![plot-chart](/apple.jpeg)

## Visualization With Python Plotly

```python
import yfinance as yf
import plotly.graph_objs as plt

data = yf.download(tickers='AAPL', period='1d', interval='1m')

fig = plt.Figure(data=[plt.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'Apple Live Market Data')])

fig.show()
```

#### Code Breakdown

> - First, we import yfinance and plotly (lines 1–2) and download the live Apple stock data for the current day with an interval of 1 minute (line 4).
>
> - Now, we can create the Plotly chart already (lines 6–10):
>
> - We create a Plotly Candlestick and use the Datetime (column 1 & index of the data returned by yfinance) as data for the x-axis (line 6)
>
> - As a candlestick needs to get open, high, low & close as inputs, we are taking these values from the yfinance data for the y-axis (lines 7–10).

Now we can already plot the chart and show it in the browser (line 12) and it looks great

![plot-chart](/newplot.png)

> If we compare the chart from Plotly with the charts from Tradingview, it is really accurate.

## Deploy using Voila

What is **Voila**?

> Voila is a Python package that turns Jupyter notebooks into working web sites. It is pretty amazing. Another Python package called Streamlit turns .py-files into websites. Voila does the same that Streamlit does to .py-files, except for Jupyter notebooks.  
> Take a look at [Voila documentation](https://voila.readthedocs.io/en/stable/)

To use voila first you need to install.

You can install these dependencies using the following commands:

```python
 pip install voila
```

#### Test Voila locally

Type the command below into a terminal to run the app locally.

```
voila finance.ipynb
```

> You can acess your app running on **localhost:8866**

## Conclusion

By following these steps, you can visualize stock market data using Python and the Plotly library. This example demonstrated how to create a candlestick chart using data fetched from the yfinance API. Feel free to explore further and customize the visualization based on your requirements.
