# 1: Print all items in list

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

# for item in shows:
#     print(item)


# 2: Print all numbers from 25 to 50

# for i in range(25, 51):
#     print(i)


# 3: Print all items in list and the index

# for i, item in enumerate(shows):
#     print("{}: {}".format(i, item))


# 4: Guess the number game, q = quit

number = 2

correct = True
# while correct:
#     guess = input("Guess a number 1 to 10 or q to Quit: ")
#
#     if guess == 'q':
#         break
#     else:
#         if int(guess) == number:
#             print("Correct")
#             correct = False
#         else:
#             print("Wrong. Guess again.")


# 5:

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        result = i*j
        list3.append(result)

print(list3)
