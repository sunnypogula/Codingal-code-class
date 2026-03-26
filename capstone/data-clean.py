import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")

print(df.head())

print(df.isnull().sum())

# ✅ FIXED

df.ffill(inplace=True)

df.drop_duplicates(inplace=True)

df['date'] = pd.to_datetime(df['date'])

print(df.head())

plt.figure()

plt.plot(df['date'], df['daily_vaccinations'])

plt.xlabel('Date')

plt.ylabel('Daily Vaccinations')

plt.title('Daily Vaccinations Trend')

plt.show()