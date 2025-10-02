
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

    def __str__(self):
        return f"{self.name} Shape"

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length={self.length}, width={self.width}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"

    def __str__(self):
        return f"Square with side={self.length}"

if __name__ == "__main__":

    rect = Rectangle(10, 5)
    print(rect)
    print("Area of Rectangle:", rect.area())
    print("Perimeter of Rectangle:", rect.perimeter())
    print()

    sq = Square(6)
    print(sq)
    print("Area of Square:", sq.area())
    print("Perimeter of Square:", sq.perimeter())
