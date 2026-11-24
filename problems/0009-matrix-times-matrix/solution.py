import numpy as np


def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    # Return AB as a Python list; A's cols must be equal to B's rows
    a_mat = np.array(a)
    b_mat = np.array(b)
    if a_mat.shape[1] != b_mat.shape[0]: 
        return -1
    return (a_mat @ b_mat).tolist()