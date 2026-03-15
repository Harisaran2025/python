import matplotlib.pyplot as plt
a=list(map(int,input("enter the numbers of x axis:").split(',')))
b=list(map(int,input("enter the numbers of y axis:").split(',')))
plt.plot(a,b,c='b',marker='x')
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("Plotting of two numbers")
plt.show()
