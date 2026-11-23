import numpy as np

def pairwise_cosine_similarity(X):
    X_arr = np.array(X)
    rows, cols = X_arr.shape
    cos_sim_mat = np.zeros((rows, rows))
    for row in range(rows):
        for col in range(rows):
            a_norm = np.sqrt(X_arr[row,:] @ X_arr[row,:])
            b_norm = np.sqrt(X_arr.T[:,col] @ X_arr.T[:,col])
            if a_norm == 0 or b_norm == 0: 
                cos_sim_mat[row, col] = 0
            else:
                cos_sim_mat[row, col] = X_arr[row,:] @ X_arr.T[:,col] / (a_norm * b_norm)
    return np.round(cos_sim_mat, 4).tolist()