import pandas as pd
df = pd.read_csv("dataT.csv")
print(df.head())
result = pd.crosstab(df["Gender"],df["Survived"])
print(result)
