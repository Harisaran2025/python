import matplotlib.pyplot as plt
n = int(input("Enter number of students: "))
students = []
marks = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    students.append(name)
    marks.append(mark)
pass_mark = float(input("Enter pass mark limit: "))
pass_students = []
pass_marks = []
fail_students = []
fail_marks = []

for i in range(n):
    if marks[i] >= pass_mark:
        pass_students.append(students[i])
        pass_marks.append(marks[i])
    else:
        fail_students.append(students[i])
        fail_marks.append(marks[i])
plt.figure(figsize=(8,5))
plt.plot(pass_students, pass_marks, marker='o', color='green', label="Pass")
plt.plot(fail_students, fail_marks, marker='o', color='red', label="Fail")
plt.axhline(y=pass_mark, linestyle='--', color='blue', label=f"Pass Mark ({pass_mark})")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.legend()
plt.grid()
plt.show()
