# Q100: Write a program to Sort words by length.

sentence = input("Enter a sentence: ")
words = sentence.split()

# Sort using the length of the word as the sorting criteria
sorted_words = sorted(words, key=len)

print("Words sorted by length:")
print(sorted_words)