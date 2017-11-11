# from alpha_vantage.timeseries import TimeSeries
# import matplotlib.pyplot as plt
# import pandas as pd


# def overall_graph(ticker1, ticker2, length, interval):
#     pass
# def zoomed_graph(ticker1, ticker2, length, interval):
#     pass
# def find_correlation(ticker1, ticker2, length, interval):
#     t1cost = ts.get_intraday(symbol=ticker1,interval=interval, outputsize='full')
#     t2cost = ts.get_intraday(symbol=ticker2,interval=interval, outputsize='full')
#     return (t1cost)

# ticker1 = 'MSFT'
# ticker2 = 'GOOGL'
# length = 0
# interval = '15min'
# print find_correlation(ticker1, ticker2, length, interval)

# from alpha_vantage.timeseries import TimeSeries
# import matplotlib.pyplot as plt
# import pandas as pd

# ts = TimeSeries(key='XP12DSLMVA2QP4MO', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='V',interval='15min', outputsize='compact')
# data['close'].plot()
# print(data.describe())
# plt.title('Visa stock data stuff')
# plt.show()