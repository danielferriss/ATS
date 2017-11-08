from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys

def stockchart(symbol1, symbol2):
    ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
    data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
    data['close'].plot()
    data2['close'].plot()
    plt.title('Testing testing 123')
    plt.show()

stockchart('msft','googl')
