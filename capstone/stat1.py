import pandas as pd
df = pd.read_csv("titan.csv")
survival_counts = df["Survived"].value_counts()
print(survival_counts)
print("Most common categorys:")
print(df["Survived"].mode())
