import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import scipy.optimize as opt
from pydoc import help
from scipy.stats.stats import pearsonr


ticker1 = "VG"
ticker2 = "BABA"
time_interval = '15min'
ts = TimeSeries(key='XP12DSLMVA2QP4MO', output_format='pandas')
data, meta_data = ts.get_intraday(symbol = ticker1,interval=time_interval, outputsize='full')
stock2, meta_data = ts.get_intraday(symbol= ticker2,interval=time_interval, outputsize='full')


def fix_data(stock1, stock2):
    stock1.drop(['high'],   axis=1, inplace=True)
    stock1.drop(['low'],    axis=1, inplace=True)
    stock1.drop(['open'],  axis=1, inplace=True)
    stock1.drop(['volume'], axis=1, inplace=True)

    stock2.drop(['high'],   axis=1, inplace=True)
    stock2.drop(['low'],    axis=1, inplace=True)
    stock2.drop(['open'],  axis=1, inplace=True)
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

    return (stock1, stock2)

def convert_to_slopes(arr_vals):
    slopes = []
    prev = 0
    next = 0
    size = len(numpyStock1)
    for index in range(1, len(arr_vals) - 2, 1):
        prev = arr_vals[index - 1]
        next = arr_vals[index + 1]
        slope = next - prev
        if slope > 0:
            slopes.append(1)
        else:
            slopes.append(-1)
    return slopes


#cost function
def calc_cost(stock1, stock2):
    cost = np.corrcoef(stock1, stock2)[0,1]
    return cost


    



#minimize cost (finding optimial time shift)
def optimal_time_shift():
    cost = calc_cost(slopes1, slopes2)
    result =  opt.minimize(cost, slopes1)
    return result
    


tuplea = fix_data(data, stock2)
#filter out values before 10am because they mess up the data
# index_value = data.index
# hours = index_value.str[11:13]
# minutes = index_value.str[14:16]
# df.ix[(hours == "09") & (30 <= minutes < 60)]

# a = ts.keys()

#filter out values before 10am because they mess up the data
# index_value = data.index
# hours = int(index_value.str[11:13])
# minutes = int(index_value.str[14:16])
# data.ix[(hours == "09") & (30 <= minutes < 60)]

numpyStock1 = tuplea[0].as_matrix()
numpyStock2 = tuplea[1].as_matrix()

slopes1 = np.array(convert_to_slopes(numpyStock1))
slopes2 = np.array(convert_to_slopes(numpyStock2))

cost = calc_cost(slopes1, slopes2)
#gets the first 5 vals
new_cost = calc_cost(slopes1, slopes2)
#gets descriptive stats
cost = 999999999999
best = None

length = len(slopes2)
for shift in range(length -1):
    if calc_cost(slopes2[shift:length-1], slopes1[0:length -1 - shift]) < cost:
        best = shift
        cost = calc_cost(slopes2[shift:length-1], slopes1[0:length -1]) < cost

print(shift)






