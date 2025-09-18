# Main.py

# Create a Robot class
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

# Create objects for Tom and Jerry
tom = Robot("Tom")
jerry = Robot("Jerry")

# Make the robots introduce themselves
tom.introduce()
jerry.introduce()