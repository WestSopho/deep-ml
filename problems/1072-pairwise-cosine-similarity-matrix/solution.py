import numpy as np

def pairwise_cosine_similarity(X):
    # We compute the pairwise cosine similarity matrix
    # (nxn) size. For each element (i, j), we compute
    # the dot product between a row of A and a column of A^T
    # (row of A), and divide them by its norm. If a row has 0 norm, 
    # the entry is 0. 
    x_arr = np.array(X)
    rows, _ = x_arr.shape
    cos_sim_mat = np.zeros((rows, rows))
    for row in range(rows):
        for col in range(rows):
            a_norm = np.sqrt(x_arr[row,:] @ x_arr[row,:])
            b_norm = np.sqrt(x_arr.T[:,col] @ x_arr.T[:,col])
            if a_norm == 0 or b_norm == 0:
                cos_sim_mat[row, col] = 0
            else:
                numerator = x_arr[row,:] @ x_arr.T[:,col]
                denominator = (a_norm * b_norm)
                cos_sim_mat[row, col] = numerator / denominator
    return np.round(cos_sim_mat, 4).tolist()