from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys
import numpy as np

ticker1 = 'msft'
ticker2 = 'googl'
interval = '15min'
length = '1day'

def stockchart(symbol1, symbol2):
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol1,interval=interval, outputsize='compact')
    data2, meta_data = ts.get_intraday(symbol=symbol2,interval=interval, outputsize='compact')
    fig, ax1 = plt.subplots()
    ax1.plot(data, 'b')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel(symbol1.upper(), color = 'b')

    ax2 = ax1.twinx()
    ax2.plot(data2, 'g')
    ax2.set_ylabel(symbol2.upper(), color = 'g')
    plt.title('Stock Graph of ' + symbol1.upper() + ' and ' + symbol2.upper())
    plt.show()
    print(data.describe())

stockchart(ticker1,ticker2)

