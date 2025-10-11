'''

The 'x' mode in Python's open() function stands for exclusive creation.
Here's what it does:
1. It creates a new file.
2. If the file already exists, it raises a FileExistsError.
3. This mode is used when you want to ensure that you're not overwriting an existing file by accident
'''
#create a new file
new_file = open('my_file.txt','x')
new_file.close()

#check if a file w=exists
import os 
print("Checking id my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print("my_file.txt is removed!")
else:
    print("the file does not exist")

#create a new file if it doesn't
my_file = open("my_file.txt","w")
my_file.write("hi! i am penguin and i am 1 yr old.")
my_file.close

#delete file names codingal
os.remove("my_file.txt")

#delete the floder
#os.rmdir('floder)
