# Q95: Write a program to Find longest word.

sentence = input("Enter a sentence: ")

# Split sentence into individual words
words = sentence.split()

longest_word = ""

# Loop through each word to find the maximum length
for word in words:
    # If the current word is longer than our previous champion, update it
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)