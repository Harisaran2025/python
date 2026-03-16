import matplotlib.pyplot as plt
subjects = input("Enter subjects separated by comma: ").split(",")
marks = list(map(int, input("Enter marks separated by comma: ").split(",")))
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
