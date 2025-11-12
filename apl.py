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
            user_name = input("Enter username: ")
            pass_word = input("Enter password: ")
            login_user(user_name,pass_word)
            print('log in succesful !!')
        elif choice == '3':
            print('Bye, take care!')
            break


if __name__ == "__main__":
    main()
