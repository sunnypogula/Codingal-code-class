#write in file using with() function
with open ('Codingal.txt','w')as file:
    file.write("hi! i am penguin and i am 1 yr old.")

#spilt file into words
with open('Codingal.txt','r')as file:
    data = file.readlines()
    print(data)
    print("Words in the this file are...")
    for line in data:
        word = line.split()
        print(word)
    file.close