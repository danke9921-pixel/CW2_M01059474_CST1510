import sqlite3

#  Direct absolute path to your database
DB_PATH = r"C:\Users\djani\Documents\MDX Level 4\Programming and Data Communication Networks\CW2_M01059474_CST1510\DATA\intelligence_platforms.db"


def connect_database():
    #  Always connect to the same database
    return sqlite3.connect(DB_PATH, check_same_thread=False)