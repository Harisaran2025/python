import random
while True:
    input("Press Enter to roll the dice...")       #user input
    dice = random.randint(1, 6)                    #systems random input
    print("You got:", dice)                        #output od dice rolled
    choice = input("Roll again? (yes/no): ")       #options for game
    if choice.lower() != "yes":
        break
print("Game Over!")
