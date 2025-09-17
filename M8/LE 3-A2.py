class student:
    grade= 10
    name = "Penguin"

    #method1
    def introduction(self):
        print("hi i am a student")

    #method2
    def details(self):
        print("my name is", self.name)
        print("i study in grade",self.grade)
ob = student()      
ob.introduction()
ob.details()