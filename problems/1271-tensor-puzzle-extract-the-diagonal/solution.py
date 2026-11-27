import numpy as np


def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    indexes = np.arange(A.shape[0])
    return A[indexes, indexes]
