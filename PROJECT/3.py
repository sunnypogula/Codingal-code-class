# Recursive function to generate Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ask user for number of terms
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i))