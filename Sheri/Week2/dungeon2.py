import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)
    if monster == door or door == player or player == monster:
        return get_locations()
    else:
        return (monster, door, player)

def move_player(player, move):
    if move.lower() == "left":
        player = (player[0], player [1]-1)
    elif move.lower() == "right":
        player = (player[0], player[1]+1)
    elif move.lower() == "up":
        player = (player[0]-1, player[1])
    elif move.lower() == "down":
        player = (player[0]+1, player[1])
    return(player)

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] == 0:
        moves.remove("LEFT")
    if player[1]== 2:
        moves.remove("RIGHT")
    if player[0] == 0:
        moves.remove("UP")
    if player[0] == 2:
        moves.remove("DOWN")
    return moves

monster, door, player = get_locations()

while True:
    print("Welcome to the dungeon!")
    print("You're currently in room", player)
    print("You can move", get_moves(player))
    print("Enter QUIT to quit")

    move = input("Which way would you like to move? ")

    move = move.upper()
    if move == 'QUIT':
        break
    elif move in get_moves(player):
        player = move_player(player, move)
    else:
        print("enter valid input")

    if monster == player:
        print("Monster! Game Over!!")
        break
    if door == player:
        print("You found the door! You win!!!")
        break



  # If it's a good move, change the player's position
  # If it's a bad move, don't change anything
  # If the new player position is the door, they win!
  # If the new player position is the monster, they lose!
  # Otherwise, continue
