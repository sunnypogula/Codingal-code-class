# Program to input three numbers and arrange them in ascending order

# Input values
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))

# Put them into a list
numbers = [x, y, z]

# Sort the list
numbers.sort()

# Reassign the sorted numbers back to x, y, z
x, y, z = numbers

# Print the updated values
print("Values in ascending order:")
print("x =", x)
print("y =", y)
print("z =", z)