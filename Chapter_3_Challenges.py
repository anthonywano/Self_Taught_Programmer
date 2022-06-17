# 1: Print 3 different Strings

print("String 1")
print("String 2")
print("String 3")

print()


# 2: Write program print Small if x < 10 and large if x >= 10

x = 0

if x < 10:
    print("small")
else:
    print("LARGE")

print()


# 3: Write program print Small if x <= 10, Medium if 10 < x <= 25, Large x > 25

x = 26

if x <= 10:
    print("small")
elif 10 < x <= 25:
    print("Medium")
else:
    print("LARGE")

print()


# 4: Divide 2 variables and print remainder

a = 5
b = 2

print(a % b)

print()


# 5: Divide variables and print quotient

a = 5
b = 2

print(a // b)

print()


# 6: Print different strings based on age

age = 70

if age == 0:
    print("Infant")
elif 1 <= age <= 4:
    print("Toddler")
elif 5 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teen")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")

print()
