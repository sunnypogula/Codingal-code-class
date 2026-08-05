import numpy as np
import pandas as pd

# 1. Load data
df = pd.read_csv("dataset.csv")

# 2. Check skewness of numerical features
print("--- Skewness ---")
print(df.skew(numeric_only=True))

# 3. Transform skewed numerical data (Log transformation)
df["transformed_num"] = np.log1p(df["skewed_column"])

# 4. Transform categorical data (One-Hot Encoding)
df = pd.get_dummies(df, columns=["category_column"], drop_first=True)

# 5. Check data association (Correlation matrix)
print("\n--- Feature Correlation ---")
print(df.corr(numeric_only=True))