# Write a function that takes two numbers and returns a random number between
# and inclusive of the inputs (i.e. make_random(5, 10) should return 5 <= num <= 10)

import random

def make_random(x,y):
    return random.randint(x,y)

print(make_random(6,10))

# Write a function that:
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# ('hail' -> 'hailing')
# ('swiming' -> 'swimingly')
# ('do' -> 'do')

#
def ingly(s):
    if len(s) >= 3:
        return s + "ing"
    elif len(s) < 3:
        return s
    else:
        if s.endswith(ing):
            return s + "ly"

print (ingly("man"))
#
# write a function that asks the user to input a date in the following format:
# "mm/dd/yyyy"
# convert this into a more readable date i.e.:
# "05/24/2003" -> "May 24, 2003"
# start by writing down the steps you will need to take as a series of comments

# - ask for input date format
# - name a variable for that input
# - run a function on that variable that converts the format to 'Month Day,
   # Year' format

# import datetime
#
#
# print(now)
#
#import string

def main():
    #get the date
    dateStr = input("Please enter a date (mm/dd/yyyy): ")

    #split in to components

    monthStr, dayStr, yearStr = dateStr.split("/")
    #convert monthStr to the month name
    #date1 = str(month)+"/"+str(day)+"/"+str(year)
    months = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]
    #date2 = monthStr+" " + str(day) + ", " + str(year)
    #output the result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)

main()
# import string
#
# def main():
#     #get the day month and Year
#     day, month, year = input("Please enter day, month, and year numbers: ")
#
#     date1 = str(month)+"/"+str(day)+"/"+str(year)
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     monthStr = months[month-1]
#     date2 = monthStr+" " + str(day) + ", " + str(year)
#
#     print("The date is", date1, "or", date2+".")
#
# main()

#




# Write a recursive function called count_down(n) that takes an integer n and
# prints every number from n down to one.  Note that for a function that just prints
# numbers you won't need to return anything.


def countdown(n):
    while n >=1:
        print(n)

        return countdown(n - 1)
print(countdown(45))
