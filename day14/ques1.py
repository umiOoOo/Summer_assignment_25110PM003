# Question 53: Write a program to Linear search.
# Description: Find if a target element exists in an array/list by checking one by one.

def linear_search(arr, target):
    # Iterate through the list using index
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if element is not in the list

# Driver Code to test
numbers = [12, 45, 67, 89, 34, 23]
target_value = 89

result = linear_search(numbers, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the list.")