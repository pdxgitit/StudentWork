# write a function (called double) that takes and integer n and returns twice
#the value of n

def double(n):
    return n * 2

# Then write a function that takes a double and a list and returns a list
# of each number doubled

num_list = [1,2,3,4,5,6,7,8,9]

doubled_list = [double(num)  for num in num_list ]

print (doubled_list)
