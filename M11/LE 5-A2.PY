#write a program to divide 2 number without using  division operator
def divide(ourdividend,ourDivisor):
    sign = (-1 if((ourdividend < 0 ) ^ (ourDivisor < 0 ))else 1) #1^1 = 0
    ordividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)

    quotienNumber = 0
    tempNumber = 0 

    for i in range(31,-1,-1): 
        if (tempNumber +(ourDivisor << i) <= ourdividend):
            tempNUmber += ourDivisor << i
            quotientNumber |= 1 << i 

        if sign == -1:
            quotientNUmber = -quotienNumber
        return quotientNumber

a = int(input("Enter a for a/b:"))
b = int(input("Enter b for a/b:"))
print("Result of",a,"/",b,"is",divide(a,b))