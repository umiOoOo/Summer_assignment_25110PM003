# Q58: Write a program to Rotate array left.

def rotate_left_by_one(arr):
    if len(arr) <= 1:
        return arr
        
    # Store the first element
    first_element = arr[0]
    
    # Shift all elements to the left by 1 position
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
        
    # Put the first element at the end
    arr[-1] = first_element
    return arr

# Example usage:
nums = [10, 20, 30, 40, 50]
print("Original:", nums)
print("Rotated Left:", rotate_left_by_one(nums))