name = "Penguin" #string  datatype
age = 15 #integer datatype
is_student = True#boolean datatype true/false
weight = 38.5 #Flaoat datatype

print("Name :", name)
print("Data Type of Name is :",type(name))
print("Age :", age)
print("Data Type of Age is :",type(age))
print("is_student:", is_student)
print("Data Type of print is_student is :",type(is_student))
print("weight   :", weight)
print("Data Type of print weight is :",type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of age is ", type(weight))