furniture_list = ["Chair", "Table", "Sofa", "Bed", "Cabinet"]
cost_list = [50, 150, 300, 450, 200]

def calculate_bill(furniture_name, quantity):
    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return 0

    if furniture_name in furniture_list:
        index = furniture_list.index(furniture_name)
        cost = cost_list[index]
        total_bill = cost * quantity
        return total_bill
    else:
        print("Error: Furniture not available.")
        return 0

furniture_to_order = "Sofa"
quantity_to_order = 2

bill_amount = calculate_bill(furniture_to_order, quantity_to_order)

if bill_amount > 0:
    print(f"The total bill amount for {quantity_to_order} {furniture_to_order}(s) is: ${bill_amount}")
else:
    print("No valid order was placed.")

