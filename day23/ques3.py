# Q91: Write a program to Check anagram strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Clean up strings by converting to lowercase and removing spaces
str1_clean = str1.lower().replace(" ", "")
str2_clean = str2.lower().replace(" ", "")

# Sort the characters of both strings
# sorted() returns a sorted list of characters (e.g., ['e', 'l', 'n', 's', 't'])
if sorted(str1_clean) == sorted(str2_clean):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")