# write a function (called double) that takes and integer n and returns twice
#the value of n

def double(n):
    return n*2

print(double(3))
# Then write a function that takes a double and a list and returns a list
# of each number doubled
new_list = []
def list_double(func, x):
    for item in x:
        new_list.append(func(item))
    return new_list






x = [1,2,3,4,5,6,7]
print(list_double(double, x))
