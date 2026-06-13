a=int(input("enter th number:"))
b=int(input("enter the number:"))
for i in range(a, b):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
