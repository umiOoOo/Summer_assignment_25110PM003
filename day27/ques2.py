# Q106: Write a program to Create employee management system.

employees = []

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Remove Employee")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        dept = input("Enter Department: ")
        
        emp = {"id": emp_id, "name": name, "dept": dept}
        employees.append(emp)
        print("Employee record added successfully!")
        
    elif choice == "2":
        if not employees:
            print("No employee records available.")
        else:
            print("\n--- Employee List ---")
            for e in employees:
                print(f"ID: {e['id']} | Name: {e['name']} | Dept: {e['dept']}")
                
    elif choice == "3":
        remove_id = input("Enter Employee ID to remove: ")
        found = False
        for e in employees:
            if e['id'] == remove_id:
                employees.remove(e)
                print("Employee removed successfully!")
                found = True
                break
        if not found:
            print("Employee ID not found.")
            
    elif choice == "4":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice!")