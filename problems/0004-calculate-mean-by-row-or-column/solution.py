import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    mat = np.array(matrix)
    if mode == "row": 
        return mat.mean(axis=1).tolist()
    return mat.mean(axis=0).tolist()