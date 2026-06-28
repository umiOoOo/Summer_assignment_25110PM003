# Q108: Write a program to Create marksheet generation system.

while True:
    print("\n--- Marksheet Generator ---")
    print("1. Generate Marksheet")
    print("2. Exit")
    
    choice = input("Enter option: ")
    
    if choice == "1":
        student_name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")
        
        # Input marks for subjects
        maths = float(input("Enter marks for Mathematics (out of 100): "))
        science = float(input("Enter marks for Science (out of 100): "))
        english = float(input("Enter marks for English (out of 100): "))
        
        total = maths + science + english
        percentage = (total / 300) * 100
        
        # Calculate grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"
            
        # Display the formatted marksheet
        print("\n==================================")
        print("         REPORT CARD/MARKSHEET     ")
        print("==================================")
        print(f"Name: {student_name:<20} Roll No: {roll_no}")
        print("----------------------------------")
        print(f"Mathematics : {maths}/100")
        print(f"Science     : {science}/100")
        print(f"English     : {english}/100")
        print("----------------------------------")
        print(f"Total Marks : {total}/300")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Final Grade : {grade}")
        print("==================================")
        
    elif choice == "2":
        break
    else:
        print("Invalid Option!")