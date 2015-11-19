# Write a function that takes two numbers and returns a random number between
# and inclusive of the inputs (i.e. make_random(5, 10) should return 5 <= num <= 10)

import random
def make_random(x, y):
    return random.randint(x, y)

print(make_random(5,10))

# Write a function that:
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def fix_string(str):
    strl = len(str)
    strend = str[-3:]
    inger = "ing"
    if strl >= 3:
        if strend == inger:
            str = str[:-3] + "ly"
        else:
            str += inger
    return str

print(fix_string("Hemoglobing"))

# ('hail' -> 'hailing')
# ('swiming' -> 'swimingly')
# ('do' -> 'do')


# write a function that asks the user to input a date in the following format:
# "mm/dd/yyy"
# convert this into a more readable date i.e.:
# "05/24/2003" -> "May 24, 2003"
# start by writing down the steps you will need to take as a series of comments

import datetime
def ask_me():
    # Acquire user input and store as a variable
    udate = input("Please enter a date (mm/dd/yyyy): ")
    # Parse date and convert to a value that can be manipulated, then change that date and store in a variable
    outdate = datetime.datetime.strptime(udate, "%m/%d/%Y").strftime("%B %d, %Y")
    # Return the value
    return outdate

print(ask_me())


# Write a recursive function called count_down(n) that takes an integer n and
# prints every number from n down to one.  Note that for a function that just prints
# numbers you won't need to return anything.

def count_down(n):
    print(n)
    if n > 1:
        count_down(n-1)

count_down(10)
