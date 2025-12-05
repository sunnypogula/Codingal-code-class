#swaping 2 numbers
def swap(a,b):  #a = 2 = 10 , b = 3 = 11
    a = a^b #10^11 = 01
    b = a^b # 01 ^ 11 = 10 = 2
    a = a^b # 01 ^ 10 =11 = 3
    print("After swapping : a =",a,"and b =",b)

def swap2(a,b):
    a = (a&b)+(a|b) #(10 &11=10)+(10|11=11)=10+11=101=5
    b = a+(~b)+1 #a+(-b-1)+1 = a-b=5-3=2
    print("After swapping : a =",a,"and b =",b)

swap(10,20)
swap2(10,20)

