def atm():
  balance=10000
  while True:
    print("1.Check Balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    ce=int(input("Enter your choice: "))
    if ce==1:
      print("your balance in account is:",balance)
    elif ce==2:
      amt=int(input("enter the amount to be deposited"))
      total_bal=balance+amt
      print("your total balance in account is",total_bal)
    elif ce==3:
      amt=int(input("enter the amount to be withdrawn"))
      if amt>balance:
        print("insufficient balance")
      elif amt<balance:
        total_bal=balance-amt
        print("your total balance in account is",total_bal)
    elif ce==4:
      break
    else:
      print("you have entered wrong choice")
atm()


