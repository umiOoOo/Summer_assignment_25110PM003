# Q9: Write a program to Check whether a number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")


 # Q10: Write a program to Print prime numbers in a range.
start = int(input("Enter lower bound: "))
end = int(input("Enter upper bound: "))

print("Prime numbers in the range are:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
print()



# Q11: Write a program to Find GCD of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find the smaller of the two numbers
if num1 < num2:
    smaller = num1
else:
    smaller = num2

gcd = 1
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

print("GCD is:", gcd)




# Q12: Write a program to Find LCM of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

lcm = greater
while True:
    if (lcm % num1 == 0) and (lcm % num2 == 0):
        print("LCM is:", lcm)
        break
    lcm += 1