import numpy as np


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    # We convert the Python lists into numpy arrays. 
    # If a's cols and b's rows are not the same, the operation is not valid.
    # Compute the dot product between a and b; convert to a Python list. 
    a_mat = np.array(a)
    b_vec = np.array(b)
    if a_mat.shape[1] != b_vec.shape[0]: 
        return -1
    return (a_mat @ b_vec).tolist()
    