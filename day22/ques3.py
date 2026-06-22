# Q87: Write a program to Find character frequency.

# Taking input from the user
text = input("Enter a string: ")

# Initialize an empty dictionary to store counts
frequency_dict = {}

# Loop through each character in the string
for char in text:
    # If the character is already in the dictionary, increase its count
    if char in frequency_dict:
        frequency_dict[char] += 1
    # If it's a new character, add it to the dictionary with a count of 1
    else:
        frequency_dict[char] = 1

# Display the frequencies cleanly
print("Character frequencies:")
for char, count in frequency_dict.items():
    print(f"'{char}': {count}")