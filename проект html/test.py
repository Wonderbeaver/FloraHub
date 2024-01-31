import sqlite3

conn = sqlite3.connect('Posts.db', check_same_thread=False)
cursor = conn.cursor()

# cursor.execute(f'SELECT * FROM users WHERE login = "admin" AND password = "12345678"')
# data = cursor.fetchall()
cursor.execute('DROP TABLE IF EXISTS posts')
cursor.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT, content TEXT, pub_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')


conn.commit()
conn.close()