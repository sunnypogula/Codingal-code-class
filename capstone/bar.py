import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("country.csv")

data_1952 = df[df["year"]==1952]
data_2007 = df[df["year"]==2007]

data_1952 = data_1952[["county" "pop"]]
data_20007 = data_2007[["county" "pop"]]

merged_data = pd.merged(data_1952, data_2007, on="county")

merged_data["growth"] =merged_data["pop2007"] - merged_data["pop_1952"]

top_growth = merged_data.sort_values(by="growth", ascending=False)

top_growth = top_growth.head(10)

plt.figure(figsize=(12,6))

plt.bar(top_growth["country"],top_growth["growth"])

plt.title("top 10 countries by population growth")

plt.xlabel("countries")
plt.ylabel("population growth")

plt.xticks(rotation=45)

plt.show()