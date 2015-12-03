# Carolyn = 7
def main():
    user = eval(input('Please enter a number: '))
    for x in range(1, user + 1):
        print(buzz(x))

def buzz(y):
    if y % 15 == 0:
        return 'FizzBuzz'
    if y % 5 == 0:
        return "Buzz"
    elif y % 3 == 0:
        return 'Fizz'
    else:
        return y


# assert len(fizz(10)) == 10
# assert fizz(5) == [1,2,3,4,5]
assert buzz(3) == 'Fizz'
assert buzz(5) == "Buzz"
assert buzz(15) == 'FizzBuzz'
assert buzz(4) == 4

main()
