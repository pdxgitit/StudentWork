# Make function that takes a number and returns a two-dimensional list (i.e. a list of lists) of random
# numbers that are between 1 and n squared.  N should determine the size of the list and the limit on random.
# Example: make_2d(3) should return [[n, n2, n3], [n4, n5, n6], [n7, n8, n9]] where any n is 1 <= n <= 9 (3 squared)

# my attampt:
# import random
# def two_d(n):
#     random_list = []
#     random_num = random.randrange(1, n**2)
#     random_list.append(random_num)
#     print(random_list)
#
# two_d(3)

#how it's done:

import random

def dem_2(n):
    outer = []
    for x in range(n):
        inner = []
        for y in range(n):
            inner.append(random.randint(1, n**2))
        outer.append(inner)
    return outer

print(dem_2(3))
