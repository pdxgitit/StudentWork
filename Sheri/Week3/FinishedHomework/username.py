# Write a program to take in a first_name and a last_name and creates a username.
# Concatinate the first Initial (make sure it is upper case) and the first seven
# letters in the user's last name.

def user_name():
    first_name = input("What is your first name? ")
    last_name = input("What is you last name? ")
    firstlet = first_name[0]
    firstseven = last_name[:8]
    username = firstlet.upper() + firstseven.lower()
    print(username)
username()
