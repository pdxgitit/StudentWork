# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function that takes a list of integers and returns a list of the products.
#
# For example, given:
#   [1, 7, 3, 4]
#
# your function would return:
#   [84, 12, 28, 21]
#
# by calculating:
#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]

alist = [1,7,3,4]

def productlist(listone):
    originallist = listone
    newlist = []
    for x in originallist:
        total = 1
        indexone = originallist.index(x)
        for y in originallist:
            indextwo = originallist.index(y)
            if indexone != indextwo:
                total *= y
        newlist.append(total)

    return newlist

print (productlist(alist))

