import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("insurance_data.csv")
print("First 5 rows of the dataset:")
print(df.head())
plt.scatter(
    df["age"],
    df["bought_insurance"],
    marker="+",
    color="red"
)
plt.xlabel("Age")
plt.ylabel("Bought Insurance")
plt.title("Age vs Insurance Purchase")
plt.show()
from sklearn.model_selection import train_test_split
X = df[["age"]]
y = df["bought_insurance"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.8,
    random_state=42)
print("\nTraining data:")
print(X_train)
print("\nTesting data:")
print(X_test)
print("\nTraining target:")
print(y_train)
print("\nTesting target:")
print(y_test)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("\nModel training completed!")
y_predicted = model.predict(X_test)
print("\nPredicted values:")
print(y_predicted)
probabilities = model.predict_proba(X_test)
print("\nPrediction probabilities:")
print(probabilities)
accuracy = model.score(X_test, y_test)
print("\nModel accuracy:")
print(accuracy)
print("Accuracy percentage:", accuracy * 100, "%")
print("\nModel coefficient:")
print(model.coef_)
print("\nModel intercept:")
print(model.intercept_)
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def prediction_function(age):
    z = 0.042 * age - 1.53
    y = sigmoid(z)
    return y
age = 35
probability = prediction_function(age)
print("\n Probability for age 43:")
print(probability)