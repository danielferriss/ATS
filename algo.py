from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import base64
import numpy as np
import io
from flask import make_response, send_file

################ Directs data to correct function based on length ################
def stockchart(symbol1, symbol2, length):
    if length == '1day':
        return stockchart_1day(symbol1, symbol2)

    if length == '1week':
        return stockchart_1weekday(symbol1, symbol2)

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

############### Graphs inputted data and encodes to return to site ################
def graph(symbol1, symbol2, data, data2, meta_data, ts):
    fig, ax1 = plt.subplots()
    ax1.plot(data, 'b')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel(symbol1.upper(), color = 'b')

    ax2 = ax1.twinx()
    ax2.plot(data2, 'g')
    ax2.set_ylabel(symbol2.upper(), color = 'g')
    plt.title('Stock Graph of ' + symbol1.upper() + ' and ' + symbol2.upper())
    ax1.locator_params(nbins=10, axis='x')
    for tick in ax1.get_xticklabels():
        tick.set_rotation(90)
    
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    fig.tight_layout()
    canvas.print_png(output)
    response = base64.b64encode(output.getvalue()).decode('ascii')
    return response

################ 1 day function ################
def stockchart_1day(symbol1, symbol2):
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
    data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
    return graph(symbol1, symbol2, data, data2, meta_data, ts)
    
################ 1 week function ################
def stockchart_1week(symbol1, symbol2):
    # Make the interval be hourly
    return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 4 week function ################
def stockchart_4week(symbol1, symbol2):
    # Make the interval be hourly
    return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 3 month function ################
def stockchart_3month(symbol1, symbol2):
    # Make the interval be daily
    return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 1 year function ################
def stockchart_1year(symbol1, symbol2):
    # Make the interval be daily
    return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 5 year function ################
def stockchart_5year(symbol1, symbol2):
    # Make the interval be weekly
    return graph(symbol1, symbol2, data, data2, meta_data, ts)
