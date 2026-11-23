import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # Convert a to a numpy array. If the elements are not the same, 
    # we return an empty array. Otherwise, we reshape it with
    # new_shape, and return it back as a Python list. 
    a_arr = np.array(a)
    if np.prod(a_arr.shape) != np.prod(new_shape):
        return []
    return a_arr.reshape(new_shape).tolist()