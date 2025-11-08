#program to convert roman numerals to integers

def romanToInt(romanInput):
    #all roman units with integer equivalent values
    roman ={'M':1000,'D':500,'C':100,'L':50,'X':10,'v':5,'i':1}
    
    #result
    resultInteger =0

    #go from 0 len-1: if integer equivalert is greater then next element,add it; else subtract it
    for i in range(0,len(romanInput) -1):
        if roman[romanInput[i]] < roman[romanInput[i + 1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]

#take roman as input from user
roman = input("Input roman numberal:")

#print the integer
print("Integer equivalent:", romanToInt(roman))