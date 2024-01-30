import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    total: int = 0
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
        total += random_roll

    rolls.append(total)
    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice you want to roll?: ")
            if user_input.lower() == 'exit':
                break
            result: list = roll_dice(int(user_input))
            total = result[-1]
            result[-1] = f" (Total: {total})"
            print(*result, sep=' | ')
        except ValueError:
            print("Something went wrong")
            continue


if __name__ == '__main__':
    main()
