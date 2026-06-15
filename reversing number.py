num = int(input("Enter number: "))
reverse = 0     #variable to store reverse numbers 
while num > 0:
    digit = num % 10     # %-it helps to takeout last digit
    reverse = reverse * 10 + digit   
    num = num // 10      # //-it helps to remove last digit

print("Reverse =", reverse)
