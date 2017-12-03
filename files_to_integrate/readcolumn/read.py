import pandas as pd
import csv
def stock(symbol):
	nasdaq = pd.read_csv("nasdaq.csv")
	nyse   = pd.read_csv("nyse.csv")
	amex   = pd.read_csv("amex.csv")

	nasdaq.columns = ["Symbol", "Name", "LastSale", "MarketCap", "IPOyear", "Sector", "industry", "Summary Quote", "None"]
	nyse.columns   = ["Symbol", "Name", "LastSale", "MarketCap", "IPOyear", "Sector", "industry", "Summary Quote", "None"]
	amex.columns   = ["Symbol", "Name", "LastSale", "MarketCap", "IPOyear", "Sector", "industry", "Summary Quote", "None"]

	nasdaq_symbols = list(nasdaq.Symbol)
	nyse_symbols   = list(nyse.Symbol)
	amex_symbols   = list(amex.Symbol)

	strip_nasdaq_symbols = [elem.strip() for elem in nasdaq_symbols]
	strip_nyse_symbols   = [elem.strip() for elem in nyse_symbols]
	strip_amex_symbols   = [elem.strip() for elem in amex_symbols]

	symbol = symbol.upper().strip()
	symbols = set().union(strip_nasdaq_symbols, strip_nyse_symbols, strip_amex_symbols)

	# with open('symbols.csv', 'w') as f:
	#     writer = csv.writer(f)
 #    	for val in symbols:
 #        	writer.writerow([val])
    if symbol not in symbols:
    	raise ValidationError('Field must be less than 50 characters')

