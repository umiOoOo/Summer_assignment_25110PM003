# Q105: Write a program to Create student record management system.

students = []  # List to store student records as dictionaries

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        
        # Create a dictionary and add to the list
        student = {"roll_no": roll_no, "name": name, "course": course}
        students.append(student)
        print("Student added successfully!")
        
    elif choice == "2":
        if not students:
            print("No records found.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Course: {s['course']}")
                
    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ")
        found = False
        for s in students:
            if s['roll_no'] == search_roll:
                print(f"\nRecord Found!\nName: {s['name']}\nCourse: {s['course']}")
                found = True
                break
        if not found:
            print("Student record not found.")
            
    elif choice == "4":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")