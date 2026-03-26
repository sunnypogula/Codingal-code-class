def calculate_complexity_example(n):
    iterations = 0
    
    # Outer loop runs 'n' times
    for i in range(n):
        # Inner loop also runs 'n' times for every single outer iteration
        for j in range(n):
            iterations += 1
            
    return iterations

# --- Testing the Logic ---
n_value = 10
total_steps = calculate_complexity_example(n_value)

print(f"For an input (n) of {n_value}:")
print(f"The code executed {total_steps} iterations.")
print(f"Time Complexity: O(n^2) - Quadratic Time")