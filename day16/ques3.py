# Q63: Write a program to Find pair with given sum.

def find_pair_with_sum(arr, target_sum):
    # Outer loop picks the first element
    for i in range(len(arr)):
        # Inner loop picks the second element (avoids checking the same element)
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return (arr[i], arr[j]) # Return the pair as soon as it's found
                
    return None # Return None if no pair matches the target sum

# Example usage:
numbers = [10, 20, 35, 50, 75]
target = 70

pair = find_pair_with_sum(numbers, target)

if pair:
    print(f"Pair found: {pair[0]} + {pair[1]} = {target}")
else:
    print("No pair found with the given sum.")