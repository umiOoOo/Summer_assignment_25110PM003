# Q61: Write a program to Find missing number in array.

def find_missing_number(arr, n):
    # n is the total number of elements including the missing one
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of elements present in the array
    actual_sum = sum(arr)
    
    # The difference is the missing number
    return expected_sum - actual_sum

# Example usage:
# Array of size 4 containing numbers from 1 to 5 (4 is missing)
numbers = [1, 2, 3, 5]
total_count = 5 

missing = find_missing_number(numbers, total_count)
print("The missing number is:", missing)