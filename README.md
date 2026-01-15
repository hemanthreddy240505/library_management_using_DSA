# library_management_using_DSA
This project is a Library Management System (LMS) implemented in Python using SQLite for persistent data storage. The system allows users to register, login, borrow books, return books, and keeps track of book demand. It also includes admin access, allowing an admin to view all users and their borrowed books.
Modules


1. database.py

Purpose: Handles all interactions with the SQLite database.

Tables:

users(username, password) → Stores registered users.

books(title, quantity) → Stores books with available quantity.

user_books(username, book) → Stores which books are borrowed by which users.

Functions:

get_all_books() → Returns all books and their quantities.

get_book_quantity(title) → Returns the quantity of a specific book.

update_book_quantity(title, qty) → Updates quantity of a book after borrow/return.

add_user_book(username, book) → Records that a user has borrowed a book.

remove_user_book(username, book) → Removes a borrowed book record when returned.

get_user_books(username) → Returns all books borrowed by a specific user.

Data Structure Used: SQLite tables for persistent storage.


2. stack_queue.py

Purpose: Tracks book demand and waiting users.

Data Structures:

demand_stack → A stack that records each borrowed book. Most demanded books can be sorted.

waiting_queue → A queue that tracks users waiting for unavailable books.

Functions:

sort_demand_stack() → Sorts the stack by frequency of demand, showing most requested books first.



3. user.py

Purpose: Handles user registration, login, and simulated input for non-interactive environments.

Functions:

register() → Allows new users to create an account. If the user exists, redirects to login.

login() → Authenticates a user. Includes admin login detection.

get_input(prompt) → Simulates input() in environments that do not support interactive input (for testing or sandboxed environments).

Admin Credentials:

Username: admin

Password: admin123
books.py

Purpose: Handles book-related operations.

Functions:

show_books() → Displays all books and their available quantity.

borrow_book(user) → Allows a user to borrow a book if available. Updates the stack and database. If not available, user is added to the waiting queue.

return_book(user) → Allows a user to return a borrowed book. Updates database, stack, and notifies waiting users in the queue.



Data Structures Used:

Stack → Records demand of borrowed books.

Queue → Maintains users waiting for unavailable books.

SQLite tables → Track actual user borrowings and book quantities.
