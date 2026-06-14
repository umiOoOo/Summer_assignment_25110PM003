# Question 55: Write a program to Second largest element.
# Description: Find the second biggest number in a list without using built-in sort functions.

def find_second_largest(arr):
    if len(arr) < 2:
        return "List must have at least two elements"

    # Initialize largest and second largest to very small numbers
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            # Current largest becomes second largest, and update largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest if num is between largest and second largest
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no unique second largest element"
    
    return second_largest

# Driver Code to test
numbers = [12, 35, 1, 10, 34, 35, 1]
print("Second largest element is:", find_second_largest(numbers))