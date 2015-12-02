# write a function that returns the factorial of a number.  It does not have
# to be done recursively.  Remember 5! is 5*4*3*2*1

def factoRama(n):
    if n < 1:
        return 1
    else:
        return n * factoRama(n -1)

print(factoRama(5))
