import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    a_arr = np.array(a)
    if np.prod(a_arr.shape) != np.prod(np.array(new_shape)): 
        return []
    reshaped_matrix = np.array(a).reshape(new_shape).tolist()
    return reshaped_matrix