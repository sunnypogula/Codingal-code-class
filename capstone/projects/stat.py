import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("dataset.csv")
col = "category_column"  # Replace with your categorical column name

# 2. Frequency values (counts of each category)
counts = df[col].value_counts()
print("--- Frequency Values ---")
print(counts)

# 3. Median category (the Mode / Most frequent category)
mode_val = df[col].mode()[0]
print(f"\nMost Frequent Category: {mode_val}")

# 4. Visualize the categorical feature
df[col].value_counts().plot(kind="bar", title=f"Frequency of {col}")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.show()

# 5. Data Transformation: One-Hot Encoding
transformed_df = pd.get_dummies(df, columns=[col])
print("\n--- Transformed Data ---")
print(transformed_df.head())