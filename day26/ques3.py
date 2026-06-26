# Q103: Write a program to Create ATM simulation.

balance = 5000.0  # Starting balance

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ₹{balance}")
        
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{balance}")
        else:
            print("Invalid amount!")
            
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{balance}")
            
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")