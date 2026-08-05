import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load built-in tips dataset
df = sns.load_dataset("tips")

# 2. Violin plot: Total bill distribution by day and gender
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True)
plt.title("Total Bill Distribution by Day and Gender")
plt.show()

# 3. Box plot: Tip distribution across party sizes
sns.boxplot(data=df, x="size", y="tip")
plt.title("Tips by Party Size")
plt.show()

# 4. FacetGrid / Relational plot: Bill vs. Tip across days and gender
sns.relplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    col="day",
    col_wrap=2,
    kind="scatter",
)
plt.suptitle("Total Bill vs Tip by Day & Gender", y=1.02)
plt.show()