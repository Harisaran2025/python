import random
import string
# Function to generate password
def gen_pass(length):
    char = string.ascii_letters + string.digits + string.punctuation   #ascii_letters --> letters from A-Z and a-z
    password = ''.join(random.choice(char) for i in range(length))    # Combine all characters of letters, digits, symbols
    return password
length = int(input("Enter password length: "))
password = gen_pass(length)
print("Generated Password:", password)
