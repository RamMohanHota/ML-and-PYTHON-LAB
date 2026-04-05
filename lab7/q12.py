from functools import reduce

def concatenate_strings(strings):
    return reduce(lambda x, y: x + y, strings)

print(concatenate_strings(["Hello", " ", "World", "!"]))