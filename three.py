from yahoo_historical import Fetcher
import datetime

stock = raw_input("input stock symbol:")
#AAPL



now = datetime.datetime.now()

three_year_ago = [now.year-3,now.month,now.day]
now_year = [now.year,now.month,now.day]
print("from: %s, today: %s" % (three_year_ago, now_year) )



def today_open():
	data_today = Fetcher(stock, now_year)
	df_today = data_today.getHistorical()
	x = 0
	for index, row in df_today.iterrows():
		if row['Open'] > x:
			x = row['Open']		
			
	return(x)
	
def Y3_range():
	data_3ylow = Fetcher(stock, three_year_ago, now_year)
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
	

price_today = today_open()
price_range = Y3_range()
threeY_range = round((price_today-price_range[0]) / (price_range[1]-price_range[0]) * 100,2)

print ("today price: %s, three year lowest price %s, highest price %s" % (price_today, price_range[0], price_range[1]) )
print("three year range: %s%%" % threeY_range)

	