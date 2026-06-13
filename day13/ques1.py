# Q49: Write a program to Input and display array.

# Asking the user for the number of elements
n = int(input("Enter the number of elements you want in the list: "))

# Initializing an empty list (array)
my_list = []

# Taking input for each element using a loop
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

# Displaying the final list
print("The array elements are:", my_list)