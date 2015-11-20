# write a function that takes two strings and concatinates them together
# call this function "cat".

def cat(s1, s2):
    return s1 + s2

# now write a function that takes a function and a list of strings and applies
# the cat function to each element in the list and returns the resulting string

def apply_it(func, lis):
    out = type(lis[0])()
    for i in lis:
        out = func(out, i)
    return out

squak = ["bla", "squak", "blark"]
print(apply_it(cat, squak))
print(apply_it(cat, [1,2,3,6]))
