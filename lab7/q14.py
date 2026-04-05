def filter_long_words(words):
    return list(filter(lambda word: len(word) > 5, words))

print(filter_long_words(["apple", "banana", "kiwi", "strawberry"]))