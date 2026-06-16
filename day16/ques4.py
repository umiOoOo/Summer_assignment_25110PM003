# Q64: Write a program to Remove duplicates from array.

def remove_duplicates(arr):
    unique_list = []
    
    for item in arr:
        # Only add the item to our new list if it's not already there
        if item not in unique_list:
            unique_list.append(item)
            
    return unique_list

# Example usage:
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
clean_list = remove_duplicates(numbers)
print("Array after removing duplicates:", clean_list)