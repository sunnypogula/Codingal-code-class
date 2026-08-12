import pandas as pd
import numpy as np

df = pd.read_csv("dataprocessing.csv")

print("Original Data")
print(df)

print("Missing values:")
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Sex"] = df["Sex"].map({
    "male":1,
    "female":0,
})

df = df.drop(["PassengerId","Name"], axis = 1)
print("Processed data:")
print(df)
print("Missing values after processing:")
print(df.isnull().sum())