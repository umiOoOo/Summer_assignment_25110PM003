# Q68: Write a program to Find common elements.

def find_common_elements(arr1, arr2):
    common_list = []
    
    # Scan through the first array to spot items that exist in the second array
    for element in arr1:
        if element in arr2 and element not in common_list:
            common_list.append(element)
            
    return common_list

# Example usage:
list1 = ['apple', 'banana', 'orange']
list2 = ['grapes', 'banana', 'apple']

common = find_common_elements(list1, list2)
print("Common elements are:", common)