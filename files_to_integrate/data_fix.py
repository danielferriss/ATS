import scipy.stats as sp
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pandas as pd

ticker1 = "VG"
ticker2 = "BABA"
time_interval = '1min'
ts = TimeSeries(key='XP12DSLMVA2QP4MO', output_format='pandas')
stock1, meta_data = ts.get_intraday(symbol = ticker1,interval=time_interval, outputsize='full')
stock2, meta_data = ts.get_intraday(symbol= ticker2,interval=time_interval, outputsize='full')


stock1.drop(['high'],   axis=1, inplace=True)
stock1.drop(['low'],    axis=1, inplace=True)
stock1.drop(['close'],  axis=1, inplace=True)
stock1.drop(['volume'], axis=1, inplace=True)

stock2.drop(['high'],   axis=1, inplace=True)
stock2.drop(['low'],    axis=1, inplace=True)
stock2.drop(['close'],  axis=1, inplace=True)
stock2.drop(['volume'], axis=1, inplace=True)


stock1_index = stock1.index.tolist()
stock2_index = stock2.index.tolist()

shared_items = list(set(stock1_index).intersection(stock2_index))


for elem in stock1_index:
	if elem not in shared_items:
		stock1.drop(elem, inplace=True)

for elem in stock2_index:
	if elem not in shared_items:
		stock2.drop(elem, inplace=True)


print(stock1)
print(stock2)

