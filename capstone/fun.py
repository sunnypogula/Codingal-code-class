import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["Survived"].value_counts())
sns.countplot(x="Gender",hue="Survived",data=df)
plt.show()
sns.countplot(x="Pcless",hue="Survived",data=df)
plt.title("Surival by passenger class")
plt.show()