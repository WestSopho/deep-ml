import numpy as np


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return the dot product between a matrix and vector; a_mat cols 
    # and b_vec rows must be the same
    a_mat = np.array(a)
    b_vec = np.array(b)
    if a_mat.shape[1] != b_vec.shape[0]:
        return -1
    return (a_mat @ b_vec).tolist()