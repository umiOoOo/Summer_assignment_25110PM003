# Q67: Write a program to Intersection of arrays.

def intersection_of_arrays(arr1, arr2):
    intersection_list = []
    
    # Loop through the first array
    for item in arr1:
        # Check if the element is also in the second array and not already added
        if item in arr2 and item not in intersection_list:
            intersection_list.append(item)
            
    return intersection_list

# Example usage:
array_a = [1, 2, 3, 4, 4]
array_b = [3, 4, 5, 6]

result = intersection_of_arrays(array_a, array_b)
print("Intersection of arrays:", result)