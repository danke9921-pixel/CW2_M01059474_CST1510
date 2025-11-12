import bcrypt

def hash_password(pwd) :
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')



def validate_password(pwd, hashed) :
    bol = bcrypt.checkpw(pwd, hashed)
    return bol

def register_user():
    user_name = input("Enter username: ")
    password = input("Enter password:  ") 
    hashed_password = hash_password(password)
    try:
        with open('users.txt', 'a') as f:
            f.write(f"{user_name}: {hashed_password}\n")
        print(hashed_password)
    except:
        print("File operation error!")


def login_user(username, password):
    
    try:
        lines = ""
        u_name = ""
        hash = ""
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines: 
                u_name, hash =line.strip().split(':')
                vld = validate_password(password, hash)
                if u_name == username and vld == True:
                    return validate_password(password, hash)
                else:
                    print("Invalid username or password")
                    return False
    except IOError:
        print("File IO Error in the login_user function")
    except:
        print("Error in the login_user function")
    finally:
        f.close()


    




