import pandas as pd

# 1. Load the dataset
df = pd.read_csv("dataset.csv")

# 2. View the first few rows
print("--- First 5 Rows ---")
print(df.head())

# 3. Check data types and missing values
print("\n--- Dataset Info ---")
print(df.info())

# 4. Get basic summary statistics (mean, min, max, etc.)
print("\n--- Summary Statistics ---")
print(df.describe())

# 5. Check missing values count per column
print("\n--- Missing Values ---")
print(df.isnull().sum())