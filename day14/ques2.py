# Question 54: Write a program to Frequency of an element.
# Description: Count how many times a specific element appears in a list.

def count_frequency(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

# Driver Code to test
numbers = [1, 2, 3, 2, 4, 2, 5, 2, 6]
target_value = 2

frequency = count_frequency(numbers, target_value)
print(f"The element {target_value} appears {frequency} times in the list.")