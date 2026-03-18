
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Load the dataset from seaborn

df = sns.load_dataset("penguins")

# Show first 5 rows

print("First 5 rows:")

print(df.head())

# Shape the data

print("\nShape of the dataset:", df.shape)

# Check missing values

print("\nMissing values:")

print(df.isnull().sum())

# Basic statistics

print("\nBasic statistics:")

print(df.describe())

# Data types

print("\nData types:")

print(df.dtypes)

# Correlation matrix

sns.heatmap(df.corr(numeric_only=True),

annot=True)

plt.title("Correlation Heatmap")

plt.show()

# Histogram

df.hist(figsize=(10, 6))

plt.show()

# Count plots

sns.countplot(x="species", data=df)

plt.show()

sns.countplot(x="sex", data=df)

plt.show()

sns.countplot(x="island", data=df)

plt.show()

# Pairplot

sns.pairplot(df, hue="species")
plt.show()