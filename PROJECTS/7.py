# Program to sort three numbers and reassign x, y, z

# Assign the given numbers
x = 5
y = 9
z = 1

# Put them into a list
numbers = [x, y, z]

# Sort the list in ascending order
numbers.sort()

# Reassign the sorted values back to x, y, z
x, y, z = numbers

# Print the updated values
print("Values in ascending order:")
print("x =", x)
print("y =", y)
print("z =", z)
