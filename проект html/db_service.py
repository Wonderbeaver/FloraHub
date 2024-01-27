import sqlite3

def check_user(login, password):
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE login = (?) AND password = (?)', (login, password))
    data = cursor.fetchone()
    conn.close()
    return data
def add_user(name, login, password):
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO users (name, login, password) VALUES (?, ?, ?)', (name, login, password))
    conn.commit()
    conn.close()

def check_login(login):
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT login FROM users WHERE login = (?)', [login])
    exist_login = cursor.fetchone()
    if login == exist_login[0]:
        return 'The account with this login already exists'
    
def get_user(id):
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = (?)', [id])
    user = cursor.fetchone()
    conn.close()
    return user

def add_post(user, title, content):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO posts (user, title, content) VALUES (?, ?, ?)', (user, title, content))
    conn.commit()
    conn.close()
    
def get_posts():
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content, user FROM posts')
    posts = cursor.fetchall()
    conn.close()
    return posts

def get_user_posts(name):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content FROM posts WHERE user = (?)', [name])
    posts = cursor.fetchall()
    conn.close()
    return posts
    

