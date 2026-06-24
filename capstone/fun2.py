import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("iris_data.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["Species"].value_counts())
plt.hist(df["SepalLength"])
plt.title("Sepal Length distrinbution")
plt.show()
sns.scatterplot(
    x="SepalLength",
    y="PetalLength",
    hue="Species",
    data=df
)
plt.show()
sns.pairplot(df, hue="Species")
plt.show()