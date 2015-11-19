import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    avail = CELLS
    monster = random.choice(avail)
    avail.remove(monster)
    door = random.choice(avail)
    avail.remove(door)
    start = random.choice(avail)
    avail.remove(start)
    return monster, door, start

def move_player(player, move):
    # If move is LEFT, y - 1
    if move == 'LEFT':
        player = (player[0], player[1] - 1)
    # If move is RIGHT, y + 1
    if move == 'RIGHT':
        player = (player[0], player[1] + 1)
    # If move is UP, x - 1
    if move == 'UP':
        player = (player[0] - 1, player[1])
    # If move is DOWN, x + 1
    if move == 'DOWN':
        player = (player[0] + 1, player[1])
    return player


def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # if player's y is 0, remove LEFT
    if player[1] == 0:
        MOVES.remove('LEFT')
    # if player's x is 0, remove UP
    if player[0] == 0:
        MOVES.remove('UP')
    # if player's y is 2, remove RIGHT
    if player[1] == 2:
        MOVES.remove('RIGHT')
    # if player's x is 2, remove DOWN
    if player[0] == 2:
        MOVES.remove('DOWN')
    return MOVES

peice_locs = get_locations()
player_loc = peice_locs[2]
monster_loc = peice_locs[0]
door_loc = peice_locs[1]
while True:
    val_moves = get_moves(player_loc)
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player_loc))  # fill in with player position
    print("You can move {}".format(val_moves))  # fill in with available moves
    print("Enter QUIT to quit")
    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    # If it's a good move, change the player's position
    if move in val_moves:
        player_loc = move_player(player_loc, move)
    # If it's a bad move, don't change anything
    # If the new player position is the door, they win!
    if player_loc == door_loc:
        print("You win!")
        break
    # If the new player position is the monster, they lose!
    if player_loc == monster_loc:
        print("You ran into the monster! You lose!")
        break
    # Otherwise, continue

def validate(a,b,c):
        try:
            datetime.date(a,b,c)
        except ValueError:
            return False
        return True
