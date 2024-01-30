from random import choice

# Generating random word
word_bank: list = ['banana', 'apple', 'marshmallow']
word: str = choice(word_bank)

# Starting game
print("Welcome to Hangman!")
guessed: str = ''
tries: int = 4

while tries > 0:
    blank: int = 0

    for char in word:
        if char in guessed:
            print(char, end='')
        else:
            print('_', end='')
            blank+=1

    print()  # print new line
    if blank == 0:
        print("You won!")
        break
    elif blank == len(word):
        guessed += input("Guess a letter: ")

    else:
        print("idk")
        break

        # TODO FINISH