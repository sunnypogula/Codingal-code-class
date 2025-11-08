# program to find if a number is armstrong number
#take input from the user
number = int(input("Input your number:"))
 
#calculate number of digits
digits = len(str(number))

#initialize result variable
resultNumber = 0

#find the sum of the a digits of each digits
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //=10

# display the reult
if number == resultNumber:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")
