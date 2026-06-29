# Q117: Write a program to Create student record system using arrays and strings.

# We preserve alignment across clean, matching lists (parallel arrays style)
student_names = []
student_grades = []

while True:
    print("\n--- Student Database ---")
    print("1. Add Student Detail")
    print("2. Display Report Records")
    print("3. Exit")
    
    choice = input("Enter option: ")
    if choice == "1":
        name = input("Enter student name: ").strip()
        grade = input("Enter assignment grade letter: ").upper().strip()
        student_names.append(name)
        student_grades.append(grade)
        print("Details stored.")
    elif choice == "2":
        print("\n--- Record Board ---")
        for i in range(len(student_names)):
            print(f"Student: {student_names[i]:<15} | Grade Evaluation: {student_grades[i]}")
    elif choice == "3":
        break