# 1: Add a square_list class variable to Square class.  Every new object gets added to list
class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def change_size(self, change):
        self.side += change

    # 2
    def __repr__(self):
        return "{0} by {0} by {0} by {0}".format(self.side)

sq1 = Square(5)
sq2 = Square(10)
sq3 = Square(1)

# print(Square.square_list)
#
# # Seems changing the object does not impact the class variable here
# sq1.change_size(2)
# print(sq1.side)
#
# print(Square.square_list)


# 2: Change Square class so it prints s x s x s x s when printing the object
sq2 = Square(29)
print(sq2)


# 3: Function that checks if objects are the same
def same_check(o1, o2):
    if o1 is o2:
        return True

    else:
        return False

sq3 = Square(10)
sq4 = sq3
sq5 = Square(10)

print(same_check(sq3, sq4))
print(same_check(sq3, sq5))