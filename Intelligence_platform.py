import sqlite3
import pandas as pd
conn = sqlite3.connect('DATA\\intelligence_platform.db')
def create_user_table():
    curr = conn.cursor()
    sql = (""" CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL, 
    role TEXT DEFAULT 'user' ) """) 

    curr.execute(sql)
    conn.commit()

def add_user(conn, name, hash):
    curr = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash) VALUES (?, ?) """)
    param = (name, hash) 
    curr.execute(sql, param)
    conn.commit()

def get_all_users():
    curr = conn.cursor()
    sql = ("""SELECT * FROM users""")
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return users


def migrate_users():
    with open('DATA\\users.txt', 'r')as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(',')
        add_user(conn, name, hash)

    conn.close()


def migrate_cyber_incidents(conn):
    data1 = pd.read_csv('DATA\\cyber_incidents.csv')
    data1.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data load')


def migrate_it_tickets(conn):
    data1 = pd.read_csv('DATA\\it_tickets.csv')
    data1.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data load')

def datasets_metadata(conn):
    data1 = pd.read_csv('DATA\\datasets_metadata.csv')
    data1.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data load')
datasets_metadata(conn)    



