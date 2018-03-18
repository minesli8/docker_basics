print('This is a test for Houston.\n\n')



from data_api.get_data import Stock
from price_predictor.price_predictor import TrendPredictor
import datetime

stock = input("Please input stock name (e.g., 'WM' for Waste Management, 'CGG' for CGG), then press 'ENTER' key:\n").strip()

stock = str(stock)
source = 'google'
date_end = datetime.date.today()
memory_gate = 90
date_begin = date_end - datetime.timedelta(memory_gate)

print('\n\nToday is %s'%date_end)

print('\n\nAnalyzing ......\n\n')
stock_instance = Stock(stock, source, date_begin, date_end)
stock_instance.get_data()
lag = -1
stock_instance.lag_data(lag)
stock_data = stock_instance.stock_data

print(stock_data.iloc[-4:, :])

trend = TrendPredictor(stock_data.iloc[:-1, :])
trend.linear_regression()

print('Predicted price for %s is %f. ' %(str(trend.today+datetime.timedelta(1))[0:10], trend.predicted_value))
