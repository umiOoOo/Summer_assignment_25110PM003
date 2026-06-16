# Q62: Write a program to Find maximum frequency element.

def find_max_frequency_element(arr):
    if not arr:
        return None
        
    max_element = arr[0]
    max_count = 0
    
    for item in arr:
        # Count how many times the current item appears in the list
        current_count = arr.count(item)
        
        # If it appears more than our previous maximum, update our tracking
        if current_count > max_count:
            max_count = current_count
            max_element = item
            
    return max_element

# Example usage:
numbers = [1, 3, 2, 3, 4, 3, 2, 1]
most_frequent = find_max_frequency_element(numbers)
print("The maximum frequency element is:", most_frequent)