# write a function (is_even(n)) that returns true or false depending on whether
# a number is even or not

# now write a function (filter_it) that takes a function and a list and returns
# a new list of numbers that are even.

def is_even(n):
    if n % 2 == 0:
        return True
'''
def filter_it(func, numlist):
    return [ x for x in numlist if is_even(x) == True]
'''

def filter_it(numlist):
    return [ (lambda x: x % 2 == 0)(x) for x in numlist ]


print (filter_it([1,2,3,4,5,6,7,8,9]))
