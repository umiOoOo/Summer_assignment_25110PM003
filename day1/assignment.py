# Q1: Program to calculate sum of first n natural numbers

n = int(input("Enter n: "))

# Using // for integer division to get a whole number
sum_val = n * (n + 1) // 2

print("Sum of first", n, "natural numbers =", sum_val)



# Q2: Program to print multiplication table of a given number

num = int(input("Enter a number: "))

print("Multiplication table of", num, ":")

# loop from 1 to 10
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

 

# Q3: Program to find factorial of a number

n = int(input("Enter a number: "))

factorial = 1

# loop from 1 to n
for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial of", n, "=", factorial)



# Q4: Program to count digits in a number

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    # If the number is negative, make it positive
    if num < 0:
        num = -num
        
    while num != 0:
        num = num // 10  # Drops the last digit
        count = count + 1

print("Number of digits =", count)