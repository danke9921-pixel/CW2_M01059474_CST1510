import bcrypt

def hash_password(pwd) :
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def validate_password(pwd, hashed) :
    pwd_ = pwd.encode('utf-8')
    hashed_ = hashed.encode('utf-8')
    return bcrypt.checkpw(pwd_, hashed_)

def register_user():
    user_name = input("Enter username: ")
    password = input("Enter password:  ") 
    hashed_password = hash_password(password)
    with open('users.txt', 'a') as f:
        f.write(f"{user_name},{hashed_password}\n")
    print(hashed_password)

def login_user(username, password):
    with open('users.txt', 'r') as f:
        users_ = f.readlines()
        for user in users_:
            user_name,hash = user.strip().split(',')
            if user_name == username:
                return validate_password(password, hash)






    




