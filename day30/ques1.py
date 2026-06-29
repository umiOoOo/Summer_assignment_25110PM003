# Q118: Write a program to Create mini library system.

library_books = ["Python Basics", "Let Us C", "Data Structures"]

while True:
    print("\n--- Mini Library ---")
    print("1. View Shelf Books")
    print("2. Donate/Add New Book")
    print("3. Exit")
    
    choice = input("Select operation: ")
    if choice == "1":
        print("\nAvailable Books:")
        for idx, book in enumerate(library_books, 1):
            print(f"{idx}. {book}")
    elif choice == "2":
        new_book = input("Enter title of book to add: ").strip()
        if new_book:
            library_books.append(new_book)
            print(f"'{new_book}' added to system catalog.")
    elif choice == "3":
        break