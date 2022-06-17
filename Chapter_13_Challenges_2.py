# 1:Create Rectangle and Square classes with calculate_perimeter method
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length


class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side


# r1 = Rectangle(2, 4)
# print(r1.calculate_perimeter())
#
# s1 = Square(2)
# print(s1.calculate_perimeter())


# 2: Create Square class with change size method
class Square2:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, change):
        self.side += change


# s2 = Square2(2)
# print(s2.side)
# print(s2.calculate_perimeter())
#
# s2.change_size(4)
# print(s2.side)
# print(s2.calculate_perimeter())
#
# s2.change_size(-1)
# print(s2.side)
# print(s2.calculate_perimeter())


# 3: Create Shape class with what_am_i method. Make Square and Rectangle class inherit Shape
class Shape:
    pass

    def what_am_i(self):
        print("I am a shape")


class Rectangle2(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def what_am_i(self):
        print("I am a rectangle")


class Square3(Shape):
    def __init__(self, s):
        self.side = s

    def what_am_i(self):
        print("I am a square")


sh1 = Shape()
r2 = Rectangle2(2, 3)
s3 = Square3(4)


# sh1.what_am_i()
# r2.what_am_i()
# s3.what_am_i()


# 4: Create class Horse and Rider.  Use composition to make a horse that has a rider
class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, breed, name, rider):
        self.breed = breed
        self.name = name
        self.rider = rider


rider = Rider("Tony")
horse = Horse("Mustang", "Bullet", rider)

print(rider.name)
print(horse.breed)
print(horse.name)
print(horse.rider)
print(horse.rider.name)

