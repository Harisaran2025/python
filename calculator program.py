
def calculator():
    print("Simple Calculator (+, -, *, /)")

    while True:
        try:
            num1 = float(input("First number: "))
            op = input("Operation: +,-,*,÷ ")
            num2 = float(input("Second number: "))

            if op == '+': result = num1 + num2
            elif op == '-': result = num1 - num2
            elif op == '*': result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")

            if input("Again? (y/n): ").lower() != 'y':
                break

        except ValueError:
            print("Invalid number!")

calculator()