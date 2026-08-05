import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load built-in penguins dataset
df = sns.load_dataset("penguins")

# 2. Count missing values column by column
print("--- Missing Values Count ---")
print(df.isnull().sum())

# 3. Visualize missing values using a heatmap
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

# 4. Remove completely empty records (rows where all values are missing)
df = df.dropna(how="all")

# 5. Fill missing categorical values (mode / most frequent value)
df["sex"] = df["sex"].fillna(df["sex"].mode()[0])

# 6. Estimate missing numerical values
df["bill_length_mm"] = df["bill_length_mm"].interpolate(method="linear")
df["bill_depth_mm"] = df["bill_depth_mm"].bfill()
df["flipper_length_mm"] = df["flipper_length_mm"].ffill()