#  A meeting is stored as tuples of integers (start_time, end_time). These integers represent the number 
#  of 30-minute blocks past 9:00am.
#
# For example:
#
# (2, 3) # meeting from 10:00 – 10:30 am
# (6, 9) # meeting from 12:00 – 1:30 pm
#
# Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges.
#
# For example, given:
#
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return:
#
#   [(0, 1), (3, 8), (9, 12)]

alist = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def returnrange(tupleA):
    return [ x for x in range(tupleA[0], tupleA[1]) ]

def condense_meeting_times(listone):
    #copy initial list
    listtwo = listone[:]
    #make new list
    newlist = []
    #for every tuple
    for x in listone:
        #compare to other tuples
        #break tuple, and get a list range
        timerange = returnrange(x)
        highernum = 0
        for y in listtwo:
            #if the first number is part of the range
            if y[0] in timerange:
                #if the second 
                if x[1] <= y[1] and highernum <= y[1]:
                    highernum = y[1]
                else:
                    highernum = x[1]
        print (x[0], highernum)


print (condense_meeting_times(alist))
