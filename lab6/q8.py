prices = {"laptop": 55000, "phone": 25000, "tablet": 18000}
max_product = max(prices, key=prices.get)
print("\nQ8 Output: Product with maximum price:", max_product, "->", prices[max_product])
