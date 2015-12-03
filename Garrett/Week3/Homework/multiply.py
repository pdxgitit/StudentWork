# Given two strings representing positive integers, such as "12" and "35", return a string containing their product.
#
# Disabled                                Accepted
#
# 1. use of `eval`                        1. strings
# 2. use of ints                          2. booleans
# 3. use of floats                        3. arrays
#
# Inputs will never have leading zeros, and neither should your output. Your function, multiplyMyNumbers, should
# handle numbers with up to 5 characters, "13255" for example.

num1 = "11"
num2 = "11"

def stringtoint(stringA, stringB):

    numlist = ["0","1","2","3","4","5","6","7","8","9"]
    num1arr = list(stringA)
    num2arr = list(stringB)
    tempnum = 0


    for x in num1arr:
        for y in num2arr:
            tempnum += (numlist.index(x) * numlist.index(y))

    print (tempnum)

print (stringtoint(num1,num2))
