# TP FIND FACTORS OF USER INPUT 
#goes from 1 to number and checks if i divide the number . if yes, it is  a factor
def print_factors(number):
    print("The factors of ",number,"are:")
    for i in range (1,number +1):
        if number % i == 0:
            print(i)

#taking input from the user
number=int(input("Enter your  number to find its facrtors:"))

#calling our function
print_factors(number)
