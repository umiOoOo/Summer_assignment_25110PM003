# Q86: Write a program to Count words in a sentence.

# Taking input from the user
sentence = input("Enter a sentence: ")

# .split() breaks the string into a list of words, ignoring extra spaces
words_list = sentence.split()

# Find the total number of items in the list
word_count = len(words_list)

# Display the result
print("Total number of words:", word_count)