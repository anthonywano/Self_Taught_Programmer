

# 1:Create Rectangle and Square classes with calculate_perimeter method

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return (2 * self.length) + (2 * self.width)


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side


rec1 = Rectangle(2, 4)
print(rec1.calculate_perimeter())

sq1 = Square(5)
print(sq1.calculate_perimeter())


# 2: Create Square class with change size method

class Square2:
    def __init__(self, side):
        self.side = side

    def change_size(self, change):
        self.side += change


sq2 = Square2(5)
print(sq2.side)

sq2.change_size(5)
print(sq2.side)

sq2.change_size(-3)
print(sq2.side)


# 3: Create Shape class with what_am_i method. Make Square and Rectangle class inherit Shape

class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a Shape")


class Rectangle2(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def what_am_i(self):
        print("I am a Rectangle")



class Square3:
    def __init__(self, side):
        self.side = side

    def what_am_i(self):
        print("I am a Square")


shp1 = Shape()
rec2 = Rectangle2(1, 1)
sq3 = Square3(5)

shp1.what_am_i()
rec2.what_am_i()
sq3.what_am_i()


# 4: Create class Horse and Rider.  Use composition to make a horse that has a rider

class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider


rider1 = Rider("Tony")
horse1 = Horse("Lightning", "Mustang", rider1)

print(rider1.name)
print(horse1.name)
print(horse1.breed)
print(horse1.rider.name)

