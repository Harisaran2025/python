import random
choices = ["rock", "paper", "scissors"]           # Choices
user_score = 0           # Scores
computer_score = 0       # Scores
# Infinite loop
while True:
    computer = random.choice(choices)                                    # Computer choice
    user = input("\nEnter rock, paper, scissors or quit: ").lower()      # User choice
# Exit condition
    if user == "quit":
        print("\nGame Over!")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break
# Check valid input
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    print("Computer chose:", computer)
# Match conditions
    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
# Display scores
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
