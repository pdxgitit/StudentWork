import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)
    if monster == door or door == start or start == monster:
        return get_locations()
    else:
        return (monster, door, start)


# def move_player(player, move):
#     if move.lower() == "left":
#         player = (player[0], player [1]-1)
#     elif move.lower() == "right":
#         player = (player[0], player[1]+1)
#     elif move.lower() == "up":
#         player = (player[0]-1, player[1])
#     elif move.lower() == "down":
#         player = (player[0]+1, player[1])
#     return(player)


#Check logic
def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[0] == 0 and player[1] == 0:
        MOVES = ['RIGHT', 'DOWN']
    elif player[0] == 0 and player[1] == 2:
        MOVES = ['RIGHT','DOWN']
    elif player[0] == 0:
        MOVES = ['LEFT', 'RIGHT', 'DOWN']
    elif player[0] == 2 and player[1]== 2:
        MOVES = ['LEFT','UP']
    elif player[1] == 2:
        MOVES = ['LEFT','UP', 'DOWN']
    elif player[0] == 2 and [1] == 0:
        MOVES = ['RIGHT', 'UP']
    elif player[0]==1 and player[1]==1:
        MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    elif player[0] == 2:
        MOVES = ['LEFT', 'RIGHT', 'UP']
    elif player[0]==1:
        MOVES = ['RIGHT', 'UP', 'DOWN']

    return MOVES
print(get_moves((1,1)))



while True:
  print("Welcome to the dungeon!")
  print("You're currently in room {player}")
  print("You can move {MOVES}")
  print("Enter QUIT to quit")

  move = (input("> "))
  move = move.upper()

  if move == 'QUIT':
    break

  # If it's a good move, change the player's position
  # If it's a bad move, don't change anything
  # If the new player position is the door, they win!
  # If the new player position is the monster, they lose!
  # Otherwise, continue
