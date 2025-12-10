# Author : Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming for Data Communication and Networks
# Description:
# This module establishes and maintains the connection to the SQLite database
# It provides a single, consistent database path for the entire system and ensures that all queries are executed against the correct database file.
import sqlite3

#  Direct absolute path to your database
DB_PATH = r"C:\Users\djani\Documents\MDX Level 4\Programming and Data Communication Networks\CW2_M01059474\CW2_M01059474_CST1510\DATA\intelligence_platforms.db"

def connect_database():
    return sqlite3.connect(DB_PATH, check_same_thread=False)