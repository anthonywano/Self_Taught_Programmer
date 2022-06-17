# 1: Print every character in string "Camus"

my_string = 'Camus'

# for i in my_string:
#     print(i)
#
# print(my_string[0])
# print(my_string[1])
# print(my_string[2])
# print(my_string[3])
# print(my_string[4])


# 2: Collect 2 strings from user and insert into new string

# str_1 = input("Please enter a noun: ")
# str_2 = input("Please enter a name: ")
#
# final = "Yesterday I wrote a {}. I sent it to {}.".format(str_1, str_2)
#
# print(final)


# 3: Capitalize first letter in sentence

sentence = "aldous Huxley was born in 1894."

first = sentence[:6]
rest = sentence[6:]

# print(sentence)
# print(first.capitalize() + rest)


# 4: Break string into list elements

string = "Where now? When now? Who now?"

questions = string.split("?")
# print(questions)


# 5: Create sentence from list

my_list = ["The", "fox", "jumped", "over", "the", "fence", "."]

my_string = " ".join(my_list[:6])
my_string += my_list[6]
# print(my_string)


# 6: Replace 's' with '$'

my_string = "A screaming comes across the sky."

# print(my_string)
# print(my_string.replace('s', '$'))


# 7: Find index of first 'm'

my_string = 'Hemingway'

# index = my_string.index('m')
# print(index)


# 8: Turn dialogue into a string

dialogue = "\"Lisa,\" said Kyle, \"I need help moving this box of toys for the garage sale. Will you help me?\""
# print(dialogue)


# 9: Create string "three three three" using concatenation and then multiplication

three = 'three '

# print(three + three + three)
#
# print(three*3)


# 9: Slice string to only include before ','

my_string = 'It was a bright and cold day in April, and the clocks were striking 13'

index = my_string.index(',')
print(my_string[:index])
