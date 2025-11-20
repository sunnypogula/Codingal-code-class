#Counting the total number of bits
def numberOfBits(n):
    count = 0
    while (n>0):
        count += 1 #count=3
        n = n>>1 #n = 101>>1 = 10 , 10>>1 = 1, 1>>1 = 0
        return count
n = int(input("Enter a number:"))
print("Number of bits:", numberOfBits(n))