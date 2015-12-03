# Write program to calculate the value of some change in dollars.  Ask for
# user input for each type of coin.  Calculate the total and print it to the
# screen.

def convertcoins(coin, num):
    '''
    Takes a single coin and count pair
    returns float of total output
    '''
    num *= 100
    try:
        if coin == "quarter":
            out = num / 4
        elif coin == "dime":
            out = num / 10
        elif coin == "nickel":
            out = num / 20
        elif coin == "pennie":
            out = num / 100
        return out
    except:
        return "Input error."


def addcoins(coins):
    tot = 0
    if type(coins) != dict:
        return "Invalid data type."
    try:
        for t in coins:
            tot += convertcoins(t, coins[t])
    except:
        return "Loop error. Invalid input."
    return tot / 100

def getcoins():
    choices = ["quarter", "nickel", "dime", "pennie"]
    out = {}
    for c in choices:
        while True:
            try:
                out[c] = int(input("How many {}s do you have? ".format(c)))
                break
            except ValueError:
                print("Please enter an whole number.")
    print(addcoins(out))

getcoins()

# addcoins function tests
assert addcoins({"quarter" : 5}) == 1.25
assert addcoins({"quarter" : 5, "pennie" : 6}) == 1.31
assert addcoins({"quarter" : "five"}) == "Loop error. Invalid input."
assert addcoins(["quarter", 5]) == "Invalid data type."

# convertcoins function tests
assert convertcoins('quarter', 5) == 125
assert type(convertcoins('pennie', 200)) == float
assert convertcoins('pennie', 197) == 197
assert convertcoins('dime', 'ten') == "Input error."
assert convertcoins('penguin', 10) == "Input error."
print("All tests passed!")
