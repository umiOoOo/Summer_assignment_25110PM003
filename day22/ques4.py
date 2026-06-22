# Q88: Write a program to Remove spaces from string.

# Taking input from the user
text = input("Enter a string with spaces: ")

# Initialize an empty string to store the result
no_spaces_text = ""

# Loop through each character
for char in text:
    # Only add the character if it is NOT a space
    if char != " ":
        no_spaces_text += char

# Display the final string
print("String after removing spaces:", no_spaces_text)