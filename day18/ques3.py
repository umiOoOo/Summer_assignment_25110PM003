# Q71: Write a program to Binary search.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Element found, return its index
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        # If target is greater, ignore left half
        else:
            low = mid + 1

    return -1  # Element is not present in the array

# Example usage (Array must be sorted)
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
target_element = 25

result = binary_search(sorted_numbers, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")