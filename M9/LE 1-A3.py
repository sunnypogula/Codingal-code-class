file = open ("Codingal.txt","r")
Counter = 0

Content = file.read()

CoList = Content.split("\n")
print(CoList)
for i in CoList:
    if 1:
        Counter += 1
print("This is the number of lines in the file")
print(Counter)