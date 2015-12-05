# Given a string which may include opening or closing round brackets, write a function to determine
# whether the string contains a balanced pair(s) of round brackets, that is there are no brackets
# which are either opened & not closed, or vice versa. Opening round brackets always have to come
# before closing bracket. An empty string is balanced.
#
#isBalanced("hi)(") == False
#isBalanced("hi(hi)") == True
#isBalanced("(") == False

def paran(string):
    balance = 0

    for x in string:
        if x == '(':
            balance += 1
        if x == ')' and balance >= 1:
            balance -= 1
    
    if balance == 0:
        return True
    else: 
        return False

print (paran("hi((hi))"))


