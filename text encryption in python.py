original_str=input("enter the string: ")
sht=int(input("Enter the key number of shifts: "))
encrypted_str=""
for letter in original_str:
  encrypted_letter= ord(letter)+sht
  encrypted_str+=chr(encrypted_letter)
  print(letter,"\t",ord(letter),"\t",encrypted_letter,"\t\t",chr(encrypted_letter))
  print("\nEncrypted string: ",encrypted_str)
