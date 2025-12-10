import sqlite3

# This is my direct  path to my actual database
DB_PATH = r"DATA/intelligence_platforms.db"


# --- CREATE TABLE ---
def create_table(conn):
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


# --- CONNECT TO DATABASE ---
conn = sqlite3.connect(DB_PATH)


# --- INSERT DATA ---
def insert_user(conn, username, password_hash, role):
    curr = conn.cursor()
    sql_insert = "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)"
    param = (username, password_hash, role)
    curr.execute(sql_insert, param)
    conn.commit()


# --- READ USERS FUNCTION ---
def get_all_user(conn):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    users = curr.fetchall()
    conn.close()
    return users


# --- OPTIONAL: PRINT USERS FROM FILE ---
'''
with open('DATA/users.txt', 'r') as f:
    users = f.readlines()

for user in users:
    print(user.strip().split(','))

conn.close()
'''