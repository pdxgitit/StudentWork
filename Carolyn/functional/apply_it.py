# write a function (mult) that takes two numbers and returns the result
# of multiplying those two numbers together
def multipl(num1, num2):
    return num1 * num2
def apply_multipl(func, arg1, arg2):
    return func(arg1, arg2)

print(apply_multipl(multipl, 2, 3))

# now write a function(apply_it) that takes three arguments: a function,
# and two arguments and returns the result of calling the function with
# the two arguments
