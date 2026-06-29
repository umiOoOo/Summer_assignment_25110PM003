# Q115: Write a program to Create menu-driven string operations system.

while True:
    print("\n--- String Operations Menu ---")
    print("1. Convert to Uppercase")
    print("2. Reverse String")
    print("3. Count Vowels")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    if choice == "4":
        break
        
    user_str = input("Enter your string: ")
    
    if choice == "1":
        print("Result:", user_str.upper())
    elif choice == "2":
        print("Result:", user_str[::-1])
    elif choice == "3":
        vowel_count = sum(1 for char in user_str if char.lower() in "aeiou")
        print("Number of vowels:", vowel_count)
    else:
        print("Invalid selection.")