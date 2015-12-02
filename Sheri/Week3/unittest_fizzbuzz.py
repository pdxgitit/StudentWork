#practicing unit testing with fizz buzz
def gen(a):
    nums = []
    for i in range(1, a+1):
        nums.append(i)
    return nums

assert len(gen(100))== 100

assert gen(5) ==[1,2,3,4,5]




def func(num):
    if num % 15 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num


assert func(3) == "fizz"
assert func(5) == "buzz"
assert func(15) == "fizzbuzz"
assert func(7) == 7


def giveanum():
    vara = int(input("Enter a number "))
    varb = gen(vara)
    for i in varb:
        print(func(i))
#assert giveanum() == 3 #enter 3 when promped
giveanum()
