#TO DO LOST
def show_tasks():
  print("\nTo Do List:")
  for i,task in enumerate(tasks,start=1):
    print(i,task)
  print()
def add_task():
  task=input("Enter The New Tasks: ")
  tasks.append(task)
  print("Task",task,"added")
def remove_task():
  show_tasks()
  task_num=int(input("Enter the number of task to be removed: "))
  if 1<=task_num <=len(tasks):
    removed_task=tasks.pop(task_num-1)
    print("Task",removed_task,"removed")
  else:
    print("Invalid task number")
tasks=[]
while True:
  print("\nOptions:")
  print("1. Show Tasks.")
  print("2. Add new tasks")
  print("3. Remove tasks")
  print("4. Quit")
  choice=input("Enter your choice(1/2/3/4): ")
  if choice =="1":
    show_tasks()
  elif choice =="2":
    add_task()
  elif choice =="3":
    remove_task()
  elif choice =="4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please select a valid option.")




 
