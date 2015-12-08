# Find the length of the longest substring in the given string s that is the same in reverse.
# As an example, if the input was “I like racecars that go fast”, the substring length would be 7.
# If the length of the input string is 0, return value must be 0.
#
# Examples:
#
# "a" -> 1
# "aab" -> 2
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0

def pali(stringA):
    length = 0
    stringlist = list(stringA)
    for x in range(len(stringlist)):
        if stringlist[x] == stringlist[x-1]:
            length += 1
        print ("1:", x+1)
        print("2:", len(stringA) + 1)
        if stringlist[x] == stringlist[x+1]:
            length += 1
    print (length)



print (pali("aab"))
            
