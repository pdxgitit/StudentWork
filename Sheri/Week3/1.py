# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
#  3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_sum():
    num_list = []
    for i in range(1, 10001):
        if i % 3 == 0:
            num_list.append(i)
        if i % 5 ==0:
            num_list.append(i)
    ans = 0
    for i in num_list:
        ans = ans + i
    return ans
print(find_sum())


    # make a list of the numbers 1 - 1000
    # make a new list of the numbers that are multiples of 3 or 5
    #get the sum of all the numbers
