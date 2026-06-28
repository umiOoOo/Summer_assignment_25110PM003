# Q107: Write a program to Create salary management system.

salaries = []

while True:
    print("\n--- Salary Management System ---")
    print("1. Add Salary Record")
    print("2. Display Salary Slips")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        name = input("Enter Employee Name: ")
        basic_salary = float(input("Enter Basic Salary: ₹"))
        
        # Simple allowances and deductions calculation
        hra = basic_salary * 0.10  # 10% House Rent Allowance
        da = basic_salary * 0.05   # 5% Dearness Allowance
        tax = basic_salary * 0.08  # 8% Tax Deduction
        
        net_salary = basic_salary + hra + da - tax
        
        record = {
            "name": name,
            "basic": basic_salary,
            "hra": hra,
            "da": da,
            "tax": tax,
            "net": net_salary
        }
        salaries.append(record)
        print("Salary details calculated and recorded!")
        
    elif choice == "2":
        if not salaries:
            print("No records to display.")
        else:
            for r in salaries:
                print("\n--- SALARY SLIP ---")
                print(f"Employee: {r['name']}")
                print(f"Basic Salary: ₹{r['basic']:.2f}")
                print(f"HRA Allowance: ₹{r['hra']:.2f}")
                print(f"DA Allowance: ₹{r['da']:.2f}")
                print(f"Tax Deduction: ₹{r['tax']:.2f}")
                print(f"Net Take-Home Salary: ₹{r['net']:.2f}")
                print("-" * 20)
                
    elif choice == "3":
        print("Exiting system.")
        break
    else:
        print("Invalid choice!")