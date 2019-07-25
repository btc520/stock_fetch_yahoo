# the following example find today open
from yahoo_historical import Fetcher
import datetime

now = datetime.datetime.now()
time_now = [now.year,now.month,now.day]

data = Fetcher("AAPL", time_now)

data_get = data.getHistorical()

#print(data_get)

open = data_get['Open']

print (float(open[0]))

#for index, row in data_get.iterrows():
	#print( row )
	#print( type(row) )