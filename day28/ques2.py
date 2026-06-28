# Q110: Write a program to Create bank account system.

accounts = {}  # Dictionary structure: { account_number: {name, balance} }

while True:
    print("\n--- Banking Account System ---")
    print("1. Create New Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Balance Inquiry")
    print("5. Exit")
    
    choice = input("Select action: ")
    
    if choice == "1":
        acc_num = input("Set Account Number: ")
        if acc_num in accounts:
            print("Account number already exists!")
        else:
            name = input("Enter Account Holder Name: ")
            initial_deposit = float(input("Enter Initial Deposit: ₹"))
            accounts[acc_num] = {"name": name, "balance": initial_deposit}
            print("Account registered successfully!")
            
    elif choice == "2":
        acc_num = input("Enter Account Number: ")
        if acc_num in accounts:
            amount = float(input("Enter deposit amount: ₹"))
            accounts[acc_num]["balance"] += amount
            print(f"Deposit successful. Balance: ₹{accounts[acc_num]['balance']}")
        else:
            print("Account number matching failure.")
            
    elif choice == "3":
        acc_num = input("Enter Account Number: ")
        if acc_num in accounts:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= accounts[acc_num]["balance"]:
                accounts[acc_num]["balance"] -= amount
                print(f"Withdrawal complete. Remaining balance: ₹{accounts[acc_num]['balance']}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")
            
    elif choice == "4":
        acc_num = input("Enter Account Number: ")
        if acc_num in accounts:
            print(f"Holder: {accounts[acc_num]['name']} | Balance: ₹{accounts[acc_num]['balance']}")
        else:
            print("Account not found.")
            
    elif choice == "5":
        break