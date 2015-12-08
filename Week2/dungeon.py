<<<<<<< HEAD
=======


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
# def move_player(player, move):
#   # Get the player's current location
#     player = start
#
#   # If move is LEFT, y - 1
#   # If move is RIGHT, y + 1
#   # If move is UP, x - 1
#   # If move is DOWN, x + 1
#     return player

    ######################
>>>>>>> daa7a17f5a0b89125da865f60f7bacf08d7a8c3e
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

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> daa7a17f5a0b89125da865f60f7bacf08d7a8c3e
###########
#
# def get_locations():
#     monster = random.choice(CELLS)
<<<<<<< HEAD
#     door = random.choice(CELLS)
=======
#     door = ra.ndom.choice(CELLS)
>>>>>>> daa7a17f5a0b89125da865f60f7bacf08d7a8c3e
#     start = random.choice(CELLS)
#     if monster == start or monster == door or door == start:
#         return get_locations()
#     else:
#         return monster, door, start

<<<<<<< HEAD
def move_player(player, move):
  # Get the player's current location
    player = start

  # If move is LEFT, y - 1
  # If move is RIGHT, y + 1
  # If move is UP, x - 1
  # If move is DOWN, x + 1
    return player

    ######################
    #
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
=======
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



=======
def move_player(player, move):

    if move == "LEFT":
        player = (player[0], player[1] -1)
    elif move == "RIGHT":
        player = (player[0], player[1] +1)
    elif move == "UP":
        player = (player[0] -1, player[1])
    elif move == "DOWN":
        player = (player[0] +1, player[1])
    return player

>>>>>>> master

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]
#
def get_moves(player):
    x, y = player
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if y <= 0:
        MOVES.remove("LEFT")
    if x <=  0:
        MOVES.remove("UP")
    if y >= 2:
        MOVES.remove("RIGHT")
    if x >= 2:
        MOVES.remove("DOWN")

    return MOVES
##############################
# player = get_locations()[2]
# moving = get_moves(player)
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]
#
# move = input("> ")
# move = move.upper()


monster, door, player = get_locations()
while True:

    moves = get_moves(player)


    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player)) # fill in with player position
    print("You can move {}".format(moves))  # fill in with available moves
>>>>>>> daa7a17f5a0b89125da865f60f7bacf08d7a8c3e
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()
<<<<<<< HEAD

    if move == 'QUIT':
        break
=======
    player = move_player(player, move)

    print(monster, door, player)
    if move == 'QUIT':
        break

    elif player == door:
        print("You WIN!!")
        break

    elif player == monster:
        print("The Monster ate you.  You LOSE!!")
        break
>>>>>>> daa7a17f5a0b89125da865f60f7bacf08d7a8c3e
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
