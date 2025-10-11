#program to merge two files into a thrid file

#reading data from gile1
with open('Codingal.txt')as fp:
    datal = fp.read()

#reading data from file2
with open('sample_doc.txt')as fp:
    data2 = fp.read()

#merging 2 files
#to add the data of file2
#from next line
datal +="" 