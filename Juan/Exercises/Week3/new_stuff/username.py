# Write a program to take in a first_name and a last_name and creates a username.
# Concatinate the first Initial (make sure it is upper case) and the first seven
# letters in the user's last name.

def intake():
    out = {}
    for i in ["First Name", "Last Name"]:
        while True:
            try:
                out[i] = input("Enter your {}: ".format(i))
                break
            except ValueError:
                print("Please enter a valid text string.")
    return out

def slicer(namearray):
    try:
        first = namearray["First Name"][0].upper()
        last = namearray["Last Name"][:7]
        return first + last
    except:
        return "Error"

print(slicer(intake()))

assert slicer({"First Name" : "Al", "Last Name" : "Skittles"}) == "ASkittle"
assert slicer({"First Name" : 5}) == "Error"
