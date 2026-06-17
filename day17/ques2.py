# Q66: Write a program to Union of arrays.

def union_of_arrays(arr1, arr2):
    # First, combine both arrays
    combined = arr1 + arr2
    union_list = []
    
    # Loop through the combined list and pick only unique elements
    for item in combined:
        if item not in union_list:
            union_list.append(item)
            
    return union_list

# Example usage:
array_a = [1, 2, 3, 4]
array_b = [3, 4, 5, 6]

result = union_of_arrays(array_a, array_b)
print("Union of arrays:", result)