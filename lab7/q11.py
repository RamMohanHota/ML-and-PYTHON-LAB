from functools import reduce

def product_of_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(product_of_list([1, 2, 3, 4]))
