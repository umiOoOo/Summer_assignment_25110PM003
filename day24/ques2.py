# Q94: Write a program to Compress a string.

text = input("Enter a string to compress: ")

# Handle edge case for an empty string
if not text:
    print("Compressed string: ")
else:
    compressed = ""
    count = 1

    # Loop through the string up to the second-to-last character
    for i in range(len(text) - 1):
        # If the current character matches the next one, increment count
        if text[i] == text[i + 1]:
            count += 1
        else:
            # If it changes, append the character and its count to our result
            compressed += text[i] + str(count)
            count = 1  # Reset count for the new character

    # Append the very last character and its count
    compressed += text[-1] + str(count)

    print("Compressed string:", compressed)