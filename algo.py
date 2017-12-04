from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import base64
import numpy as np
import io
from flask import make_response, send_file
import pandas as pd

################ check whether or not the symbol is in the markets ###############
def symbols():
    s = pd.read_csv("symbols.csv")
    s.columns = ["Symbol"]
    return list(s.Symbol)

################ Directs data to correct function based on length ################
def stockchart(symbol1, symbol2, length):
    if length == '1day':
        return stockchart_1day(symbol1, symbol2)
    
    if length == '1week':
        return stockchart_1week(symbol1, symbol2)
    
    if length == '4week':
        return stockchart_4week(symbol1, symbol2)
    
    if length == '3month':
        return stockchart_3month(symbol1, symbol2)
    
    if length == '1year':
        return stockchart_1year(symbol1, symbol2)
    
    if length == '5year':
        return stockchart_5year(symbol1, symbol2)
    else:
        return stockchart_1day(symbol1, symbol2)

def modify_data(data):
    data.drop(['high'], axis = 1, inplace = True)
    data.drop(['low'], axis = 1, inplace = True)
    data.drop(['close'], axis = 1, inplace = True)
    data.drop(['volume'], axis = 1, inplace = True)
    
    return data

############### Graphs inputted data and encodes to return to site ################
def graph(symbol1, symbol2, data, data2, meta_data, ts, title):
    fig, ax1 = plt.subplots()
    ax1.plot(data, 'b')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel(symbol1.upper(), color = 'b')
    
    ax2 = ax1.twinx()
    ax2.plot(data2, 'g')
    ax2.set_ylabel(symbol2.upper(), color = 'g')
    plt.title(symbol1.upper() + ' and ' + symbol2.upper() + ' (' + title + ')')
    for tick in ax1.get_xticklabels():
        tick.set_rotation(90)
    
    if title == '4 Weeks':
        for label in ax1.xaxis.get_ticklabels()[1::2]:
            label.set_visible(False)
    if title == '3 Months' or title == '1 Year':
        for label in ax1.xaxis.get_ticklabels()[1::3]:
            label.set_visible(False)
        for label in ax1.xaxis.get_ticklabels()[2::3]:
            label.set_visible(False)
    if title == '5 Years':
        for label in ax1.xaxis.get_ticklabels()[1::4]:
            label.set_visible(False)
        for label in ax1.xaxis.get_ticklabels()[2::4]:
            label.set_visible(False)
        for label in ax1.xaxis.get_ticklabels()[3::4]:
            label.set_visible(False)

    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    fig.tight_layout()
    canvas.print_png(output)
    response = base64.b64encode(output.getvalue()).decode('ascii')
    return response

################ 1 day function ################
def stockchart_1day(symbol1, symbol2):
    title = '1 Day'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_intraday(symbol=symbol1,interval='60min', outputsize='compact')
    data2, meta_data = ts.get_intraday(symbol=symbol2,interval='60min', outputsize='compact')
    print(data1)
    newdata1 = data1.drop(data1.index[0:59])
    newdata2 = data2.drop(data2.index[0:59])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    return graph(symbol1, symbol2, newdata1,  newdata2, meta_data, ts, '24 Hours')

################ 1 week function ################
def stockchart_1week(symbol1, symbol2):
    # Make the interval be hourly
    title = '1 Week'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_daily(symbol=symbol1, outputsize='compact')
    data2, meta_data = ts.get_daily(symbol=symbol2, outputsize='compact')
    newdata1 = data1.drop(data1.index[0:93])
    newdata2 = data2.drop(data2.index[0:93])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)

################ 4 week function ################
def stockchart_4week(symbol1, symbol2):
    # Make the interval be hourly
    title = '4 Weeks'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_daily(symbol=symbol1, outputsize='compact')
    data2, meta_data = ts.get_daily(symbol=symbol2, outputsize='compact')
    newdata1 = data1.drop(data1.index[0:len(data1.index) - 23])
    newdata2 = data2.drop(data2.index[0:len(data2.index) - 23])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)

################ 3 month function ################
def stockchart_3month(symbol1, symbol2):
    # Make the interval be daily
    title = '3 Months'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_daily(symbol=symbol1, outputsize='compact')
    data2, meta_data = ts.get_daily(symbol=symbol2, outputsize='compact')
    
    newdata1 = data1.drop(data1.index[0:36])
    newdata2 = data2.drop(data2.index[0:36])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    #print(newdata1)
    return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)

################ 1 year function ################
def stockchart_1year(symbol1, symbol2):
    # Make the interval be daily
    title = '1 Year'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_weekly(symbol=symbol1)
    data2, meta_data = ts.get_weekly(symbol=symbol2)
    
    newdata1 = data1.drop(data1.index[0:len(data1.index) - 53])
    newdata2 = data2.drop(data2.index[0:len(data2.index) - 53])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    #print(newdata1)
    return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)

################ 5 year function ################
def stockchart_5year(symbol1, symbol2):
    title = '5 Years'
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data1, meta_data = ts.get_monthly(symbol=symbol1)
    data2, meta_data = ts.get_monthly(symbol=symbol2)
    
    newdata1 = data1.drop(data1.index[0:len(data1.index) - 62])
    newdata2 = data2.drop(data2.index[0:len(data2.index) - 62])
    
    newdata1 = modify_data(newdata1)
    newdata2 = modify_data(newdata2)
    
    #print(newnewdata1)
    return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)
