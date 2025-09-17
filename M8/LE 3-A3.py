class parrot:

    #class attribute
    species = "bird"

    #instance attribute
    #constuctor method - special method
    def __init__(self,name,age):
        self.name = name
        self.age = age

#instantiate the parrot class
blu = parrot("blu",10)
woo = parrot("woo",15)

#access the class attributes
print("blu is a {}".format(blu.species))
print("woo is also a {}".format(woo.species))

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
