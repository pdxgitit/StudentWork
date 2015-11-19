import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or start == door:
        return get_locations()
    else:
        return monster, door, start

def move_player(player, move):
    # Get the player's current location
    x, y = player[0], player[1]

    if move == 'LEFT' and y != 0:
        y -= 1
    elif move == 'RIGHT' and y != 2:
        y += 1
    elif move == 'UP' and x != 0:
        x -= 1
    elif move == 'DOWN' and x != 2:
        x += 1

    return x, y

def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player[0], player[1]
    
    if y == 0:
        MOVES.remove('LEFT')
    elif x == 0:
        MOVES.remove('UP')
    elif y == 2:
        MOVES.remove('RIGHT')
    elif x == 2:
        MOVES.remove('DOWN')
    return MOVES
    
player = get_locations()[2]
door = get_locations()[1]
monster = get_locations()[0]

while True:
    print("Welcome to the dungeon!")
    # fill in with player position
    print("You're currently in room {}".format(player))
    
    # fill in with available moves
    openmove = get_moves(player)
    print("You can move {}".format(openmove))  
    
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    player = move_player(player, move) 

    if player == door:
        print ("you win!")
        break
    if player == monster:
        print ("You lose!")
        break

    # If it's a good move, change the player's position
    # If it's a bad move, don't change anything
    # If the new player position is the door, they win!
    # If the new player position is the monster, they lose!
    # Otherwise, continue
