def answer(x, y, z):
    # your code here
    import datetime
    import itertools

    def validate(perms):
        a = perms[0]
        b = perms[1]
        c = perms[2]
        try:
            datetime.date(a, b, c)
        except ValueError:
            return False
        return True

    def getperms(a, b, c):
        return itertools.permutations((a, b, c))

    def checkreplace(func, lis):
        newlis = []
        for i in lis:
            print(i)
            if func(i):
                newlis.append(i)
                print(str(i) + "Appended")
        return set(newlis)

    valdates = list(checkreplace(validate, getperms(x, y, z)))
    if len(valdates) > 1:
        return "Ambiguous"
    else:
        a = valdates[0][0]
        b = valdates[0][1]
        c = valdates[0][2]
        return "{:02d}/{:02d}/{:02d}".format(b, c, a), valdates

# print(answer(19,19,3))
# print(answer(2,30,3))
print(answer(2,30,2))
