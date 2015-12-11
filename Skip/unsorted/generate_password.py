# Write a password generator in Python. Be creative with how you generate
# passwords - strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your code in a main
# method.

import random
import string

#genpass = input("Do you want to generate a new password? YN")
genpass = "Y"

charstring = string.ascii_letters + string.digits

def getpass():
    password = ""
    while len(password) <= 16:
        for x in charstring:
            if random.randrange(1,100) > 95:
                password += x

    password = password[:16]

    return password

print(getpass())
#print(charstring)
