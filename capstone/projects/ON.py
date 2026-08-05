import numpy as np

# 1. Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# 2. Basic Arithmetic Operations
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# 3. Statistical Operations
print("Sum:", np.sum(arr))
print("Mean (Average):", np.mean(arr))
print("Max Value:", np.max(arr))
print("Min Value:", np.min(arr))

# 4. Array Reshaping
matrix = arr.reshape(1, 5)
print("Reshaped Matrix:\n", matrix)