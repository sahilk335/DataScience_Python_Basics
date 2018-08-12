# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:30:56 2018

@author: sahil

Title : Styles

You can see all of the available styles you currently have by doing:

print(plt.style.available)
For me, that gives ['bmh', 'dark_background', 'ggplot', 'fivethirtyeight', 'grayscale']

Let's try out the dark_background:

style.use('dark_background')

"""
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from matplotlib import style


style.use('ggplot')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock) :
    print(plt.style.available)
    print(plt.__file__)
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
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
    ax1.plot(date,Low)
    ax1.plot(date,Adjusted_close)
    #plt.plot_date(date, Close,'-', label='Price') 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

graph_data("TESLA")


