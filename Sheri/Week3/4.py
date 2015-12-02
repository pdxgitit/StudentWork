# Write a function that takes a number and prints a series of numbers that follow this pattern:
#
# If the number is even divide by 2
# Otherwise multiply the number by 3 and add 1
# Print the new number
# If the number equals 1 then terminate the function


def takea_number(n):
    if n ==1:
        print("end of program")
        return
    if n % 2 == 0:
        n = n/2
        print(n)
    else:
        n = n/3 + 1
        print(n)
        if n == 1:
            print ("end of program")
            return


takea_number(11)
