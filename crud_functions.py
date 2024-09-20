import sqlite3
import asyncio
connection = sqlite3.connect('nott_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')

    for i in range(1,5):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                        (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('nott_telegram.db')
    cursor = connection.cursor()
    chek_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if chek_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Users(username, email, age, balance) VALUES('{username}', '{email}', '{age}', 1000)
''')
        connection.commit()

def is_included(username):
    connection = sqlite3.connect('nott_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM Users')
    users = cursor.fetchall()
    for user in users:
        if username in user:
            return True
        else:
            continue
    return False
    connection.commit()
