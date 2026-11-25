import numpy as np


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Return the inverse of the matrix A as a list of lists
    mat = np.array(matrix)
    determinant = np.linalg.det(mat)
    if np.isclose(determinant, 0): 
        return None
    return ((1 / determinant) * np.array([[mat[1,1], -mat[0,1]], [-mat[1,0], mat[0,0]]])).tolist()