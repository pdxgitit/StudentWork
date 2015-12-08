# Write a function that takes a number and prints a series of numbers that follow this pattern:
#
# If the number is even divide by 2
# Otherwise multiply the number by 3 and add 1
# Print the new number
# If the number equals 1 then terminate the function

def printnum(num):
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        
        print(int(num))

        if num == 1:
            break

printnum(100)
