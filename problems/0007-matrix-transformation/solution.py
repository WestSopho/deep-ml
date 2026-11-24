import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    # Return T^{-1}AS as a Python list; T and S must be invertible
    a_mat = np.array(A)
    t_mat = np.array(T)
    s_mat = np.array(S)
    if np.isclose(np.linalg.det(t_mat), 0) or np.isclose(np.linalg.det(s_mat), 0):
        return -1
    return (np.linalg.inv(t_mat) @ a_mat) @ s_mat