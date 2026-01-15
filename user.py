from database import c, conn

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    if c.fetchone():
        print("User already exists. Please login.")
        return login()
    c.execute('INSERT INTO users VALUES (?,?)', (username,password))
    conn.commit()
    print("Registration successful!")
    return username

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password))
    if c.fetchone():
        print("Login successful!")
        return username
    else:
        print("Login failed. Try again.")
        return login()
