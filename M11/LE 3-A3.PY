#finding which number in the array appears add number of times.
#Assumption :only two numbers should odd number of times

def TwoOdd(arr,size):
    xorof2,x,y,SetBit = arr[0],0,0,0

    for i in range(1,size):
        xorof2 = xorof2 ^ arr[i]
    #xorof2=3
    SetBit = xorof2 & ~(xorof2-1)#11& 01 =01=1  

    for i in range(size): #range(6),i=0,1,2,3,4,5
        if(arr[i] & SetBit): #110 $011=000
            x = x ^arr[i] #000 ^ 011 =011 , 011^101 = 110,110^011 = 101=5
        else:
            y = y ^ arr[i]
#000 ^ 110 = 110, 110^110 = 000, 000^110 = 110 = 6

    return(x,y)
arr = []
arr_size = int(input("Etner the size of the array:"))
for i in range(0,arr_size):
    z = int(input("Enter element:"))
    arr.append(z)

x , y = TwoOdd(arr,arr_size)
print("TwoOdd element are", x,"&", y)

#[6,3,5,6,3,6]
#[110,011,101,110,011,110]
#[110 ^ 00 = 110,110^011=101,101^101=000,000^110=110,110^011=101,101^110 = 11=3]