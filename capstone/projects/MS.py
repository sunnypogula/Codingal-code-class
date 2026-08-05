import matplotlib.pyplot as plt
import numpy as np

# 1. Generate 12 months data
months = np.arange(1, 13)

# 2. Cumulative savings data for two plans
plan_a = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400])
plan_b = np.array([150, 350, 600, 900, 1250, 1650, 2100, 2600, 3150, 3750, 4400, 5100])

# 3. Plot both plans
plt.plot(months, plan_a, label="Plan A", color="blue", marker="o")
plt.plot(months, plan_b, label="Plan B", color="green", marker="s")

# 4. Shade the difference between the plans
plt.fill_between(months, plan_a, plan_b, color="gray", alpha=0.3, label="Difference")

# 5. Control visible axis ranges
plt.xlim(1, 12)
plt.ylim(0, 5500)

# 6. Add labels, title, and legend
plt.xlabel("Months")
plt.ylabel("Savings ($)")
plt.title("Monthly Savings Progress Chart")
plt.legend()

# 7. Display chart
plt.grid(True)
plt.show()