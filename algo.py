from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import base64
import numpy as np
import io
import pandas as pd
from flask import make_response, send_file


################ Checks if input is a stock ################
def symbols():
	s = pd.read_csv("files_to_integrate/readcolumn/symbols.csv")
	s.columns = ["Symbol"]
	return list(s.Symbol)

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
def graph(symbol1, symbol2, data, data2, meta_data, ts, title):
	fig, ax1 = plt.subplots()
	ax1.plot(data, 'b')
	ax1.set_xlabel('Time(s)')
	ax1.set_ylabel(symbol1.upper(), color = 'b')
	ax2 = ax1.twinx()
	ax2.plot(data2, 'g')
	ax2.set_ylabel(symbol2.upper(), color = 'g')
	plt.title('Stock Value of ' + symbol1.upper() + ' and ' + symbol2.upper() + ' for ' + title +'\n ' + data.index.values[0] + ' - ' + data.index.values[len(data.index)-1])
	ax1.locator_params(nbins=24, axis='x')
	# data.to_csv("data_dataframe", sep='\t')
	# we dont want to write files
	for tick in ax1.get_xticklabels():
		tick.set_rotation(90)
	
	# plt.show()

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
	newdata1 = data1.drop(data1.index[0:59])
	newdata2 = data2.drop(data2.index[0:59])
	# print (newdata1)
	# print (newdata2)
	return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, '24 Hours')
	
################ 1 week function ################
def stockchart_1week(symbol1, symbol2):
	# Make the interval be hourly
	title = '1 Week'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_weekly(symbol=symbol1)
	data2, meta_data = ts.get_weekly(symbol=symbol2)
	return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 4 week function ################
def stockchart_4week(symbol1, symbol2):
	# Make the interval be hourly
	title = '4 Weeks'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_monthly(symbol=symbol1)
	data2, meta_data = ts.get_monthly(symbol=symbol2)
	return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 3 month function ################
def stockchart_3month(symbol1, symbol2):
	# Make the interval be daily
	title = '3 Months'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
	data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
	return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 1 year function ################
def stockchart_1year(symbol1, symbol2):
	# Make the interval be daily
	title = '1 Year'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
	data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
	return graph(symbol1, symbol2, data, data2, meta_data, ts)

################ 5 year function ################
def stockchart_5year(symbol1, symbol2):
	# Make the interval be weekly
	title = '5 Years'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
	data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
	return graph(symbol1, symbol2, data, data2, meta_data, ts)
