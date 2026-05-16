import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("house_rent.csv")

print(df.head())

plt.figure(figsize=(8,5))

plt.scatter(
    df["Area"],
    df["Rent"],
    color="blue",
    s=100
)

plt.title("area vs house rent ")
plt.xlabel("area in square feet")
plt.ylable("monthly rent")
plt.grid(True)
plt.show()

sns.pairplot(df)
plt.show()