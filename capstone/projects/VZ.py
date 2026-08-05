import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load data
df = pd.read_csv("dataset.csv")

# 2. Scatter Plot (Numerical vs Numerical)
sns.scatterplot(data=df, x="column_x", y="column_y")
plt.title("Scatter Plot: Numerical Relationship")
plt.show()

# 3. Box Plot (Categorical vs Numerical)
sns.boxplot(data=df, x="category_col", y="numeric_col")
plt.title("Box Plot: Category vs Value")
plt.show()

# 4. Pair Plot (Relationships across all variables)
sns.pairplot(df)
plt.show()