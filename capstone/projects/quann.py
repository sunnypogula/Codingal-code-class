import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())
q1 = df["projects"].quantile(0.25)
q2 = df["projects"].quantile(0.50)
q3 = df["projects"].quantile(0.75)
iqr = q3-q1
print("Q1=",q1)
print("Median =",q2)
print("Q3 =",q3)
print("IQR = ",iqr)

plt.boxplot(df["projects"])
plt.title("Boxplot of Passenger projects")
plt.show()