import secrets  # not random because it can be reverse engineered
import string  # library that categorizes every character in a string (digits, ASCII, hex, punctuation, etc)


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


def generate_password(length: int, symbols: bool, upper_case: False):
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if upper_case:
        combination += string.ascii_uppercase

    while True:
        password: str = ""
        for _ in range(length):
            password += combination[secrets.randbelow(len(combination))]

        check: bool = False
        if upper_case and has_upper(password) and symbols and has_symbols(password):
            check = True

        if check:
            return password


if __name__ == "__main__":
    for i in range(1, 6):
        length = input("Enter the length of the password: ")
        symbols = input("Do you want symbols in your password? (y/n): ")
        upper_case = input("Do you want upper case in your password? (y/n): ")
        if symbols == "y":
            symbols = True
        else:
            symbols = False
        if upper_case == "y":
            upper_case = True
        else:
            upper_case = False
        new_password = generate_password(int(length), symbols, upper_case)
        
        description: str = (
            f"length: {len(new_password)}, has_symbols: {has_symbols(new_password)}, "
            f"upper_casing: {has_upper(new_password)}"
        )
        print(f"{i} -> {new_password} | {description}")
