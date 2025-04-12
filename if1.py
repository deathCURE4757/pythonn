age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old.")
elif age >= 18:
    print("You are a young adult.")
elif age < 0:
    print("Invalid age.")
else:
    print("You are a minor.")