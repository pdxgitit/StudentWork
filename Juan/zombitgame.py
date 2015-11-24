# Welcome to Zombit, a game where you try to infect all the rabbits
# Those damn rabbits are irrationally resistant to becoming zombies
# Don't worry, we named the main function "simulate", so no actual
# rabbits were harmed in the making of this function
import random

# some variables to hold drawing peices
r_peices = {
    "strong" : " 0 ",
    "weak" : " o ",
    "infected" : " z ",
    "patient-z" : " Z "
}
t_b_tile = "==="
s_tile = "||"

# function to determine the strength of your virus
def ranstrength():
    return random.randint(0, 10000)

# function to create an unsuspecting population of rabbits
def createpopulation():
    columns = range(random.randint(2, 20))
    rows = range(random.randint(2, 20))
    print(columns)
    print(rows)
    rabbits = []
    for w in columns:
        rabbits.append([])
        for l in rows:
             rabbits[w].append(random.randint(0, 10000))
    return rabbits

# function to visualize the current state of your rabbit population

# function to simulate the spread of your disease
def simulate(population, x, y, strength):
    # convert starting position to a two-integer list for ease of use
    strt = [y, x]

    # check size of population array and store for use in coordinate validation
    x_max = len(population) - 1
    y_max = len(population[0]) - 1

    # function to validate coordinates
    def validate(coords):
        above = coords[0] < 0
        right = coords[1] < 0
        below = coords[0] > x_max
        left = coords[1] > y_max
        if left or right or above or below:
            return False
        return True

    # spread function - recursively modify outward from one cell
        # only returns when stopped on all sides at all base cases
    def spread(cell_coord, popl):

        # define all directional coordinate changes
        left = [cell_coord[0], cell_coord[1] - 1]
        right = [cell_coord[0], cell_coord[1] + 1]
        up = [cell_coord[0] - 1, cell_coord[1]]
        down = [cell_coord[0] + 1, cell_coord[1]]
        dirs = [up, down, left, right]

        # retreive and store current cell value
        cell_val = popl[cell_coord[0]][cell_coord[1]]

        # check if cell value is greater than strength
            # end this branch if so
        if cell_val > strength:
            return popl

        # check if cell value is already sub zero
            # end this branch if so
        if cell_val < 0:
            return popl

        # modify current cell value
        popl[cell_coord[0]][cell_coord[1]] = -1

        # call spread() for each valid direction move
        for i in dirs:
            if validate(i):
                popl = spread(i, popl)

        return popl

    # begin the spread
    population = spread(strt, population)

    # return a modified population array
    return population
