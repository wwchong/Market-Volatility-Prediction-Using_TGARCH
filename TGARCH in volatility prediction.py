import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from ib_insync import *
import seaborn as sns
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm

data = pd.read_csv("SPX_5Y_5mins_data.csv")
daily_data = pd.read_csv("SPX_5Y_daily_data.csv")
data.drop("Unnamed: 0",axis=1,inplace=True)

#calculate the 5 mins return
data['change'] = data['close'].pct_change()

#calculate the 5 mins log return
data['log_return'] = np.log(1+data['change'])

#calculate the squared of return
data['squared_return'] = data['log_return']**2
data.dropna(inplace=True)

#turn the column into datetime format
data['Simple Date'] = pd.to_datetime(data['Simple Date']).dt.date
daily_data['date'] = pd.to_datetime(daily_data['date']).dt.date

#calculate the Daily Realized Variance
rv = data.groupby(by='Simple Date')[['squared_return']].sum()

#plot the autocorrelation of Daily Realized Variance
plt.figure(figsize=(8,6))
sns.barplot(x=np.arange(1,21),y=acf(rv)[1:21])
plt.show()

#calculate the log daily return 
daily_data['log_return'] = np.log(1+daily_data['close'].pct_change())

#consider the log daily return as AR(1) process
model2 = ARIMA(daily_data['log_return'].dropna(), order=(1,0,0))
model_fit2 = model2.fit()
print(model_fit2.summary())

#calculate the epsilon2 of each log daily return data
#coefficients are from the AR(1) model summary
daily_data['epsilon2'] = (daily_data['log_return'] - (0.0006-0.2416*daily_data['log_return'].shift()))**2

#rename the column in rv dataframe
rv.rename({"squared_return":"Realized Variance"},axis=1,inplace=True)

#prepare for TGARCH model training
#lag rv factor
rv['lag_rv'] = rv['Realized Variance'].shift()

#lag epsilon squared factor
rv = rv.merge(daily_data[['epsilon2','date']],'inner',left_on='Simple Date',right_on='date')
rv['lag_epsilon2'] = rv['epsilon2'].shift()
rv.drop('date',axis=1,inplace=True)

#dummy variable lag I where I = 1 when lag epsilon squared factor < 0 and I = 0 when lag epsilon squared factor >= 0 
rv['I'] = np.where(rv['lag_epsilon2'] > 0, 1, 0)

#combine dummy variable I and lag epsilon squared factor
rv['I_epsilon'] = rv['I'] * rv['lag_epsilon2']

rv.dropna(inplace=True)

#split train data and test data set
train_data = rv.iloc[:1200]
test_data = rv.iloc[1200:]

#run regression
x = train_data[['lag_rv','lag_epsilon2','I_epsilon']]
x = sm.add_constant(x)
y = train_data[['Realized Variance']]
model = sm.OLS(y,x)
model = model.fit()
print(model.summary())
#As we can see, all of our coefficients are statistically significant and R-squared is about 0.40 which is pretty high

#our prediction on the test set
y_hat = model.predict(sm.add_constant(test_data[['lag_rv','lag_epsilon2','I_epsilon']]))

#the mean squared error of our prediction
print("The MSE is " + str(np.mean((y_hat-test_data['Realized Variance'])**2)))
