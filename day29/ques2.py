# Q114: Write a program to Create menu-driven array operations system.

arr = []

while True:
    print(f"\n--- Current List: {arr} ---")
    print("1. Insert Element")
    print("2. Delete Element by Value")
    print("3. Search Element Index")
    print("4. Reverse List")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        val = int(input("Enter integer to insert: "))
        arr.append(val)
        print(f"{val} added successfully.")
    elif choice == "2":
        val = int(input("Enter value to delete: "))
        if val in arr:
            arr.remove(val)
            print(f"First occurrence of {val} removed.")
        else:
            print("Value not found in list.")
    elif choice == "3":
        val = int(input("Enter value to search: "))
        if val in arr:
            print(f"Value found at index: {arr.index(val)}")
        else:
            print("Value not found.")
    elif choice == "4":
        arr.reverse()
        print("List reversed.")
    elif choice == "5":
        break
    else:
        print("Invalid Selection.")