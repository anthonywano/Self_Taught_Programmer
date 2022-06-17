import math

# 1: Define a class Apple with 4 attributes


class Apple:
    def __init__(self, apple_type, color, weight, flavor):
        self.type = apple_type
        self.color = color
        self.weight = weight
        self.flavor = flavor


ap1 = Apple("Honey Crisp", "Red/Yellow", 1, "Sweet")

# print(ap1.type)
# print(ap1.color)
# print(ap1.weight)
# print(ap1.flavor)


# 2: Create Circle class with area method


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius**2


cir1 = Circle(2)
print(cir1.area())


# 3: Create Triangle class with area method

class Triangle:
    def __init__(self, h, b):
        self.height = h
        self.base = b

    def area(self):
        return (self.height * self.base) / 2


tri1 = Triangle(3, 9)
print(tri1.area())


# 4: Create Hexagon class with perimeter method


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6


hex1 = Hexagon(1, 1, 1, 1, 1, 1)
print(hex1.calculate_perimeter())
