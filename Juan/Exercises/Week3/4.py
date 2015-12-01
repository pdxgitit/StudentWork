# Write a function that takes a number and prints a series of numbers that follow this pattern:
#
# If the number is even divide by 2
# Otherwise multiply the number by 3 and add 1
# Print the new number
# If the number equals 1 then terminate the function

def numbertron(n):
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    print(n)
    if n != 1:
        numbertron(n)

numbertron(1)
