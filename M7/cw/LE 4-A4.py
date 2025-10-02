#python program to check if a number is prime
#take input from the user
num = int(input("enter a number:"))
#check if number is greater then 1 (since primes are >1)
if num>1:
    #loop only up to the square root of num for efficiency
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num}) is not a prime number.")
            break
        #if nko divisors were found , thec number is prime
    else:
        print(f"{num}is a prime number.")
else:
    #nujmbeeeer less then 2 are not prime
    print (f"{num}is not a prime number.mnnnnnnnr ")