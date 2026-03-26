import math

def calculate_lcm(a, b):
    # The math.gcd function is the most efficient way to find the GCD
    gcd = math.gcd(a, b)
    
    # Apply the LCM formula
    lcm = abs(a * b) // gcd
    return lcm

# --- User Input Section ---
print("--- LCM Calculator ---")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 == 0 or num2 == 0:
        print("LCM is not defined for zero.")
    else:
        result = calculate_lcm(num1, num2)
        print(f"The Least Common Multiple of {num1} and {num2} is: {result}")

except ValueError:
    print("Please enter valid integers.")