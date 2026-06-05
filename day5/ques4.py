# Q20: Write a program to Find largest prime factor.

# Take input from the user
num = int(input("Enter a number: "))

# Keep a backup of the number to display at the end
original_num = num
largest_prime_factor = 1

# Step 1: Divide out all the 2s (the only even prime)
while num % 2 == 0:
    largest_prime_factor = 2
    num //= 2  # Reduce the number

# Step 2: Check odd numbers starting from 3
factor = 3
while factor * factor <= num:
    while num % factor == 0:
        largest_prime_factor = factor
        num //= factor  # Reduce the number
    factor += 2  # Move to the next odd number

# Step 3: If the remaining number is greater than 2, it must be prime
if num > 2:
    largest_prime_factor = num

print(f"The largest prime factor of {original_num} is: {largest_prime_factor}")