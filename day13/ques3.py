# Q51: Write a program to Find largest and smallest element.

n = int(input("Enter the number of elements: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

# Assuming the first element is both the largest and smallest initially
largest = my_list[0]
smallest = my_list[0]

# Checking the rest of the elements
for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Displaying the results
print("Largest element is:", largest)
print("Smallest element is:", smallest)