# Q120: Write a program to Develop complete mini project using arrays, strings and functions.

# Global tracking structures
expense_titles = []
expense_amounts = []

def add_expense(title, amount):
    """Clean string check and array insertion operation."""
    if title.strip() == "" or amount <= 0:
        print("Failed! Invalid input credentials.")
        return
    expense_titles.append(title.strip().capitalize())
    expense_amounts.append(amount)
    print("Expense added securely.")

def view_expenses():
    """Iterate and print structured string elements."""
    if not expense_titles:
        print("\nNo entries logged yet.")
        return
    print("\n=== EXPENSE REPORT SHEET ===")
    for i in range(len(expense_titles)):
        print(f"{i+1}. Item: {expense_titles[i]:<15} | Amount: ₹{expense_amounts[i]:.2f}")
    print(f"============================\nTotal Ledger Balance: ₹{sum(expense_amounts):.2f}")

# Main Execution Routine Interface Loop
while True:
    print("\n--- Household Mini Expense Tracker ---")
    print("1. Log New Expense Entry")
    print("2. Generate Balance Statement Summary")
    print("3. Close Management Application")
    
    choice = input("Select Option Panel: ")
    if choice == "1":
        name_entry = input("Enter utility item/description: ")
        cost_entry = float(input("Enter spent payment value: ₹"))
        add_expense(name_entry, cost_entry)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Shutting down management pipeline. Tracking complete!")
        break
    else:
        print("Invalid Operational Code.")