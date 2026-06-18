# Q72: Write a program to Sort array in descending order.

def sort_descending(arr):
    n = len(arr)
    # Using a simple bubble sort approach modified for descending order
    for i in range(n):
        for j in range(0, n - i - 1):
            # Change condition to '<' to push smaller elements to the end
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
numbers = [12, 34, 11, 90, 22, 64, 25]
print("Original array:", numbers)
descending_numbers = sort_descending(numbers)
print("Array sorted in descending order:", descending_numbers)