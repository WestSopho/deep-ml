import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    # Return the 
    n = a.shape[0]
    return a[n - 1 - np.arange(n)]