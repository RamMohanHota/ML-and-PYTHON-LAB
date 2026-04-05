def celsius_to_fahrenheit(celsius_list):
    return list(map(lambda c: (c * 9/5) + 32, celsius_list))

print(celsius_to_fahrenheit([0, 37, 100]))