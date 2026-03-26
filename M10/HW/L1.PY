# Function 1: Single Step (Constant Time)
# This uses the built-in multiplication operator.
def multiply_single_step(n, m):
    result = n * m
    return result

# Function 2: N Iterations (Linear Time)
# This simulates n * m by adding 'm' to a total 'n' times.
def multiply_n_iterations(n, m):
    result = 0
    for i in range(n):
        result += m
    return result

# --- Testing the functions ---
num_n = 5
num_m = 10

print(f"Multiplying {num_n} and {num_m}:")
print(f"Method 1 (1 iteration): {multiply_single_step(num_n, num_m)}")
print(f"Method 2 ({num_n} iterations): {multiply_n_iterations(num_n, num_m)}")