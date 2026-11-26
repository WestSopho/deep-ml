import numpy as np


def determinant_4x4(matrix: list[list[int|float]]) -> float:
    # Return the determinant as float
    if np.array(matrix).shape == (2,2):
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    determinant = 0
    for col in range(len(matrix[0])):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        determinant += (-1)**col * matrix[0][col] * determinant_4x4(minor)
    return determinant 