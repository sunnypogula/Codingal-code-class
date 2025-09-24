#parent class
class person():
    #__init__ is known as the constructor
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class employee(person):
    def __init__ (self,name ,idnumber,salary,post):
        self.salary = salary
        self.post =post

        #invoking the __init__ of the parent class
        person.__init__(self,name,idnumber)

#creation of an objeact variable or an instance
a = employee('penguin',20210401,15000,"intern")

#calling a function of the class person using its instances
a.display()