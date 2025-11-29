#program to check if user input number are equal without using any comparion operator.

def checkIfSame(number1,number2):

#user XOR operator as a^a is always 0
   if ((number1 ^ number2) != 0):
      print("Number are not equal")
   else:
      print("Both number are equal")
    #taking input
number1 = int(input("Enter first number to compare:"))
number2 = int(input("Enter second number to compare:"))

checkIfSame(number1,number2)
