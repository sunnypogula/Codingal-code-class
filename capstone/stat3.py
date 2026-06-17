import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titan.csv")
count = df["Survived"].value_counts()

count.plot(
    kind="pie",
    autopct="%1.1f%%",
)
plt.title("Titanic Survival Counts")
plt.show()