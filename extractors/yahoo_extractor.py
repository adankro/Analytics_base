import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf


#yf.pdr_override()
# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list = ['CL=F','BTC-USD', 'DBX', 'DJIA', 'DOW', 'LB', 'EXPE',
               'PXD', 'MCHP', 'CRM', 'JEC', 'NRG', 'HFC', 'NOW', ]
today = date.today()
# We can get data by our choice by giving days bracket
start_date = '2019-01-01'
end_date = today.strftime('%Y-%m-%d')
files = []

def getData(ticker):
    print(ticker)
    data = yf.download(ticker, start=start_date, end=end_date)
    dataname = ticker
    files.append(dataname)
    SaveData(data, dataname)

# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv('./data/yahoo/' + filename +'.csv')


for ticker in ticker_list:
    getData(ticker)
