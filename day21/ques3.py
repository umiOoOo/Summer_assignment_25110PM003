# Q83: Write a program to Count vowels and consonants.

# Taking input from the user
text = input("Enter a string: ")

# Define a string containing all vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through each character in the string
for char in text:
    # Check if the character is an alphabet letter
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display the counts
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)