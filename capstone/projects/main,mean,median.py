import statistics
marks = [70,80,90,60,100]

total = sum(marks)

count = len(marks)
mean = total/count

print(marks)
print(mean)

mode = statistics.mode(marks)
print(marks)
print(mode)