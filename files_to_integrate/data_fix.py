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

index_value = stock1.index.tolist()

values = stock1.open.tolist()

stock1_dict = {}

for i in range (0, len(index_value)):
    stock1_dict[index_value[i]] = values[i]

index_value = stock2.index.tolist()

values = stock2.open.tolist()

stock2_dict = {}

for i in range (0, len(index_value)):
    stock2_dict[index_value[i]] = values[i]

shared_items = set(stock1_dict.keys()) & set(stock2_dict.keys())

##### need to get rid of the uncommon (basically whats not in shared_items)a

# common_days = pd.merge(stock1, stock2, how = 'inner', on = stock1.index)

# print(common_days)

#filter out values before 10am because they mess up the data
# index_value = data.index.tolist()
# for value in index_value:
#     hours = value[11:13]
#     minutes = value[14:16]
#     data.ix[(hours == "09") & (30 <= int(minutes) < 60)]

# print(data)#     minutes = value[14:16]
# a = ts.keys()

# numpyStock1 = data['close'].as_matrix()
# numpyStock2 = stock2['close'].as_matrix()
