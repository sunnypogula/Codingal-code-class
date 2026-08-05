import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load built-in planets dataset
df = sns.load_dataset("planets")

# 2. Inspect the dataset
print("--- Dataset Head ---")
print(df.head())

# 3. Chart 1: Planet discoveries over time (by year)
sns.countplot(data=df, x="year")
plt.title("Number of Planet Discoveries by Year")
plt.xticks(rotation=45)
plt.show()

# 4. Chart 2: Discoveries by detection method
sns.countplot(data=df, y="method")
plt.title("Planet Discoveries by Method")
plt.show()

# 5. Chart 3: Orbital period vs Distance (Scatter plot)
sns.scatterplot(data=df, x="distance", y="orbital_period", hue="method")
plt.yscale("log")
plt.xscale("log")
plt.title("Orbital Period vs Distance (Log Scale)")
plt.show()