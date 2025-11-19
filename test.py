import sqlite3

# --- CREATE TABLE ---
conn = sqlite3.connect('DATA\\intelligence_platforms.db')
curr = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT
);
"""
curr.execute(sql)
conn.commit()

# --- INSERT DATA ---
sql_insert = "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)"
param = ("Djani1981", "Volimcevapi", "admin")

curr.execute(sql_insert, param)
conn.commit()

# --- READ USERS FUNCTION ---
def get_users():
    conn = sqlite3.connect('DATA\\intelligence_platforms.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    users = curr.fetchall()
    conn.close()
    return users

# --- PRINT USERS FROM FILE ---
with open('DATA/users.txt', 'r') as f:
    users = f.readlines()

for user in users:
    print(user.strip().split(','))

# Close after all operations
conn.close()
