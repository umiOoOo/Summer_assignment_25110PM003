# Q102: Write a program to Create voting eligibility system.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    years_left = 18 - age
    print(f"You are not eligible to vote yet. You can vote in {years_left} years.")