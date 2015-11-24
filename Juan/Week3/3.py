# Make function that takes a number and returns a two-dimensional array (i.e. a list of lists) or random
# numbers that are between 1 and n squared.  N should determine the size of the array and the limit on random.
# Example: make_2d(3) should return [[n, n2, n3], [n4, n5, n6], [n7, n8, n9]] where any n is 1 <= n <= 9 (3 squared)

import random

def thingy(n):
    top = n ** 2
    size = range(0, n)
    final = []
    for i in size:
        final.append([])
        for q in size:
            final[i].append(random.randint(1, top))
    return final

print(thingy(3))

def comprehendit(n):
    top = n ** 2
    top = n ** 2
    size = range(0, n)
    final = [[random.randint(1, top) for q in size] for i in size]
    return final

print(comprehendit(3))
