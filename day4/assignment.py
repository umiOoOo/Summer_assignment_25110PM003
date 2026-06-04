# Q13: Write a program to Generate Fibonacci series.
terms = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:")
    while count < terms:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
print()


# Q14: Write a program to Find nth Fibonacci term.
n = int(input("Enter the position (n): "))

a = 0
b = 1

if n <= 0:
    print("Please enter a position greater than 0.")
elif n == 1:
    print("The 1st Fibonacci term is:", a)
elif n == 2:
    print("The 2nd Fibonacci term is:", b)
else:
    for i in range(3, n + 1):
        nth = a + b
        a = b
        b = nth
    print("The", n, "th Fibonacci term is:", b)



    # Q15: Write a program to Check Armstrong number.
num = int(input("Enter a number: "))

num_str = str(num)
num_digits = len(num_str)
total_sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    total_sum += digit ** num_digits
    temp //= 10

if num == total_sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")



    # Q16: Write a program to Print Armstrong numbers in a range.
start = int(input("Enter lower bound: "))
end = int(input("Enter upper bound: "))

print("Armstrong numbers in the range are:")
for num in range(start, end + 1):
    num_str = str(num)
    num_digits = len(num_str)
    total_sum = 0
    
    temp = num
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** num_digits
        temp //= 10
        
    if num == total_sum:
        print(num, end=" ")
print()