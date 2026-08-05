import numpy as np
import pandas as pd

# 1. Create a labeled Series
student_names = pd.Series(["Alice", "Bob", "Charlie", "David"])

# 2. Build a DataFrame table (including some missing values to clean)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 90, np.nan, 70],
    "Science": [92, np.nan, 78, 88],
}
df = pd.DataFrame(data)

# 3. Save to CSV and read back from CSV
df.to_csv("student_marks.csv", index=False)
df = pd.read_csv("student_marks.csv")

# 4. View rows and inspect data information
print("--- First Rows ---")
print(df.head())

print("\n--- Data Information ---")
df.info()

# 5. Clean missing values (filling with column average)
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())

# 6. Calculate total and average marks
df["Total"] = df["Math"] + df["Science"]
df["Average"] = df["Total"] / 2

print("\n--- Final Student Marks DataFrame ---")
print(df)