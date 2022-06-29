import numpy as np
from math import copysign, hypot

def _givens_rotation_matrix_entries(a, b):
    """Compute matrix entries for Givens rotation."""
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)


def givens_rotation(A):

    (num_rows, num_cols) = np.shape(A)

    # Initialize orthogonal matrix Q and upper triangular matrix R.
    Q = np.identity(num_rows)
    R = np.copy(A)

    # Iterate over lower triangular matrix.
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    
    for (row, col) in zip(rows, cols):

        # Compute Givens rotation matrix and
        # zero-out lower triangular matrix entries.
        if R[row, col] != 0:
            (c, s) = _givens_rotation_matrix_entries(R[col, col], R[row, col])

            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
            print("---------------------")
            print("---------GGGGG---------")
            print(G)
            print("---------Ai------------")
            print(R)
	
    return (Q, R)



# Set print options (optional)
np.set_printoptions(precision=4, suppress=True)

# Input matrix
A = np.array([[1,1,1],[3,-1,-1],[2,-3,1]], dtype=float)
b = np.array([37,3,13], dtype=float)
    
# Print input matrix
#print(A)

# Compute QR decomposition using Givens rotation
(Q, R) = givens_rotation(A)
print(" \nsolve \n")
print("-----------------------------------")
# Print orthogonal matrix Q
print(" Q :\n")
print(Q)

print("-----------------------------------")
# Print upper triangular matrix R
print(" R :\n")
print(R)