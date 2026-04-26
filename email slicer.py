email = input("Enter email: ")   #users input mail

if "@" in email:
    username, domain = email.split("@")    #splitting the emai
    print("Username:", username)           #PRINT THE USERNAME
    print("Domain:", domain)               #PRINT THE DOMAIN
else:
    print("Invalid Email")         
