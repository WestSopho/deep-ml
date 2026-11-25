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
    # Return A^{-1} as a lists of lists, or -1 if A has determinant 0
    mat = np.array(matrix)
    det = mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0]
    if np.isclose(det, 0):
        return None
    adjugate = np.array([[mat[1,1], -mat[0,1]], [-mat[1,0], mat[0,0]]])
    return (1 / det * adjugate).tolist()