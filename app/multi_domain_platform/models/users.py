# Handling user login and Registration using CRUD Functions .

def verify_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone() # Looking for Username 

    if result is None:
        return False

    stored_password = result[0]
    return stored_password == password  


def create_user(conn, username, password):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password, "user")
        )
        conn.commit()
        return True
    except conn.IntegrityError:
        return False  # Username already exists.


# Retrieves Basic User Details which is helpful for the admin to view and as well as profile pages.
def get_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


# Updates the user's password it is helpful for resets or even adjustments. 
def update_password(conn, username, new_password):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password_hash = ? WHERE username = ?", (new_password, username))
    conn.commit()
    return cursor.rowcount > 0  # True if a row was updated.


# Deletes the user from the system 
def delete_user(conn, username):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    return cursor.rowcount > 0  # True if a row was deleted.