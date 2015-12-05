#!/usr/bin/python

def Gen(n):
    return [ x+1 for x in range(n) ]

def checkit(n):
    string = ""
    if n % 3 == 0:
        string += 'Fizz'
    if n % 5 == 0:
        string += 'Buzz'
    if string == '':
        return n

    return string

#Gen Tests
assert Gen(5) == [1,2,3,4,5]
assert len(Gen(100)) == 100

#checkit tests
assert checkit(3) == 'Fizz'
assert checkit(5) == 'Buzz'
assert checkit(15) == 'FizzBuzz'
assert checkit(7) == 7

def main():
    for x in Gen(30):
        print(checkit(x))

if __name__ == '__main__':
    main()
