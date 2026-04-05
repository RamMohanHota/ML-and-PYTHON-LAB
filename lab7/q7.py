def compare(comp_func, a, b):
    return a if comp_func(a, b) else b

print(compare(lambda x, y: x > y, 7, 12)) 