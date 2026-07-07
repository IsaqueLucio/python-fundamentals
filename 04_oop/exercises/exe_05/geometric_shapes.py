"""
Exercise 1: Geometric Shapes
File: 16_geometric_shapes.py

Rules:
1. Create a class 'Square' with an __init__ taking 'side' (float).
2. Create a method 'calculate_area(self)' that returns side * side.
3. Create a class 'Circle' with an __init__ taking 'radius' (float).
4. Create a method 'calculate_area(self)' that returns 3.14 * (radius ** 2).
5. Create a function OUTSIDE the classes called 'print_area(shape)'.
   - This function should call the 'calculate_area()' method of the passed object and print the result.
6. Create one Square and one Circle. Pass both to the 'print_area' function to test polymorphism.
"""

class Square:

    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        area = round((self.side * self.side), 3)
        return area

class Circle:

    def __init__(self, radius: float):
        self.radius = radius
    
    def calculate_area(self):
        area = round((3.14 * (self.radius ** 2)), 3)
        return area

def print_area(shape):
    print(shape.calculate_area())

square = Square(9.9)
circle = Circle(9.7)

print_area(square)
print_area(circle)