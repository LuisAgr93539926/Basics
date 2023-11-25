from random import randint

lowerNum, higherNum = 1, 20
randomNumber: int = randint(lowerNum, higherNum)

print(f"Guess a number between {lowerNum} and {higherNum}")

while True:
    try:
        guessedNumber: int = int(input("Guess: "))
    except ValueError as e:
        print('Enter a valid number')
        continue

    if guessedNumber > randomNumber:
        print(f"Lower")
    elif guessedNumber < randomNumber:
        print(f"Higher")
    else:
        print(f"Finally")
        break
