import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)


    if monster == door or monster == start or door == start:
        return get_locations()
    else:
        return monster, door, start


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

monster, door, player = get_locations()
while True:

    moves = get_moves(player)

    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player)) # fill in with player position
    print("You can move {}".format(moves))  # fill in with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()
    player = move_player(player, move)

    print(monster, door, player)
    if move == 'QUIT':
        break

    elif player == door:
        print("You found the door; You Win!!")
        break

    elif player == monster:
        print("The Monster ate you. Sorry!!")
        break
