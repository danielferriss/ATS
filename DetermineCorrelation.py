import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ticker1 = "GS"
ticker2 = "MS"
time_interval = '15min'
ts = TimeSeries(key='XP12DSLMVA2QP4MO', output_format='pandas')
data, meta_data = ts.get_intraday(symbol = ticker1,interval=time_interval, outputsize='full')
stock2, meta_data = ts.get_intraday(symbol= ticker2,interval=time_interval, outputsize='full')
# print(stock2.describe())
# print(data.describe())
print(data['open'].corr(stock2['open']))


file_name = "C:\\users\\anmol\\Documents\\DataFiles\\machinedata1.csv"
data = pd.read_csv(file_name, header=None, names = ['Population','Profit'])

#gets the first 5 vals
data.head()

#gets descriptive stats
data.describe()




