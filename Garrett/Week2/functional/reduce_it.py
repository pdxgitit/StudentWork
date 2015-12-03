# write a function that takes two strings and concatinates them together
# call this function "cat".

# now write a function that takes a function and a list of strings and applies
# the cat function to each element in the list and returns the resulting string


def cat(stringA, stringB):
    return stringA + stringB

def docat(func, stringlist):
    placeholder = ""
    for x in stringlist:
        placeholder = func(placeholder, x)

    return placeholder

strings = ["a", "big", "fat", "phony" ]

print(docat(cat, strings))
