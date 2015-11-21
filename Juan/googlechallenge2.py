# Test cases
# ==========
#
# Inputs:
#     (int) population = [[1, 2, 3],
#                         [2, 3, 4],
#                         [3, 2, 1]]
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
    #convert starting position to a two-integer list for ease of use
    strt = [x, y]

    #check the size of the population array and store it for use in coordinate validation
    x_max = len(population[0]) - 1
    y_max = len(population) - 1

    #function to validate coordinates
    def validate(coords):
        left = coords[0] < 0
        above = coords[1] < 0
        right = coords[0] > x_max
        below = coords[1] > y_max
        if left or right or above or below:
            return True
        return False


    #spread function - recursively modify outward from one cell
        #only returns when stopped on all sides at all base cases
    def spread(cell_coord):
        global population
        #define all directional coordinate changes
        up = [cell_coord[0], cell_coord[1] - 1]
        down = [cell_coord[0], cell_coord[1] + 1]
        left = [cell_coord[0] - 1, cell_coord[1]]
        right = [cell_coord[0] + 1, cell_coord[1]]

        #check if current coordinates are valid
            #return nothing if not
        if validate(cell_coord):
            return

        #retreive and store current cell value
        cell_val = population[cell_coord[0]][cell_coord[1]]

        #check if cell value is greater than strength
            #return nothing if so
        if cell_val > strength:
            return

        #check if cell value is already sub zero
            #return nothing if so
        if cell_val < 0:
            return

        #modify current cell value
        population[cell_coord[0]][cell_coord[1]] = -1

        #call spread() four times with Up Down Left Right coordinates
        spread(up)
        spread(down)
        spread(right)
        spread(left)

    #begin the spread
    spread(strt)

    #return a modified population array
    return population

population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
x = 2
y = 1
strength = 5
print(answer(population, x, y, strength))
