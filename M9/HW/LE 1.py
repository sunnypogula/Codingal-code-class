#open the file in the read mode
file_read = open('Codingal.txt','r')
print("FIle in read Mode - ")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt','w')
file_write.write("File in write mode ....")
file_write.write("Hi! iam pengium. i am 1 yr.old")
file_write.close()

file_append = open('Codingal.txt','a')
file_append.write("\nfile in append mode..")
file_append.write("Hi! iam pengium. i am 1 yr.old")
file_append.close()
