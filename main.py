# ---------------------------
# Module: main.py (with Admin Access)
# ---------------------------
from user import register, login
from books import show_books, borrow_book, return_book
from stack_queue import sort_demand_stack
from database import c

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

user_choice = input("Do you want to Register or Login? (R/L): ").upper()
if user_choice == 'R':
    current_user = register()
else:
    current_user = login()

if current_user == "ADMIN":
    # Admin workflow
    while True:
        print("\nAdmin Options: 1-Show Users Data 2-Show Books 3-Show Demand Stack 4-Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            c.execute('SELECT * FROM user_books')
            all_data = c.fetchall()
            print("\nUsers Borrowed Books:")
            if all_data:
                for user, book in all_data:
                    print(f"{user} -> {book}")
            else:
                print("No books borrowed by any user.")
        elif choice == "2":
            show_books()
        elif choice == "3":
            sort_demand_stack()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
else:
    # Normal user workflow
    while True:
        print("\nOptions: 1-Show Books 2-Borrow Book 3-Return Book 4-Show Demand Stack 5-Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_books()
        elif choice == '2':
            borrow_book(current_user)
        elif choice == '3':
            return_book(current_user)
        elif choice == '4':
            sort_demand_stack()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")