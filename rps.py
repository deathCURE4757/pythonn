import random

option = ("rock", "paper", "scissors")
player = None
computer = random.choice(option)
print("Welcome to Rock, Paper, Scissors!")
print("Choose your option:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Quit")
while True:
    player = input("Enter your choice (1-4): ")
    if player == "1":
        player = "rock"
    elif player == "2":
        player = "paper"
    elif player == "3":
        player = "scissors"
    elif player == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    computer = random.choice(option)