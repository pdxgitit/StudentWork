# write a program that prints out all the elements of the list that are less
# than 10.  Bonus for letting a user decide the threshold.
user = int(input('Give me a number: '))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for item in a:
        if item < user:
            print(item)




# write a function that checks if a string (first argument) ends with
# the given target string (second argument).

# i.e. confirm_ending("Sebastian", "n") == True

def confirm_ending(x,y):
    hi = len(y)*(-1)
    if x[hi:] == y:
        print("True")
    else:
        print("False")

confirm_ending("Sebastian", "ian")



# Return true if the string in the first element of the array contains
# all of the letters of the string in the second element of the array.
# For example, ["hello", "Hello"], should return true because all of the letters
# in the second string are present in the first, ignoring case.
# The arguments ["hello", "hey"] should return false because the string "hello"
# does not contain a "y". Lastly, ["Alien", "line"], should return true because
# all of the letters in "line" are present in "Alien".
