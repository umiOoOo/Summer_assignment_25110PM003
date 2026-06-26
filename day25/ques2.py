# Q98: Write a program to Find common characters in strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common_chars = []

# Loop through the first string
for char in str1:
    # If character is in the second string and not already counted
    if char in str2 and char not in common_chars and char != " ":
        common_chars.append(char)

print("Common characters:", common_chars)