def check_password(user_password: str):
    with open('10-million-password-list-top-100000.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, password in enumerate(common_passwords, start=1):
        if user_password == password:
            print(f'{password}    ⚠️⚠️ Common Password (#{i}) ⚠️⚠️')
            return
        if user_password == '':
            print('Type something...')
            return
    print('✅✅ Unique Password! ✅✅')


if __name__ == '__main__':
    while True:
        password: str = input("Enter a password (To exit type 'exit'): ")

        if password == 'exit':
            print('Thank you!')
            break

        check_password(password)