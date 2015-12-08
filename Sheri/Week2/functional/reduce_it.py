# write a function that takes two strings and concatinates them together
# call this function "cat".

def cat(string1, string2):
    new_string = string1 + string2

# now write a function that takes a function and a list of strings and applies
# the cat function to each element in the list and returns the resulting string

def resulting_string(func, listostrings):
    for i in listostrings:
        func(i)
resulting_string(cat(["dog", ])
