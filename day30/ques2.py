# Q119: Write a program to Create mini employee management system.

emp_records = []

while True:
    print("\n--- Mini Employee Base ---")
    print("1. Add Employee Entry")
    print("2. List All Active Records")
    print("3. Exit")
    
    choice = input("Action ID: ")
    if choice == "1":
        eid = input("Set Registration ID: ")
        ename = input("Enter Full Name: ")
        emp_records.append({"id": eid, "name": ename})
        print("Record logged.")
    elif choice == "2":
        print("\nEmployee List:")
        for emp in emp_records:
            print(f"ID: {emp['id']} -> Name: {emp['name']}")
    elif choice == "3":
        break