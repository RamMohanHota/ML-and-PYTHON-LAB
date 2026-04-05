def palindrom(word):
    return word==word[::-1]
print(palindrom("itamati"))
print(palindrom("hello"))