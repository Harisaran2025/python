with open("/sample.txt", "r") as file:  #'r' helps to read the file
    content = file.read()
print(content)

with open("/sample.txt", "w") as file:   #'w' it helps to write in the file
    file.write("Hello Python\n")
    file.write("Welcome to File Handling")
print("Data written successfully!")

with open("/sample.txt", "a") as file:    #'a' it helps to append the content in file
    file.write("\nThis line is appended.")
print("Data appended successfully!")

with open("/sample.txt", "r") as source:   
    data = source.read()

with open("/copy.txt", "w") as destination:
    destination.write(data)
print("File copied successfully!")
