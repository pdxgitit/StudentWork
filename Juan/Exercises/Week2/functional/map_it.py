# write a function (called double) that takes and integer n and returns twice
#the value of n

def double(n):
    return n * 2

# Then write a function that takes a double and a list and returns a list
# of each number doubled

def apply_it(func, n):
    return [func(i) for i in n]

Quibble = [1,2,3,4]
print(apply_it(double, Quibble))
