class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of Rectangle: {self.length * self.breadth}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")

shapes = [Rectangle(5, 3), Circle(7)]
for s in shapes:
    s.area()
