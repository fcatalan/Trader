import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
#%matplotlib inline

def get_stock():
     #web.DataReader(stock,'google',start,end)['Close']
    return pd.read_csv('C:/Trader/indicator/goog-2011-yahoofinance.csv')['Close']

def get_high():
    #return web.DataReader(stock,'google',start,end)['High']
    return pd.read_csv('C:/Trader/indicator/goog-2011-yahoofinance.csv')['High']

def get_low():
    #return web.DataReader(stock,'google',start,end)['Low']
    return pd.read_csv('C:/Trader/indicator/goog-2011-yahoofinance.csv')['Low']

dfa = pd.read_csv('C:/Trader/indicator/goog-2011-yahoofinance.csv')

def CCI(close, high, low, n, constant): 
    TP = (high + low + close) / 3 
    CCI = pd.Series((TP - TP.rolling(window=n).mean()) / (constant * TP.rolling(window=n).std()), name = 'CCI_' + str(n)) 
    return CCI

df = pd.DataFrame(get_stock())
df['High'] = get_high()
df['Low'] = get_low()
df['CCI'] = CCI(df['Close'], df['High'], df['Low'], 20, 0.015)
df.tail()

#df.plot(y=['Close'])
df.plot(y=['CCI'])
plt.show()