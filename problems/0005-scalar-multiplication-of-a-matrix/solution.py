import numpy as np


def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Multiply the matrix by the scalar straightforwardly; 
    # the scalar is broadcasted to a matrix with the same size
    return np.array(matrix) * scalar