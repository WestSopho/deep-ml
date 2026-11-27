import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    first = np.ones(a.shape[0])
    second = np.arange(2).reshape(-1, 1)
    mask = first * second
    return (1 - mask) * a + mask * b
