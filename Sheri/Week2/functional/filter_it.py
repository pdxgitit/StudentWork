# write a function (is_even(n)) that returns true or false depending on whether
# a number is even or not

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# now write a function (filter_it) that takes a function and a list and returns
# a new list of numbers that are even.
liszt = list(range(2, 78))

def filter_it(funct, liszt):
    new_list = []
    for i in liszt:

        if funct(i):
            new_list.append(i)
    return new_list

print(filter_it(is_even, liszt))
# write a function (is_even(n)) that returns true or false depending on whether
# a number is even or not

# now write a function (filter_it) that takes a function and a list and returns
# a new list of numbers that are even.
