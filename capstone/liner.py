import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv(r'petrol_consumption.csv')
dataset.head()
dataset.describe()
X = dataset[['Petrol_tax','Avarage_income','Paved_Highways','Population_Driver_licence(%)']]
y = dataset['Petrol_consumtion']
from sklearn.model_selection import train_test_splitx_train
X_train,X_test,y_train,y_test = train_test_split(X,y,test_side=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
coeff_df = pd.DataFrame(regressor.coef_,X.columns,columns=['coefficient'])
coeff_df
y_pred = regressor.predit(X_test)
df = pd.DataFrame({'Actual':y_test,'Predictes':y_pred})
df
from sklearn import metrics
print('mean absolute error:',metrics.mean_absolute_error(y_test,y_pred))
print('mean absolute error:',metrics.mean_squared_error(y_test,y_pred))
print('mean absolute error:',np.sqrt(metrics.mean_absolute_error(y_test,y_pred)))