import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    # Compute the mean along axis 1 if it is mode row, otherwise, along 0 
    # if it is mode column; axis removes the opposite axis to get the desired
    # axis. 
    mat = np.array(matrix)
    if mode == "row": 
        return mat.mean(axis=1).tolist()
    return mat.mean(axis=0).tolist()