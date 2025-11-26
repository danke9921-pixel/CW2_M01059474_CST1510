from main import register_user, login_user

def password_requirements(password: str) -> bool:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return False

    if not any(char.islower() for char in password):
        print("Password must contain at least a lowercase letter.")
        return False

    if not any(char.isupper() for char in password):
        print("Password must contain at least an uppercase letter.")
        return False

    # Fixed special characters string and fixed indentation
    special_characters = "!#@*^$?~<>%&"
    if not any(char in special_characters for char in password):
        print("Password must contain at least one special character.")
        return False

    return True


def menu():
    print('Choose an option:')
    print('1. Register')
    print('2. Login')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input('Enter your choice: ').strip()

        if choice == '1':
            register_user()

        elif choice == '2':
            user_name = input("Enter username: ")
            pass_word = input("Enter password: ")
            login_user(user_name, pass_word)
            print('log in succesful !!')

        elif choice == '3':
            print('Thank you creating your login credentials, take care for now!')
            break


if __name__ == "__main__":
    main()