# Given a list of ints, write a function find the highest_product you can get from three of the integers.
# The input list will always have at least three integers.

def product_of_three(alist):
    
    #sort the list to put the highest integers at the end
    alist.sort()

    #set a total for product
    total = 1

    #prune the list to only give back the last three results
    for x in alist[:3:-1]:
        total *= x

    return total

somelist = [1,4,3,20,5,3,10]

print (product_of_three(somelist))
