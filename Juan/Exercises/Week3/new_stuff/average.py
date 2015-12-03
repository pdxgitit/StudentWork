# Write a function that can take any number of comma separated values and
# returns the average of the values.  (Think *args)

def getavs(*args):
    result = 0
    totargs = 0
    for i in args:
        if type(i) == float or type(i) == int:
            result += i
            totargs += 1
    assert type(result) == int or type(result) == float
    return result/totargs

assert getavs(2.0, 2, 2) == 2
assert getavs(2, 2, "python") == 2

# Once you have that working write a function that can open a file and read in the
# numbers inside in one of two formats (see nums.txt and nums2.txt) and print the
# average to the screen.

import io
import re

def openread(filename):
    with io.open(filename, 'r', encoding = 'utf-8') as f:
        nums = f.read()
    nums = filter(None, re.split('[\n ,]', nums))
    out = 0
    count = 0
    for i in nums:
        out += float(i)
        count += 1
    out /= count
    return out


assert openread('nums.txt') == 25
assert openread('nums2.txt') == 25
print("All Tests Passed!")
