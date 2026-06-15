# Q59: Write a program to Rotate array right.

def rotate_right_by_one(arr):
    if len(arr) <= 1:
        return arr
        
    # Store the last element
    last_element = arr[-1]
    
    # Shift all elements to the right by 1 position (moving backwards)
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
        
    # Put the last element at the front
    arr[0] = last_element
    return arr

# Example usage:
nums = [10, 20, 30, 40, 50]
print("Original:", nums)
print("Rotated Right:", rotate_right_by_one(nums))