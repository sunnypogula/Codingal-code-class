import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score
diabetes_X, disbates_y = datasets.load_disbetes(return_x_y = True)
diabetes_X = diabetes_X[:,np.newaxis]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]


diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.linearRegression()

regr.fit(diabetes_X_train,diabetes_y_test)
diabetes_y_pred = regr.predict(diabetes_y_train)

print('Coefficent:',regr.coef)
print('mean squared error: %.2f')

print('coefficient of determination:%.2f')
plt.scatter(diabetes_X_test,diabetes_y_test,color='black')
plt.plot(diabetes_X_test,diabetes_y_pred,color = 'blue',linewidth=3)

plt.xtick(())
plt.yticl(())
plt.show()