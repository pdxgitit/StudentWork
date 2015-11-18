# Write a function that takes two numbers and returns a random number between
# and inclusive of the inputs (i.e. make_random(5, 10) should return 5 <= num <= 10)
import random
def rando(a, b):
    print(random.randint(a, b))

rando(1, 5)


# Write a function that:
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# ('hail' -> 'hailing')
# ('swiming' -> 'swimingly')
# ('do' -> 'do')
abby = 'ing'
doug = 'ly'
def ingstring(stuff):
    if stuff[-3:] == abby:
        print(stuff + doug)
    elif len(stuff) >= 3:
        print(stuff + abby)
    else:
        print(stuff)

ingstring('swim')
ingstring('swimming')
ingstring('do')

# write a function that asks the user to input a date in the following format:
# "mm/dd/yyy"
# convert this into a more readable date i.e.:
# "05/24/2003" -> "May 24, 2003"
# start by writing down the steps you will need to take as a series of comments

# user = input('Date: mm/dd/yyyy ')
def dater(user):
    user = input('Date: mm/dd/yyyy ')
    for char in user:
        if user[:2] == '01':
            print('January'+ user[3:])
        elif char[:2] == '02':
            print('February'+ user[3:])
        elif char[:2] == '03':
            print('March'+ user[3:])
        elif char[:2] == '04':
            print('April'+ user[3:])
        elif char[:2] == '05':
            print('May'+ user[3:])
        elif char[:2] == '06':
            print('June'+ user[3:])
        elif char[:2] == '07':
            print('July'+ user[3:])
        elif char[:2] == '08':
            print('August'+ user[3:])
        elif char[:2] == '09':
            print('September'+ user[3:])
        elif char[:2] == '10':
            print('October'+ user[3:])
        elif char[:2] == '11':
            print('November'+ user[3:])
        elif char[:2] == '12':
            print('December'+ user[3:])



# Write a recursive function called count_down(n) that takes an integer n and
# prints every number from n down to one.  Note that for a function that just prints
# numbers you won't need to return anything.
