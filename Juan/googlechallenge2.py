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
    def get_neighbors(a, b, popl):
        """
        returns the value of each uninfected cell neighboring
        a = patient x coord
        b = patient y coord
        popl = current population
        """
        up, down = popl[a - 1][b], popl[a + 1][b]
        right, left = popl[a][b + 1], popl[a][b - 1]
