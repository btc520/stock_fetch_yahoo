from yahoo_historical import Fetcher
import datetime

#stock = raw_input("input stock symbol:")
#AAPL

holdings = ["BLV", "DBC", "GLD"]

now = datetime.datetime.now()

three_year_ago = [now.year-3,now.month,now.day]
now_year = [now.year,now.month,now.day]
print("from: %s, today: %s" % (three_year_ago, now_year) )



def today_open(loop_holdings_today):
	data_today = Fetcher(loop_holdings_today, now_year)
	df_today = data_today.getHistorical()
	x = 0
	for index, row in df_today.iterrows():
		if row['Open'] > x:
			x = row['Open']		
			
	return(x)
	
def Y3_range(loop_holdings_range):
	data_3ylow = Fetcher(loop_holdings_range, three_year_ago, now_year)
	df_3y_range = data_3ylow.getHistorical()

	year3_low = 100000
	year3_high = 0
	
	for index, row in df_3y_range.iterrows():
		if row['Open'] < year3_low:
			year3_low = row['Open']
		if row['High'] < year3_low:
			year3_low = row['High']
		if row['Low'] < year3_low:
			year3_low = row['Low']
		if row['Close'] < year3_low:
			year3_low = row['Close']
			
	for index, row in df_3y_range.iterrows():
		if row['Open'] > year3_high:
			year3_high = row['Open']
		if row['High'] > year3_high:
			year3_high = row['High']
		if row['Low'] > year3_high:
			year3_high = row['Low']
		if row['Close'] > year3_high:
			year3_high = row['Close']
			
			
	return(year3_low, year3_high)
	
for symbol in holdings: 
	price_today = today_open(symbol)
	price_range = Y3_range(symbol)
	
	threeY_range = round((price_today-price_range[0]) / (price_range[1]-price_range[0]) * 100,2)

	print ("###")
	print ("%s today price: %s, three year lowest price %s, highest price %s" % (symbol, price_today, price_range[0], price_range[1]) )
	print("three year range: %s%%" % threeY_range)
	print("###")

	