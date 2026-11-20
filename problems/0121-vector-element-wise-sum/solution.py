import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    # We convert a, b to np arrays. If the shape doesn't match, return -1. Otherwise, add them element-wisely, and return the result as a Python list. 
    a_np = np.array(a)
    b_np = np.array(b)
    if a_np.shape != b_np.shape:
        return -1
    return (a_np + b_np).tolist()