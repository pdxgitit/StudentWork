list = [0,1,3,3,4,5,6,7,8,8,8,8]

for x in range(len(list)):
    if list[x] == list[x+1]:
        print (list[x])
