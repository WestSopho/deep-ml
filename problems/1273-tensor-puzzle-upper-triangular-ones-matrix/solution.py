import numpy as np

def triu_ones(n: int) -> np.ndarray:
    # Return the triangular matrix as float64
    first_index = np.arange(n).reshape(-1, 1)
    second_index = np.arange(n)
    mask = first_index <= second_index
    return mask.astype(float)
