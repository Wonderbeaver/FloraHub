import sqlite3
import random


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

def add_post(user_id, title, content):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO posts (user_id, title, content, pub_time) VALUES (?, ?, ?, CURRENT_TIMESTAMP)', (user_id, title, content))
    conn.commit()
    conn.close()
  

def get_posts(id=None, page=1):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    limit = 10
    offset = (page - 1) * limit
    if id:
        cursor.execute('SELECT title, content, user_id, pub_time, id FROM posts WHERE user_id = (?) ORDER BY pub_time DESC LIMIT ? OFFSET ?', [id, limit, offset])
    else: 
        cursor.execute('SELECT title, content, user_id, pub_time, id FROM posts ORDER BY pub_time DESC LIMIT ? OFFSET ?', (limit, offset))
    posts = cursor.fetchall()
    posts_data = []
    for post in posts:
        posts_data.append({
            'title': post[0],
            'content': post[1],
            'author': get_user(post[2]),
            'pub_time': post[3],
            'id': post[4]
        })
    conn.close()
    return posts_data

def get_post(post_id):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts WHERE id = (?)', [post_id])
    post = cursor.fetchone()
    post_data = {
        'title': post[2],
        'content': post[3],
        'author': get_user(post[1]),
        'pub_time': post[4],
        'id': post[0]

    }
    conn.close()
    return post_data


def get_posts_len(id=None):
    conn = sqlite3.connect('Posts.db', check_same_thread=False)
    cursor = conn.cursor()
    if id:
        cursor.execute('SELECT id FROM posts WHERE user_id = (?)', [id])
    else:
        cursor.execute('SELECT id FROM posts')
    posts = cursor.fetchall()
    conn.close()
    return len(posts)

# def get_user_posts(id):
#     conn = sqlite3.connect('Posts.db', check_same_thread=False)
#     cursor = conn.cursor()
#     cursor.execute('SELECT title, content FROM posts WHERE user_id = (?)', [id])
#     posts = cursor.fetchall()
#     conn.close()
#     return posts

