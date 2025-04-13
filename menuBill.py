menu = {"pizza": 10,
     "burger": 5,
     "soda": 2, 
     "salad": 4, 
     "fries": 3,
     "dessert": 6,
     "water": 1,
     "coffee": 2,
     "tea": 2,
     "juice": 3,
     "sandwich": 5,
     "pasta": 8,
     "steak": 15,
     "chicken": 12 }
cart = []
total = 0

print("Welcome to the restaurant menu!")
print("-------Here is the menu--------")
# Display the menu
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")    
print("-------End of the menu--------")
print("Please select items from the menu to add to your cart.")
print("Type 'done' when you are finished.")
while True:
    item = input("Enter an item from menu: ").lower()
    if item == "done":
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"{item} added to cart.")
    else:
        print("Item not found in the menu.")
print("-------Your cart--------")  
for item in cart:
    print(item)
print(f"Total: ${total:.2f}") 
# Display the total amount         