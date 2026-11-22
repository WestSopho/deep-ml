import numpy as np

def cross_product(a, b):
    # Use the formula for the cross product directly
    a_vec = np.array(a)
    b_vec = np.array(b)
    return np.array([
        a_vec[1]*b_vec[2] - a_vec[2]*b_vec[1], 
        a_vec[2]*b_vec[0] - a_vec[0]*b_vec[2], 
        a_vec[0]*b_vec[1] - a_vec[1]*b_vec[0]])