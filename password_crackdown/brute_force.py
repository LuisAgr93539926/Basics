import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open('top-10k-common-words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if word == match:
            return f'Common word: {match} (#{i})'


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        guess: str = ''.join(guess)  # To get a str guess instead of list
        attempts += 1

        if guess == word:
            return f'{word} was cracked in {attempts:,} attempts'


def crack_word(word: str) -> str | None:
    digits: bool = False
    symbols: bool = False

    for char in word:
        if char in string.punctuation:
            symbols = True
        if char in string.digits:
            digits = True

    return brute_force(word, len(word), digits, symbols)


if __name__ == '__main__':
    password = input('Type a password -> ')
    print('Seaching...')

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if word := crack_word(password):
            print(word)
        else:
            print('No match')

    end_time: float = time.perf_counter()
    print(f'Performed in {round(end_time - start_time, 4)} seconds ')