principle = 0
rate = 0
time = 0
 
while principle <= 0:
     principle = float(input("Enter the principle amount: "))
     if principle <= 0:
         print("Please enter a valid amount.")
         
while rate <= 0:
     rate = float(input("Enter the rate of interest: "))
if rate <= 0:
            print("Please enter a valid rate.")
while time <= 0:
     time = float(input("Enter the time in years: "))
if time <= 0:
            print("Please enter a valid time.")

print(principle)        
print(rate)
print(time)    

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")