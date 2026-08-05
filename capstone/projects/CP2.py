import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load dataset using Pandas
df = pd.read_csv("dataset.csv")

# 2. Perform Data Operations (Pandas & NumPy)
print("--- Dataset Head ---")
print(df.head())

print("\n--- Summary Statistics ---")
print(df.describe())

# Clean missing values
df = df.dropna()

# NumPy mathematical operation
df["value_log"] = np.log1p(df["numeric_column"])

# 3. Data Visualization (Seaborn & Matplotlib)
# Scatter plot with Seaborn
sns.scatterplot(data=df, x="column_x", y="column_y", hue="category_column")
plt.title("X vs Y Scatter Plot")
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()