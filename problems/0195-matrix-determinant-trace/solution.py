import numpy as np


def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    # Return the determinant and trace as floats
    mat = np.array(matrix)
    return (np.linalg.det(matrix), np.float64(np.sum(np.diag(matrix))))
    