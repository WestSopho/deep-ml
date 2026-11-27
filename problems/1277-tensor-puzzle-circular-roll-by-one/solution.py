import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    n = a.shape[0]
    out = np.zeros(n)
    for i in np.arange(n):
        out[i] = a[(i + 1) % n]
    return out