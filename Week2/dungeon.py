import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)
    #print(monster, door, start)

    if monster == door or monster == start or door == start:
        return get_locations()
    else:
        return monster, door, start
#print (get_locations())

###########
#
# def get_locations():
#     monster = random.choice(CELLS)
#     door = ra.ndom.choice(CELLS)
#     start = random.choice(CELLS)
#     if monster == start or monster == door or door == start:
#         return get_locations()
#     else:
#         return monster, door, start

# def move_player(player, move):
#   # Get the player's current location
#     player = start
#
#   # If move is LEFT, y - 1
#   # If move is RIGHT, y + 1
#   # If move is UP, x - 1
#   # If move is DOWN, x + 1
#     return player
#
#     ######################

def move_player(player, move):
    player = start
    if move == "LEFT":
        player = (player[0], player[1]-1)
    elif move == "RIGHT":
        player = (player[0], player[1]+1)
    elif move == "UP":
        player = (player[0]-1, player[1])
    elif move == "DOWN":
        player = (player[0] =1, player[1])
    return player




def get_moves(player):

    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] == 0:
        MOVE.remove("LEFT")
    if player[0] ==  0:
        MOVE.remove("UP")
    if player[1] == 2:
        MOVE.remove("RIGHT")
    if player[0] == 2:
        MOVE.remove("DOWN")

    return MOVES


    # def get_moves(player):
    #   MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    #   if player[1] == 0:
    #       MOVES.remove('LEFT')
    #   if player[0] == 0:
    #       MOVES.remove('UP')
    #   if player[1] == 2:
    #       MOVES.remove('RIGHT')
    #   if player[0] == 2:
    #       MOVES.remove('DOWN')
    #   return MOVES
##################
# def move_player(player, move):
#     player = start
#     if move == "LEFT":
#         player = (player[0] -1, player[1])
#     elif move == "RIGHT":
#         player = (player[0] +1, player[1])
#     elif move == "UP":
#         player = (player[0], player[1] +1)
#     elif move == "DOWN":
#         player = (player[0], player[1] -1)
#     return player

##############################
player = get_locations()
moving = get_moves(player)
while True:
    # start = get_locations()[2]
    # move = get_moves(player)

    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(start)) # fill in with player position
    print("You can move {}".format(move))  # fill in with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
##################################
# player = get_locations()
# moving = get_moves(player)
#
# while True:
#   print("Welcome to the dungeon!")
#   print("You're currently in room {}".format(player[2]))  # fill in with player position
#   print("You can move {}".format(moving))  # fill in with available moves
#   print("Enter QUIT to quit")
#
#   move = input("> ")
#   move = move.upper()
#
#   if move == 'QUIT':
#     break
  # If it's a good move, change the player's position
  # If it's a bad move, don't change anything
  # If the new player position is the door, they win!
  # If the new player position is the monster, they lose!
  # Otherwise, continue
