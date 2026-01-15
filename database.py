import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

# Tables
c.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS books(title TEXT PRIMARY KEY, quantity INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS user_books(username TEXT, book TEXT)''')
conn.commit()

# Preload some books
initial_books = [
    ('Python Basics', 3),
    ('Data Structures', 2),
    ('Algorithms', 4),
    ('Machine Learning', 1),
    ('Databases', 2)
]
for book, qty in initial_books:
    c.execute('INSERT OR IGNORE INTO books(title, quantity) VALUES (?, ?)', (book, qty))
conn.commit()

# Database helper functions
def get_all_books():
    c.execute('SELECT * FROM books')
    return c.fetchall()

def get_book_quantity(title):
    c.execute('SELECT quantity FROM books WHERE title=?', (title,))
    res = c.fetchone()
    return res[0] if res else None

def update_book_quantity(title, qty):
    c.execute('UPDATE books SET quantity=? WHERE title=?', (qty, title))
    conn.commit()

def add_user_book(username, book):
    c.execute('INSERT INTO user_books VALUES (?,?)', (username, book))
    conn.commit()

def remove_user_book(username, book):
    c.execute('DELETE FROM user_books WHERE username=? AND book=?', (username, book))
    conn.commit()

def get_user_books(username):
    c.execute('SELECT book FROM user_books WHERE username=?', (username,))
    return c.fetchall()
