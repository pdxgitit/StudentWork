import random
import math

SHIPLEN = 2
BOARD = []

def generateboard(n):
    for x in range(n):
        for y in range(n):
          BOARD.append((x,y))

def printboard(board):
    bound = 6
    counter = 0
    for x in board:
        counter += 1
        if x == (bound * -1, bound * -1):
            print(" X ", end="")
        else:    
            #print(" O ", end="")
            print(x, end="")
        if bound == counter:
            counter = 0
            print ()

def placeship(shiplen):
    anchor = random.choice(BOARD)
    y, x = anchor[0], anchor[1]

    direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    if direction == 'UP' and y != 0:
        y -= (shiplen - 1)
    elif direction == 'DOWN' and y != 5:
        y += (shiplen - 1)
    elif direction == 'LEFT' and x != 0:
        x -= (shiplen - 1)
    elif direction == 'RIGHT' and x != 5:
        x += (shiplen - 1)

    if y == -1 or x == -1 or y == 6 or x == 6:
        return placeship(shiplen)
    elif (anchor != (y,x)):
        return ((y, x), anchor)
    else:
        return placeship(shiplen)

def updateboard(ship):
    marker = 6
    for boat in ship:
        for xy in BOARD:
            if boat == xy:
                temp = BOARD.index(boat)
                BOARD.remove(boat)
                BOARD.insert(temp, (marker,marker))

def attack(x,y):
    strike = -6
    marker = 6
    try:
        for xy in BOARD:
            if (x, y) == xy:
                temp = BOARD.index(xy)
                BOARD.remove(xy)
                BOARD.insert(temp, (strike, strike))
                print("MISS")
        temp = BOARD.index(x,y)
    except:
        print()
        #BOARD.insert(temp, (strike, strike))


generateboard(6)
printboard(BOARD)
ship = placeship(2)
updateboard(ship)
print ("next")
printboard(BOARD)
print (ship)
attack(1,2)
printboard(BOARD)
