# # Hangman Game

import Build_Game

level = 0
win = False
word = Build_Game.choose_word()
word_left = list(word)
word_found = list('#' * len(word))

while level < 6 and win is False:

    Build_Game.build_game_board(level)
    Build_Game.build_game_word(word_found)

    guess = input("Guess a letter: ")

    try:
        found = word_left.index(guess)
        print("Correct! {} is in the word.".format(guess))
        word_found[found] = word_left[found]
        word_left[found] = '#'

        if '#' not in word_found:
            win = True
    except:
        print("Sorry, {} is not in the word.".format(guess))
        level += 1

if win:
    Build_Game.build_game_board(level)
    Build_Game.build_game_word(word_found)
    print("You Win! The word was {}".format(word))

if level == 6:
    Build_Game.build_game_board(level)
    print("Sorry you lose, the word was {}. Game Over!".format(word))
