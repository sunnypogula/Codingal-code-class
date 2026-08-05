import numpy as np
import matplotlib.pyplot as plt

sample_size = [1,10,50,100]
plt.figure(figsize=(12,8))
for i ,size in enumerate(sample_size):
    means = []
    for _ in range( 1000):
        sample = np.random.randint(-40,41,size)
        means.append(np.mean(sample))
        plt.subplot(2,2,i + 1)
        plt.hist(means, bins = 20)
        plt.title(f"simple size = (size)")
        plt.xlabel("Sample mean")
        plt.ylabel("frequency")
plt.tight_layout()
plt.show