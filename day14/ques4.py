# Question 56: Write a program to Find duplicates in array.
# Description: Find and print elements that appear more than once in a list.

def find_duplicates(arr):
    duplicates = []
    unique_elements = []

    for num in arr:
        # If the number is already seen and not already added to duplicates
        if num in unique_elements and num not in duplicates:
            duplicates.append(num)
        elif num not in unique_elements:
            unique_elements.append(num)

    return duplicates

# Driver Code to test
numbers = [4, 3, 2, 7, 8, 2, 3, 1, 4]
print("Duplicate elements in the array are:", find_duplicates(numbers))