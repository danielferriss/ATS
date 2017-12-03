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
def graph(symbol1, symbol2, data, data2, meta_data, ts, title):
	fig, ax1 = plt.subplots()
	ax1.plot(data, 'b')
	ax1.set_xlabel('Time(s)')
	ax1.set_ylabel(symbol1.upper(), color = 'b')

	ax2 = ax1.twinx()
	ax2.plot(data2, 'g')
	ax2.set_ylabel(symbol2.upper(), color = 'g')
	plt.title(symbol1.upper() + ' and ' + symbol2.upper() + ' (' + title + ')')
	ax1.locator_params(nbins=16, axis='x')
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
	title = '1 Day'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data1, meta_data = ts.get_intraday(symbol=symbol1,interval='60min', outputsize='compact')
	data2, meta_data = ts.get_intraday(symbol=symbol2,interval='60min', outputsize='compact')
	print(data1)
	newdata1 = data1.drop(data1.index[0:59])
	newdata2 = data2.drop(data2.index[0:59])
	newnewdata1 = newdata1.drop(columns=['high', 'low','close','volume'])
	newnewdata2 = newdata2.drop(columns=['high', 'low','close','volume'])
	return graph(symbol1, symbol2, newnewdata1, newnewdata2, meta_data, ts, '24 Hours')
	
################ 1 week function ################
def stockchart_1week(symbol1, symbol2):
	# Make the interval be hourly
	title = '1 Week'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data1, meta_data = ts.get_daily(symbol=symbol1, outputsize='compact')
	data2, meta_data = ts.get_daily(symbol=symbol2, outputsize='compact')
	newdata1 = data1.drop(data1.index[0:93])
	newdata2 = data2.drop(data2.index[0:93])
	newnewdata1 = newdata1.drop(columns=['high', 'low','close','volume'])
	newnewdata2 = newdata2.drop(columns=['high', 'low','close','volume'])
	return graph(symbol1, symbol2, newnewdata1, newnewdata2, meta_data, ts, title)

################ 4 week function ################
def stockchart_4week(symbol1, symbol2):
	# Make the interval be hourly
	title = '4 Weeks'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data1, meta_data = ts.get_daily(symbol=symbol1, outputsize='compact')
	data2, meta_data = ts.get_daily(symbol=symbol2, outputsize='compact')
	newdata1 = data1.drop(data1.index[0:78])
	newdata2 = data2.drop(data2.index[0:78])
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
	print(newdata1)
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
	print(newdata1)
	print(newdata2)
	return graph(symbol1, symbol2, newdata1, newdata2, meta_data, ts, title)

################ 5 year function ################
def stockchart_5year(symbol1, symbol2):
	# Make the interval be weekly
	title = '5 Years'
	ts = TimeSeries(key='QBGZM8IV1P2X2VJQ', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol=symbol1,interval='15min', outputsize='compact')
	data2, meta_data = ts.get_intraday(symbol=symbol2,interval='15min', outputsize='compact')
	return graph(symbol1, symbol2, data, data2, meta_data, ts)

stockchart_1week('GOOGL','AAPL')
