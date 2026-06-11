import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Book_Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E'],
    'Price': [15, 22, 10, 45, 12],
    'User_Rating': [4.5, 4.8, 4.2, 4.9, 3.8]
}
df = pd.DataFrame(data)

target_column = 'Price'

variance_val = df[target_column].var()
print(f"Variance of {target_column}: {variance_val}")

# 3. Calculate Standard Deviation
# Standard deviation is the square root of variance, showing spread in original units.
std_dev_val = df[target_column].std()
print(f"Standard Deviation of {target_column}: {std_dev_val.f}")

plt.figure(figsize=(8, 5))
sns.histplot(df[target_column], kde=True, color='skyblue', bins=5)

plt.title('Distribution of Book', )
plt.xlabel(target_column, )
plt.ylabel('Frequency',)

plt.grid(axis='y', alpha=0.3)
plt.show()