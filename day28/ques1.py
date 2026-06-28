# Q109: Write a program to Create library management system.

books = [
    {"title": "Python Programming", "author": "John Doe", "status": "Available"},
    {"title": "Data Structures", "author": "Jane Smith", "status": "Available"}
]

while True:
    print("\n--- Library Management System ---")
    print("1. Display Books")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print("\n--- Book Catalogue ---")
        for idx, book in enumerate(books):
            print(f"{idx + 1}. '{book['title']}' by {book['author']} | Status: {book['status']}")
            
    elif choice == "2":
        book_title = input("Enter book title to issue: ")
        found = False
        for book in books:
            if book['title'].lower() == book_title.lower():
                found = True
                if book['status'] == "Available":
                    book['status'] = "Issued"
                    print(f"Book '{book['title']}' has been issued successfully!")
                else:
                    print("Sorry, this book is already issued out.")
                break
        if not found:
            print("Book not found in catalogue.")
            
    elif choice == "3":
        book_title = input("Enter book title to return: ")
        found = False
        for book in books:
            if book['title'].lower() == book_title.lower():
                found = True
                if book['status'] == "Issued":
                    book['status'] = "Available"
                    print(f"Thank you! '{book['title']}' is now available again.")
                else:
                    print("This book is already sitting in the library.")
                break
        if not found:
            print("Book details mismatch.")
            
    elif choice == "4":
        break