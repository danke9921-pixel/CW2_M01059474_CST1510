# Author : Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming and Data Communication Networks
# Description:
# This module manages all authentcation processes, including password hashing
# and user verification using bcrypt. It ensures that user credentials are stored securely and that login attempts are validated correctly.

import os
import sqlite3
import bcrypt

#  Dynamically resolve the path to the database file in DATA folder
DB_PATH = r"DATA/intelligence_platforms.db"

#  Ensure the DATA folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

#  Create the database file if it doesn't exist
if not os.path.exists(DB_PATH):
    open(DB_PATH, "a").close()

#  Connect to the database
def get_connection():
    return sqlite3.connect(DB_PATH)

#  Ensure users table exists
def ensure_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Run this once when the module loads
ensure_users_table()

# Password requirements
def password_requirements(password: str) -> bool:
    #  Must be at least 8 characters
    if len(password) < 8:
        return False

    #  Must include at least one uppercase, one lowercase, one digit, and one special character
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return has_upper and has_lower and has_digit and has_special

# Register a new user
def register_user(username: str, password: str, role: str = "user") -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False

    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, hashed_pw, role)
    )
    conn.commit()
    conn.close()
    return True

# Login user
def login_user(username: str, password: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        stored_pw = row[0]
        return bcrypt.checkpw(password.encode("utf-8"), stored_pw)
    return False