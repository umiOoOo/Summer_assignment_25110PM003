# Q50: Write a program to Find sum and average of array.

n = int(input("Enter the number of elements: "))
my_list = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

# Calculating sum
total_sum = 0
for num in my_list:
    total_sum += num

# Calculating average (Sum divided by number of elements)
if n > 0:
    average = total_sum / n
else:
    average = 0

# Displaying the results
print("Sum of the array:", total_sum)
print("Average of the array:", average)