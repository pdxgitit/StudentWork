# write a function that takes two lists and returns a dictionary where the first
# list is the keys and the second list is the values.

# if the first list is longer than the second list then the keys should still be
# created with the value set to the empty string

# if the first list is shorter then any elements in the second list with no keys
# should be discarded

def make_dict(keys, values):

    newdict = {}

    if len(keys) > len(values):
        for i in range(len(keys)):
            if !values[i]:
                newdict[keys[i]] = ""
            else:
                newdict[keys[i]] = values[i]

    if len(keys) < len(values):
        for i in range(len(keys)):
            if !key[i]:
                pass
            else:
                newdict[keys[i]] = values[i]

        return newdict

print (make_dict([1,2,3,4,5], ['a','b','c','d','e','f']))
