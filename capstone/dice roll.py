import random

sides = int(input("Enter number of sides(6 or 12):"))
rolls = int(input("How many rolls?"))

for i in range(rolls):
    result = random.randint(1,sides)
    print("Rolls",i + 1,":",result)