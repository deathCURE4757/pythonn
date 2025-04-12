weight = float(input("Enter weight: "))
unit = input("Enter unit (kg/lb): ")

if unit == 'kg':
    converted_weight = weight * 2.20462
    print(f"{weight} kg is equal to {converted_weight:.2f} lb")
elif unit == 'lb':
    converted_weight = weight / 2.20462
    print(f"{weight} lb is equal to {converted_weight:.2f} kg")
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")
# The above code converts weight between kilograms and pounds based on user input.
# It prompts the user to enter a weight and its unit, then performs the conversion and displays the result.