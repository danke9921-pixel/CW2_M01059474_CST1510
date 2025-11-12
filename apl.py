from main import register_user, login_user

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
            try:
                user_name = input("Enter username: ")
                pass_word = input("Enter password: ")
                print(login_user(user_name, pass_word))
            except ValueError as v:
                print(f"\nValue Error: {v}\n")
            except TypeError as t:
                print(f"Type Error: {t}")
        elif choice == '3':
            print('Bye, take care!')
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
