import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guess = 0
is_running = True
print("Welcome to the guessing game!")
print(f"Guess a number between {lowest_num} and {highest_num}!")
while is_running:
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Congratulations! You guessed the correct number!")
        is_running = False
    elif guess < answer:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again."   )  
        
        
print("Thanks for playing!") 