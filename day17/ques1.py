# Q65: Write a program to Merge arrays.

def merge_arrays(arr1, arr2):
    # The '+' operator combines two lists into a new one
    merged_list = arr1 + arr2
    return merged_list

# Example usage:
array_a = [1, 2, 3]
array_b = [4, 5, 6]

result = merge_arrays(array_a, array_b)
print("Merged array:", result)