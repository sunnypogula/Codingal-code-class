#progra, to eliminate repeated lne from a file

#creating the output file 
outputFile = open('UpdataedFile.tet',"w")

#reading the input file 
inputFile = open('Repeated.txt',"r")

#hol;ds line the in[put file
lines_seen_so_far =set()
print("Eliminating duplicate line")
#iterating each line in the file
for line in inputFile:
    #checlking if line is unique
    if line not in lines_seen_so_far:
        #write unique lines in oputput file
        outputFile.write(line)

        #adds unique line to lines_seen_so_far
        lines_seen_so_far.add(line)

#closing the file
inputFile.close
outputFile.close
