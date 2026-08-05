import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load built-in exercise dataset
df = sns.load_dataset("exercise")

# 2. Filter for running records only
running = df[df["kind"] == "running"]

# 3. Separate 1-min and 30-min records
min_1 = running[running["time"] == "1 min"][["id", "pulse"]]
min_30 = running[running["time"] == "30 min"][["id", "pulse"]]

# 4. Merge results and calculate pulse change
merged = pd.merge(min_1, min_30, on="id", suffixes=("_1min", "_30min"))
merged["pulse_change"] = merged["pulse_30min"] - merged["pulse_1min"]

# 5. Sort participants by pulse change
merged = merged.sort_values(by="pulse_change", ascending=False)

# 6. Reshape data for grouped bar plot
plot_data = running[running["id"].isin(merged["id"])]

# 7. Create grouped bar plot
ax = sns.barplot(
    data=plot_data, x="id", y="pulse", hue="time", order=merged["id"]
)

# 8. Label each bar with its height value
for container in ax.containers:
    ax.bar_label(container)

plt.title("Fitness Progress Comparison Chart (Running)")
plt.xlabel("Participant ID")
plt.ylabel("Pulse")
plt.show()