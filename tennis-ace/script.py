import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression

def train_model(X_train, X_test, y_train, y_test):
  # Fit training data 
  linreg = LinearRegression()
  
  if len(X_train.shape) == 1:
    # reshape 
    X_train = X_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)
  
  linreg.fit(X_train, y_train)

  # Predict using test set 
  y_predict = linreg.predict(X_test)
  
  # coefficient of determination 
  r2 = linreg.score(X_test, y_test)
  
  # sum of squared residuals 
  ssr = np.sum((y_predict - y_test)**2)
  return y_predict, r2, ssr 

def predict_vs_test(y_predict, y_test):
  fig, ax = plt.subplots()
  ax.scatter(x=y_test, y=y_predict, s=10)
  ax.plot([0, y_test.max()], [0, y_test.max()], color='black')
  ax.set_xlim(0, y_test.max()), ax.set_ylim(0, y_test.max())
  ax.set_xlabel('y_test')
  ax.set_ylabel('y_predict'); 