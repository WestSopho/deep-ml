import numpy as np


def heaviside(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    # Return heavyside step with zero-value as float64 array
    out = np.zeros(a.shape)
    where_equal = np.nonzero(a == 0)[0]
    where_great = np.nonzero(a > 0)[0]
    out[where_equal] = b[where_equal]
    out[where_great] = 1
    return out