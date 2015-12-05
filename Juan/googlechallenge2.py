# Test cases
# ==========
#
# Inputs:
#     (int) population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
#     (int) x = 0
#     (int) y = 0
#     (int) strength = 2
# Output:
#     (int) [[-1, -1, 3],
#            [-1, 3, 4],
#            [3, 2, 1]]
#
# Inputs:
#     (int) population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
#     (int) x = 2
#     (int) y = 1
#     (int) strength = 5
# Output:
#     (int) [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]

def answer(population, x, y, strength):
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
                spread(i, popl)

        return popl

    # begin the spread
    spread(strt, population)

    # return a modified population array
    return population

population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
x = 0
y = 0
strength = 2
print(answer(population, x, y, strength))
