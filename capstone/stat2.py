import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titan.csv")
count = df["Survived"].value_counts()
count.plot(kind="bar")
plt.title("Titanic Survival Counts")
plt.xlabel("Surivived")
plt.ylabel("Count")
plt.show()