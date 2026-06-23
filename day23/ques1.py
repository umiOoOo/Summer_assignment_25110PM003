# Q89: Write a program to Find first non-repeating character.

text = input("Enter a string: ")

# Step 1: Count frequencies of all characters
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Step 2: Find the first character with a count of 1
found = False
for char in text:
    if char_count[char] == 1:
        print("The first non-repeating character is:", char)
        found = True
        break

if not found:
    print("There are no non-repeating characters.")