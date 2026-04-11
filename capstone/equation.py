import matplotlib.pyplot as plt

import numpy as np

x = np.arange(1,11)

y1 =  (2 * x) + 1
y2 =  (2 * x**2) + 2

plt.plot(x,y1, label="y = 2x + 1")
plt.plot(x,y2, label="y = 2x**2 + 2")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of equations")

plt.legend()
plt.show()