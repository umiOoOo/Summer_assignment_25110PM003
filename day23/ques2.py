# Q90: Write a program to Find first repeating character.

text = input("Enter a string: ")

seen_characters = []
found = False

# Loop through each character
for char in text:
    # If the character has been seen before, it is the first repeating one
    if char in seen_characters:
        print("The first repeating character is:", char)
        found = True
        break
    else:
        # Otherwise, add it to our tracking list
        seen_characters.append(char)

if not found:
    print("No repeating characters found.")