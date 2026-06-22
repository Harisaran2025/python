import random
print("welcome to number guessing game")
print("guess the number between 1 to 100")
secret_num =random.randint(1,100)
for i in range(0,8):
    try:
        user_input = int(input("enter your guessed number:"))
        if user_input < 1 or user_input > 100:
            print("enter the valid number")
        elif secret_num < user_input:
            print("guessed number is greater than secret number")
        elif secret_num > user_input:
            print("guessed number is smaller than secret number")       
        else:
            print("congratulations! you are right")
            break

    except ValueError:
        print("Invalid Characters, not recognised . Please enter the numbers between 1-100 to play the game")
if secret_num == user_input:
    print(f"Congratulations you guessed the secret number {secret_num} in {i} attempts")
else:
    print("sorry! all your attempts are executed")
