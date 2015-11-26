def gen(n):
    return [x for x in range(1, n + 1)]

def change(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return n

for i in gen(int(input("Gimme a number: "))):
    print(change(i))

# Test change function
assert change(3) == "Fizz"
assert change(5) == "Buzz"
assert change(15) == "FizzBuzz"
assert change(7) == 7

# Test gen function
assert len(gen(100)) == 100
assert gen(5) == [1,2,3,4,5]

# All test passed break
print("All Tests Passed")
