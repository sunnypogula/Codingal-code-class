import pandas as pd
import matplotlib.pyplot as plt
import statistics 
import numpy as np

data = pd.read_csv("london_weather.csv")
print("weather DataSet")
print(data)

temperature = data["Temperature"]
mean_team = temperature.mean()
print("\nAverage Temperature")
print(mean_team)

variance = np.var(temperature)
print("\nVariance")
print(variance)

std_dev = np.std(temperature)
print("\nStandard Deviation")
print(std_dev)

best_month = data.loc[data["Temperature"].idxmax()]

print("\nBest month to visit london")
print(best_month["Month"])
plt.hist(
    temperature,
    bins=5
)

plt.title("London Temperature Disrtribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()