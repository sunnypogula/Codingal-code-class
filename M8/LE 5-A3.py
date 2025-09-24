# It refers to the process of hiding complex implementation details
# import necessary packages
from abc import ABC, abstractmethod      

# create a base class
class Animal(ABC):
    # abstract method
    # should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass


# sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


# Driver code
H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()