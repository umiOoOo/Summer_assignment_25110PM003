# Q81: Write a program to Find string length without len().

# Taking input from the user
text = input("Enter a string: ")

# Initialize a counter variable to 0
length = 0

# Loop through each character in the string
for char in text:
    length += 1

# Display the result
print("The length of the string is:", length)