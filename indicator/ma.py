# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:47:21 2018
@author: peirmah
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('C:/Trader/indicator/goog-2011-yahoofinance.csv')

def Exponential_Moving_Average(df, n):
    EMA = []
    j = 1
    #get n sma first and calculate the next n period ema
    sma = sum(df[:n]) / n
    multiplier = 2 / float(1 + n)
    EMA.append(sma)
    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    EMA.append(( ( df.iloc[n] - sma) * multiplier) + sma)    
    #print (ema)
    #now calculate the rest of the values
    for i in df.iloc[n+1:]:
        tmp = ( (i - EMA[j]) * multiplier) + EMA[j]
        #print(i, "|", ema[j], "|", multiplier, "|", ema[j], "|", "=", "|", "{0:.2f}".format(tmp))
        j = j + 1
        EMA.append(tmp)
     #print(EMA)   
    return EMA
        
#Exponential_Moving_Average((df['Adj Close']),10)
EMA = Exponential_Moving_Average((df['Adj Close']),10)
plt.plot(EMA,label='EMA')
plt.plot((df['Adj Close']),label='Share Price')
plt.xlabel('Date')
plt.ylabel('USD')
plt.legend()
plt.show()