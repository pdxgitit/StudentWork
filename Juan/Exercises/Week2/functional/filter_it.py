# write a function (is_even(n)) that returns true or false depending on whether
# a number is even or not

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# now write a function (filter_it) that takes a function and a list and returns
# a new list of numbers that are even.

def filter_it(func, lis):
    out = [func(i)   for i in lis]
    return out

Quarble = [1,2,3,4]
print(filter_it(is_even, Quarble))
