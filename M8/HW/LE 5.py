# Main.py

# Parent Class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return "Area method not implemented"

    def perimeter(self):
        return "Perimeter method not implemented"

    def describe(self):
        return f"This is a shape called {self.name}"


# Child Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Child Class: Square (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


# Sample Usage / Test
if __name__ == "__main__":
    # Create a rectangle
    rect = Rectangle(10, 5)
    print(rect.describe())
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())

    print()  # spacer

    # Create a square
    sq = Square(7)
    print(sq.describe())
    print("Square Area:", sq.area())
    print("Square Perimeter:", sq.perimeter())