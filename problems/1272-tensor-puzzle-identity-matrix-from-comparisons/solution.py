import numpy as np


def eye(n: int) -> np.ndarray:
    # Return the comparison boolean matrix as a float matrix
    row = np.arange(n)
    col = np.arange(n).reshape(-1, 1)
    return (row == col).astype(np.float64)