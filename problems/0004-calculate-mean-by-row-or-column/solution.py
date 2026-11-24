import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    # Return the mean across rows or cols depending on the mode
    mat = np.array(matrix)
    if mode == "row":
        return mat.mean(axis=1).tolist()
    return mat.mean(axis=0).tolist()