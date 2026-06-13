# Q52: Write a program to Count even and odd elements.

n = int(input("Enter the number of elements: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

# Counters for even and odd numbers
even_count = 0
odd_count = 0

# Looping through the array to check each number
for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Displaying the results
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)