import numpy as np


def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Return the array multiplied by an scalar element-wisely; 
    # tolist() returns the numpy array as a Python array.
    return (np.array(matrix) * scalar).tolist()