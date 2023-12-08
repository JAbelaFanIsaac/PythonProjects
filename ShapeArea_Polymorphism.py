import math

class Shape:
    def calculateArea(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return 0.5 * self.base * self.height

class Decagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculateArea(self):
        Area = 2.5*(self.side_length**2)* (5 + 2*(5**(1/2)))**(1/2)
        return Area


shapes = [Circle(5), Rectangle(10, 5), Triangle(10, 5), Decagon(10)]
for shape in shapes:
    print(f"Area: {shape.calculateArea()}")
