import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


#plt.switch_backend('new_backend')

dates = []
prices = []

def get_data(filename):
	with open(filename,'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			dates.append(int(row[0].split('-')[2]))
			prices.append(float(row[1]))
	return

def predict_prices(dates,prices,x):
	dates=np.reshape(dates,(len(dates),1)) # nx1 matrix
	svr_lin = SVR(kernel = 'linear',C=1e3)
	svr_poly = SVR(kernel = 'poly',degree=2)
	svr_rbf = SVR(kernel = 'rbf',gamma=0.1)
	svr_lin.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)

	plt.scatter(dates,prices,color='black',label='Date')
	plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting RBF kernel
	plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting linear kernel
	plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting polynomial kernel
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('SVR')
	plt.legend()
	plt.show()

	return svr_lin.predict(x)[0],svr_poly.predict(x)[0],svr_rbf.predict(x)[0]

get_data('aapl.csv')
#print(dates)
#print(prices)

predicted_price = predict_prices(dates,prices,29)
print(predicted_price)