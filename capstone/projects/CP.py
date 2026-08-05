import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load data
df = pd.read_csv("dataset.csv")

# 2. Distribution Plot (Histogram)
sns.histplot(df["numeric_column"], kde=True)
plt.title("Data Distribution")
plt.show()

# 3. Categorical Count Plot (Bar Chart)
sns.countplot(data=df, x="category_column")
plt.title("Category Counts")
plt.show()

# 4. Relationship Plot (Scatter Plot)
sns.scatterplot(data=df, x="col_x", y="col_y", hue="category_column")
plt.title("X vs Y Relationship")
plt.show()

# 5. Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()