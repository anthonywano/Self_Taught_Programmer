
import random

def build_game_board(level):
    if level == 0:
        print("""  
  _______
 |       |
 |
 |
 |
 |
 |
===========
            """)
    elif level == 1:
        print("""
  _______
 |       |
 |       0
 |
 |
 |
 |
===========
""")
    elif level == 2:
        print("""
_______
|       |
|       0
|       |
|
|
|
===========
""")
    elif level == 3:
        print("""
  _______
 |       |
 |       0
 |      /|
 |
 |
 |
===========
""")
    elif level == 4:
        print("""
  _______
 |       |
 |       0
 |      /|\\
 |
 |
 |
===========
""")
    elif level == 5:
        print("""
  _______
 |       |
 |       0
 |      /|\\
 |      /
 |
 |
===========
""")
    else:
        print("""
  _______
 |       |
 |       0
 |      /|\\
 |      / \\
 |
 |
===========
""")


# build_game(0)
# build_game(1)
# build_game(2)
# build_game(3)
# build_game(4)
# build_game(5)
# build_game(6)


def build_game_word(word_found):

    for char in word_found:
        if char != '#':
            print(char + " ", end='')
        else:
            print('_ ', end='')

    print()


def choose_word():
    words = ['impress',
             'tiny',
             'nappy',
             'kettle',
             'dock',
             'harm',
             'ten',
             'brash',
             'morning',
             'jaded',
             'happen',
             'sign',
             'private',
             'punish',
             'numberless',
             'daffy',
             'verse',
             'solid',
             'resolute',
             'needle']

    return words[random.randint(0, 19)]

