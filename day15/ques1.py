# Q57: Write a program to Reverse array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    # Swap elements from outer edges moving inward
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
nums = [1, 2, 3, 4, 5]
print("Original:", nums)
print("Reversed:", reverse_array(nums))