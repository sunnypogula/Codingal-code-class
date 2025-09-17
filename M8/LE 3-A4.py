class parrot:

    #instance attributes
    #constructor - special method
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #instance method
    def sing(self, song):
        return "{} sings {}".format(self.name,song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the odject
blu = parrot("blu",10)

#call our instance methods
print(blu.sing("happy"))
print(blu.dance())
