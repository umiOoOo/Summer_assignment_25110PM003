# Q112: Write a program to Create contact management system.

contacts = {}  # Dictionary to store contact details as: {Name: Phone Number}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Choose action: ")
    
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print(f"Contact for {name} saved successfully.")
        
    elif choice == "2":
        if not contacts:
            print("Your contact book is empty.")
        else:
            print("\n--- Saved Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name:<15} Phone: {phone}")
                
    elif choice == "3":
        search_name = input("Enter Name to search: ")
        if search_name in contacts:
            print(f"Found! Phone: {contacts[search_name]}")
        else:
            print("Contact not found in directory.")
            
    elif choice == "4":
        break