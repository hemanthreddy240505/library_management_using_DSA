from database import get_all_books, get_book_quantity, update_book_quantity, add_user_book, remove_user_book, get_user_books
from stack_queue import demand_stack, waiting_queue

def show_books():
    books = get_all_books()
    print("\nAvailable Books:")
    for book, qty in books:
        print(f"{book}: {qty}")





def borrow_book(user):
    show_books()
    book = input("Enter book to borrow: ")
    qty = get_book_quantity(book)
    if qty is None:
        print("Book not found.")
        return
    if qty > 0:
        update_book_quantity(book, qty-1)
        add_user_book(user, book)
        demand_stack.append(book)
        print(f"{book} borrowed successfully!")
    else:
        print(f"{book} not available. You are added to the waiting queue.")
        waiting_queue.append((user, book))




def return_book(user):
    borrowed = get_user_books(user)
    if not borrowed:
        print("You have no borrowed books.")
        return
    print("Your borrowed books:")
    for b in borrowed:
        print(b[0])
    book = input("Enter book to return: ")
    if (book,) in borrowed:
        remove_user_book(user, book)
        qty = get_book_quantity(book)
        update_book_quantity(book, qty+1)
        if book in demand_stack: 
            demand_stack.remove(book)
        print(f"{book} returned successfully!")


        
        # Check waiting queue





        for i in range(len(waiting_queue)):
            w_user, w_book = waiting_queue[0]
            if w_book == book:
                print(f"Notifying {w_user}: {book} is now available.")
                waiting_queue.popleft()
                break
    else:
        print("You did not borrow this book.")
