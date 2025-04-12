unit = input("Enter unit (C/F): ")
temp  = float(input("Enter temperature: "))
if unit == 'C':
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
elif unit == 'F':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
# The above code converts temperature between Celsius and Fahrenheit based on user input.
# It prompts the user to enter a temperature and its unit, then performs the conversion and displays the result.