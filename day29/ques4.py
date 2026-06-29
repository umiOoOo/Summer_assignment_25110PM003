# Q116: Write a program to Create inventory management system.

inventory = {}  # Format: {item_name: quantity}

while True:
    print("\n--- Inventory Management ---")
    print("1. Add/Update Item Stock")
    print("2. View Current Inventory")
    print("3. Check Specific Item Stock")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        item = input("Enter item name: ").lower()
        qty = int(input("Enter quantity to add: "))
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
        print(f"Updated {item} stock details.")
    elif choice == "2":
        print("\n--- Stock Sheet ---")
        for item, qty in inventory.items():
            print(f"Item: {item.capitalize()} | Quantity: {qty}")
    elif choice == "3":
        item = input("Enter item to check: ").lower()
        print(f"Stock of {item}: {inventory.get(item, 0)}")
    elif choice == "4":
        break