text = "Python is fun and Python is powerful"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(" Output:", frequency)
