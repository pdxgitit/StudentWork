# write a function (called double) that takes and integer n and returns twice
#the value of n

# Then write a function that takes a double and a list and returns a list
# of each number doubled

def double(n):
    return n * 2

def double_them(func, numlist):
    return [ double(x) for x in numlist ]


print (double_them(double, [1,2,3,4,5,6]))
