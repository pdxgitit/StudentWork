# write a function that returns the factorial of a number.  It does not have
# to be done recursively.  Remember 5! is 5*4*3*2*1

def factorial(n):
    num = n
    while n > 1:
        n -= 1
        num *= n
    return num

print(factorial(5))
