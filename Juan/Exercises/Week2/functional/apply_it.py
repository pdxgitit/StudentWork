# write a function (mult) that takes two numbers and returns the result
# of multiplying those two numbers together

def mult(x, y):
    return x * y

# now write a function(apply_it) that takes three arguments: a function,
# and two arguments and returns the result of calling the function with
# the two arguments

def apply_it(func, x, y):
    return func(x, y)

print(apply_it(mult, 5, 5))
