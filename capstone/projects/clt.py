import numpy as np
import matplotlib.pyplot as plt

sample_size = [2,30,55,99]
plt.figure(figsize=(14,10))
for i ,size in enumerate(sample_size):
    means = []
    for _ in range( 2000):
        sample = np.random.randint(-40,41,size)
        means.append(np.mean(sample))
        plt.subplot(2,2,i + 1)
        plt.hist(means, bins = 20)
        plt.title(f"simple size = (size)")
        plt.xlabel("Sample mean")
        plt.ylabel("frequency")
plt.tight_layout()
plt.show