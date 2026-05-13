import matplotlib.pyplot as plt
males = [85,90,150,149,93,115,135,80,77,82,129,98,110,149]
females = [83,92,145,138,95,120,130,84,79,85,125,100,105,112,136]

plt.hist(males, bins=5,
         color = "blue",
         edgecolor= "black",
         alpha=0.7,
         label="men")

plt.hist(females,bins=5,
         color = "pink",
         edgecolor= "black",
         alpha=0.7,
         label="women")

plt.title("Analysis of Blood super level")
plt.xlabel("Frequency")
plt.legend()
plt.show()