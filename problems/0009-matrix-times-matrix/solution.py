import numpy as np


def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    # Convert lists to numpy arrays.
    # Check that the cols of a and rows of b are the same.
    # Compute the matrix computation. 
    # Return the result as a Python list.
    a_mat = np.array(a)
    b_mat = np.array(b)
    if a_mat.shape[1] != b_mat.shape[0]: 
        return -1
    return (a_mat @ b_mat).tolist()