import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("iris_dataset.csv")
print(data.head())

print("\nshape of Dataset:")
print(data.shape)
print("\nColumn Names:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nStatistical summary:")
print(data.describe())

print("\nflower species count:")
print(data["species"].values_counts())

print("\nAverage values:")
print(data.mean(numeric_only=True))

print("\nMaxiumum values:")
print(data.max(numeric_only=True))

print("\nMinimum Values:")
print(data.min(numeric_only=True))

plt.figure(figsize=(8,6))
sns.scatterplot(
    x="sepal_length",
    y="petal_length",
    hue="species",
    data=data
)

plt.title("sepal length vs petal length")
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(data["sepal+length"],bins=10)
plt.title("Distribution of Sepal length")
plt.show()

plt.figure(figsize=(8,8))
sns.boxplot(x="species",y="petal_length")
plt.show

numeric_data = data.select_dtypes(include=np.number)
correlation= numeric_data.corr()
plt.figure(figsize=(8,8))
sns.heatmap(correlation,annot=True)
plt.title("Correlation heatmap")
plt.show()