# Armstrong number checker

# Read number from user
num = int(input("Enter a number: "))

# Convert number to string to find number of digits
order = len(str(num))

# Compute the sum of each digit raised to the power of 'order'
temp = num
result = 0
while temp > 0:
    digit = temp % 10
    result += digit ** order
    temp //= 10

# Check and display result
if num == result:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")