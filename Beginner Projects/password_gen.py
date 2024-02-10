import secrets  # not random because it can be reverse engineered
import string  # library that categorizes every character in a string (digits, ASCII, hex, punctuation, etc)
import enum

def has_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def has_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def generate_password(length:int, symbols: bool, upper_case: False):
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if upper_case:
        combination += string.ascii_uppercase

    while True:
        password: str = ''
        for _ in range(length):
            password += combination[secrets.randbelow(len(combination))]

        check: bool = False
        if upper_case and has_upper(password) and symbols and has_symbols(password):
            check = True

        if check:
            return password


if __name__ == '__main__':
    for i in range(1, 6):
        new_password = generate_password(3, True, True)
        # new_password = generate_password(3, False, False)
        # new_password = "arsi,otn"
        description: str = f'length: {len(new_password)}, has_symbols: {has_symbols(new_password)}, upper_casing: {has_upper(new_password)}'
        print(f'{i} -> {new_password} | {description}')

