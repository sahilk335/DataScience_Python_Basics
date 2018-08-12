# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 06:11:57 2018

@author: sahil

Title : 
"""
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock) :
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    
    source_code=urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data=[]
    split_source=source_code.split('\n')
    
    for line in split_source[1:] :
        split_line=line.split(',')
        # As we see the data, we have observed that
        if len(split_line)==7 :
            if 'values' not in line :
                stock_data.append(line)

    date,Open,High,Low,Close,Adjusted_close,Volume = np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True,
                                                           converters={0: bytespdate2num('%Y-%m-%d')})
    plt.plot_date(date, Close,'-', label='Price') 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

graph_data("TESLA")

