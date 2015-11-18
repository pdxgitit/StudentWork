# Write a function that takes two numbers and returns a random number between
# and inclusive of the inputs (i.e. make_random(5, 10) should return 5 <= num <= 10)
import random

def make_random(x, y):
    return random.randrange(x,y)

print (make_random(5,10))

# Write a function that:
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# ('hail' -> 'hailing')
# ('swiming' -> 'swimingly')
# ('do' -> 'do')

verb = "swim"

def brit(string):

    if len(string) < 3:
        pass
    elif string[-3:] == "ing":
        string += "ly"
    else:
        string += "ing"

    return string 

print (brit(verb))

# write a function that asks the user to input a date in the following format:
# "mm/dd/yyy"
# convert this into a more readable date i.e.:
# "05/24/2003" -> "May 24, 2003"
# start by writing down the steps you will need to take as a series of comments

#getdate = input("Date please")
getdate = "11/09/2015"

#split date into list
datelist = getdate.split('/')

#convert month number to month string
def month(x):
	x = int(x) - 1 
	months = ['January',
                 'Feburary',
                 'March',
                 'April',
                 'May',
                 'June',
                 'July',
                 'August',
                 'September',
                 'October',
                 'November',
                 'December']
	return months[x]

#function for syntactic sugar
def day(x):
	return x

#function for syntactic sugar
def year(x):
	return x

print ("{} {}, {}".format(month(datelist[0]), day(datelist[1]), year(datelist[2])))

# Write a recursive function called count_down(n) that takes an integer n and
# prints every number from n down to one.  Note that for a function that just prints
# numbers you won't need to return anything.

def count_down(n):
    if n == 0:
        print ()
        return 0
    else:
        print (n, end=" ")
        return count_down(n - 1)

count_down(10)
