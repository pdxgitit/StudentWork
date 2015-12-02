# Write a program to take in a first_name and a last_name and creates a username.
# Concatinate the first Initial (make sure it is upper case) and the first seven
# letters in the user's last name.
def main():
    first = firstName()
    last = lastName()
    a = firstInitial(first)
    b = str(firstSeven(last))
    c = str(allTogether(a, b))
    print (c)


def firstName():
    first_name = input("Enter your first name: ")
    return first_name

def lastName():
    last_name = input("Enter your last name: ")
    return last_name

def firstInitial(first):
    first_initial = first.upper()[0]
    return first_initial

def firstSeven(last):
    first_seven = last.lower()[:8]
    return first_seven

def allTogether(a, b):
    username = a + b
    return(username)

main()
