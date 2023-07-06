import os

import matplotlib.pyplot as plt
import requests

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error as mape

# checking ../Data directory presence
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# download data if it is unavailable
if 'data.csv' not in os.listdir('../Data'):
    url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
    r = requests.get(url, allow_redirects=True)
    open('../Data/data.csv', 'wb').write(r.content)

# read data
import pandas as pd

data = pd.read_csv('data copy 3.txt')
# Make X a DataFrame with a predictor rating and y a series with a target salary
X,y = data[['rating']], data['salary']

# Split predictor and target into training and test sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state = 100)

#Fit the linear regression model with the following formula on the training data: salary∼rating
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

predictions_train = model.predict(X_train)
predictions_test = model.predict(X_test)

# Stage 1/5

#Predict a salary with the fitted model on test data and calculate the MAPE
from sklearn.metrics import mean_absolute_percentage_error
mape_train = mean_absolute_percentage_error(y_test,predictions_test)
# write your code here

#Print three float numbers: the model intercept, the slope, and the MAPE rounded to five decimal places and separated by whitespace.
#print(model.intercept_.round(5), model.coef_[0].round(5), mape_train.round(5))

#Stage 2/5

X, y = data[['rating']], data['salary']

min_mape_score = float('inf')
X_pow = X

for predict_power in range(2, 5, 1):
    X_pow = X_pow * X

    X_train, X_test, y_train, y_test = train_test_split(X_pow, y, test_size=0.3, random_state=100)

    model2 = LinearRegression()
    model2.fit(X_train, y_train)

    y_prediction = model2.predict(X_test)
    mape_score = mape(y_test, y_prediction)

    min_mape_score = min(min_mape_score, mape_score)

#print("%.5f" % min_mape_score)

# Stage 3/5

X,y = data[['rating','draft_round','age','experience','bmi']], data['salary']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state = 100)

#Fit the linear regression model with the following formula on the training data: salary∼rating
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

#Print the model coefficients separated by a comma.
coeffs = list(model.coef_)
#print(str(coeffs)[1:-1])

# Stage 4/5
#Find the variables where the correlation coefficient is greater than 0.2. Hint: there should be three of them.
corr = X.corr()
corr_list = corr[corr != 1][corr > 0.2].dropna(how='all').index.to_list()  # ['rating', 'age', 'experience']
subsets = [['rating'], ['age'], ['experience'], ['rating', 'age'], ['rating', 'experience'], ['age', 'experience']]
mape_list = []

for subset in subsets:
    X_subset = X_train.drop(columns=subset)
    X_subset_test = X_test.drop(columns=subset)
    model = LinearRegression()
    model.fit(X_subset, y_train)
    predictions_test = model.predict(X_subset_test)
    mape_test = mape(y_test, predictions_test)
    mape_list.append(mape_test)

# Make predictions and print the lowest MAPE. The MAPE is a floating number rounded to five decimal places.
#print(f'{min(mape_list):.5f}')

# Stage 5/5

X , y = data[['rating','draft_round','bmi']], data['salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

model = LinearRegression()
model.fit(X_train,y_train)

predictions_test = model.predict(X_test)
predictions_test[predictions_test<0] =0
mape_train_1 = mean_absolute_percentage_error(y_test,predictions_test)

median = y_train.median()
predictions_test = model.predict(X_test)
predictions_test[predictions_test<0] =median
mape_train_2 = mean_absolute_percentage_error(y_test,predictions_test)

print(min(mape_train_1.round(5),mape_train_2.round(5)))
