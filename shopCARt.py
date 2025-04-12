item = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity: "))
price_per_item = float(input("Enter the price per item: "))
total_cost = quantity * price_per_item

print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price per item: {price_per_item}")
print(f"Total cost: {total_cost}")