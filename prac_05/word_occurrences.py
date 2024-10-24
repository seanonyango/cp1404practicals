"""
Word Occurrences
Estimate: 20 minutes
Actual: 9 minutes
"""
word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = words.count(word)

for word in word_to_count:
    print(f"{word}: {word_to_count[word]}")