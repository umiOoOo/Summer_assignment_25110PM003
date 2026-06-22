# Q85: Write a program to Check palindrome string.

# Taking input from the user
text = input("Enter a string: ")

# Convert to lowercase so the check is case-insensitive (e.g., 'Radar' becomes 'radar')
clean_text = text.lower()

# Reverse the string using slicing
reversed_text = clean_text[::-1]

# Check if the original matches the reversed string
if clean_text == reversed_text:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")