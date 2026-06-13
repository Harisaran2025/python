balance=int(input("Enter the balance you have:"))
amount=int(input("enter the amount that you want"))
if amount<=balance:
  if amount%100==0:
    print("please collect your amount")
  else:
    print("select amount of multiples of 100")
else:
  print("insufficient balance")
    
