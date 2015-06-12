# Minimum Cost Path

import numpy as np

# defines the matrix
ROWS = 5
COLS = 5
mat_shape = (ROWS, COLS)

matrix = np.random.random_integers(0, 20, (5,5))

def get_min_cost_path (matrix, dest_col, dest_row):
    cost_matrix = np.zeros((5, 5))
    cost_matrix[0, 0] = matrix[0, 0]
    
    for row in range(0, ROWS):
        for col in range (0, COLS):
            # ignore the top left
            if (not (row == 0 and col == 0)):
                # if top row
                if (row == 0):
                    cost_matrix[row][col] = cost_matrix[row][col-1] + matrix[row][col]
                elif (col == 0):
                    cost_matrix[row][col] = cost_matrix[row-1][col] + matrix[row][col]
                else:
                    cost_matrix[row][col] = min(cost_matrix[row-1][col] + matrix[row][col],
                                                cost_matrix[row][col-1] + matrix[row][col],
                                                cost_matrix[row-1][col-1] + matrix[row][col])
            
    # we could've early returned, but let's ignore that                                           
    return cost_matrix[dest_row][dest_col]

print get_min_cost_path(matrix, 3, 3)
    