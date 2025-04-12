operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operator == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif operator == '-':
    print(num1, "-", num2, "=", num1 - num2)
elif operator == '*':   
    print(num1, "*", num2, "=", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error! Division by zero.")
elif operator == '%':
    print(num1, "%", num2, "=", num1 % num2)
elif operator == '**':
    print(num1, "**", num2, "=", num1 ** num2)
elif operator == '//':
    if num2 != 0:
        print(num1, "//", num2, "=", num1 // num2)
    else:
        print("Error! Division by zero.")
else:
    print(f"{operator} is a Invalid operator!")
# The above code performs basic arithmetic operations based on user input.