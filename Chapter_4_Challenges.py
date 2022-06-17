# 1: Write Function: Takes number as input and returns num squared

def square_me():
    user_input = input("Enter a number: ")

    user_input_num = float(user_input)

    return user_input_num ** 2


# print(square_me())


# 2: Write Function: Accepts string as param and prints it

def print_this(this_str):
    print(this_str)


# print_this("Hey")
# print_this("Check")
# print_this("This Out")


# 3: Write Function: 3 required parameters, 2 options parameters

def param_test(a, b, c, d=2, e=2):
    print(a + b + c + d + e)


# param_test(1, 1, 1)
# param_test(1, 1, 1, 1)
# param_test(1, 1, 1, 1, 1)


# 4: Function 1: Return Int/2
#    Function 2: Return Int*4
#    Pass Result of Function 1 into Function 2

def func_1(x):
    return x//2


def func_2(y):
    return y*4


holder = func_1(10)
result = func_2(holder)

# print(result)


# 5: Function: Convert str to float, catch exceptions

def str_float(my_str):
    try:
        float(my_str)
        print(float(my_str))
    except ValueError:
        print("String must only contain numbers")


str_float("a")
str_float("5")
str_float("72.60")
