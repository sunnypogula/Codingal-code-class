# empty tuple
my_tuple = ()
print(my_tuple)

#tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with mixed datatypes
my_tuple = (1,"hello",3.4,[1,2])
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8,4,6],(1,2,3,))
print(my_tuple)

# accessing tuple elements using  indexing
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[-1])

# nested tuple()
n_tuple = ("mouse",[8,4,6(1,2,"abcd",{'1':2})],(1,2,3))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])
print(n_tuple[1][3][3]['1'])

# slicing
print("sliced:",my_tuple[1:4])

#Iiterating through tuple
for letter in (my_tuple):
    print("hello",letter)