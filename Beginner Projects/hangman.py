from random import choice

# 1. word bank
word_bank: list[str] = ['banana', 'apple']
word: str = choice(word_bank)

print('Welcome to hangman!')

guess: str = ''  # guessed letters
tries: int = 4  # amount of tries before losing

while True:
    for char in word:
        if char in guess:
            print(char, end='')
        else:
            print('_', end='')

    print()  # newline

    guess += input('Guess a letter ->')  # user input

    if guess in word:
        print('Good job!')
    else:
        tries -= 1
        print(f'Wrong! {tries} tries left...')

    if word == guess:
        print("You won!")

    if tries == 0:
        break

    