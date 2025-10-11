# Program to perform different operations on a file using Python

# Step 1: Create and write content into a file
file = open("Codingal.txt", "w")
file.write("Python is fun!\n")
file.write("I am learning file handling.\n")
file.write("File operations include read, write, and append.\n")
file.write("Let's explore how files work in Python.\n")
file.write("This is the last line.\n")
file.close()

# Step 2: Read the entire content of the file
file = open("Codingal.txt", "r")
content = file.read()
print("---- File Content ----")
print(content)
file.close()

# Step 3: Read file line by line
file = open("Codingal.txt", "r")
print("\n---- Reading line by line ----")
for line in file:
    print(line.strip())
file.close()

# Step 4: Count the number of lines, words, and characters
file = open("Codingal.txt", "r")
lines = file.readlines()
num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)
file.close()

print("\n---- File Statistics ----")
print(f"Total lines: {num_lines}")
print(f"Total words: {num_words}")
print(f"Total characters: {num_chars}")

# Step 5: Append new content to the file
file = open("Codingal.txt", "a")
file.write("\nNew line added using append mode.")
file.close()

# Step 6: Display final updated content
file = open("Codingal.txt", "r")
updated_content = file.read()
print("\n---- Updated File Content ----")
print(updated_content)
file.close()