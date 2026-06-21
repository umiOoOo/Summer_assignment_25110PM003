# Q84: Write a program to Convert lowercase to uppercase.

# Taking input from the user
text = input("Enter a string: ")

result = ""

# Loop through each character
for char in text:
    # Check if the character is a lowercase letter (ASCII 97 to 122)
    if 'a' <= char <= 'z':
        # Convert to uppercase by subtracting 32 from its ASCII value
        uppercase_char = chr(ord(char) - 32)
        result += uppercase_char
    else:
        # Keep uppercase letters, numbers, and symbols as they are
        result += char

# Display the result
print("Uppercase string:", result)



# Alternative built-in method
text = input("Enter a string: ")
print("Uppercase string:", text.upper())