# Q96: Write a program to Remove duplicate characters.

text = input("Enter a string: ")

result = ""

# Loop through each character
for char in text:
    # Check if the character is already in our result string
    if char not in result:
        result += char

print("String after removing duplicates:", result)