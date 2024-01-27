import sqlite3

conn = sqlite3.connect('Posts.db', check_same_thread=False)
cursor = conn.cursor()

# cursor.execute(f'SELECT * FROM users WHERE login = "admin" AND password = "12345678"')
# data = cursor.fetchall()

cursor.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, user TEXT, title TEXT, content TEXT)')
conn.commit()
conn.close()