# Q92: Write a program to Find maximum occurring character.

text = input("Enter a string: ")

# Step 1: Count frequencies using a dictionary
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Step 2: Find the character with the maximum count
max_char = ""
max_frequency = 0

for char in char_count:
    if char_count[char] > max_frequency:
        max_frequency = char_count[char]
        max_char = char

# Display the result
print(f"The maximum occurring character is '{max_char}' with a count of {max_frequency}.")