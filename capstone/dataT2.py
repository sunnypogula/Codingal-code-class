import pandas as pd
df = pd.read_csv("dataT.csv")
result = pd.crosstab(df["Gender"],df["Survived"])
print(result)