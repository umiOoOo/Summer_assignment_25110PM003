# Q60: Write a program to Move zeroes to end.

def move_zeroes(arr):
    insert_pos = 0
    
    # Move all non-zero elements to the front
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1
            
    # Fill the rest of the array positions with zeroes
    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1
        
    return arr

# Example usage:
nums = [0, 1, 0, 3, 12, 0, 5]
print("Original:", nums)
print("Zeroes Moved:", move_zeroes(nums))