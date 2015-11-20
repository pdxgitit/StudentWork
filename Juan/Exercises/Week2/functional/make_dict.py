# write a function that takes two lists and returns a dictionary where the first
# list is the keys and the second list is the values.

def make_dict(lis1, lis2):
    out = {}
    diff = len(lis1) - len(lis2)
    if diff != 0:
        if diff > 0:
            while diff > 0:
                lis2.append("")
                diff -= 1
        else:
            while diff < 0:
                lis2.pop(diff)
                diff += 1
    x = 0
    for i in lis1:
        out[i] = lis2[x]
        x += 1
    return out

print(make_dict(['happy', 'times'], ['sad', 'tims', 'rims']))

# if the first list is longer than the second list then the keys should still be
# created with the value set to the empty string

# if the first list is shorter then any elements in the second list with no keys
# should be discarded
