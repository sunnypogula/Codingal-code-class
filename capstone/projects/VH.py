import matplotlib.pyplot as plt
import pandas as pd

# 1. Load dataset
df = pd.read_csv("dataset.csv")

# 2. Plot histogram to check distribution
plt.hist(df["column_name"], bins=10, color="skyblue", edgecolor="black")

# 3. Add labels and title
plt.title("Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")

# 4. Display the plot
plt.show()