import matplotlib.pyplot as plt

# 1. Data for weekly savings
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
savings = [50, 80, 60, 100]

# 2. Line Graph (with customized line style)
plt.figure(figsize=(6, 4))
plt.plot(
    weeks, savings, color="green", marker="o", linestyle="--", linewidth=2
)
plt.title("Weekly Savings Progress (Line Graph)")
plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.grid(True)
plt.show()

# 3. Bar Chart (for comparison)
plt.figure(figsize=(6, 4))
plt.bar(weeks, savings, color="skyblue", edgecolor="blue")
plt.title("Weekly Savings Progress (Bar Chart)")
plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.show()