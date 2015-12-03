# write a function (mult) that takes two numbers and returns the result
# of multiplying those two numbers together

# now write a function(apply_it) that takes three arguments: a function,
# and two arguments and returns the result of calling the function with
# the two arguments

def mult(num1, num2):
    return num1*num2

def apply_it(func, num1, num2):
    return func(num1, num2)

print(apply_it(mult, 3, 4))
