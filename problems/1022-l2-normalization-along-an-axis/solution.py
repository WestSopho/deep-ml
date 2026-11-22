import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    # keepdims is true since we want to choose any axis. 
    # For instance, if we do not use keepdims and the axis is 1 (columns)
    # the denominator is treated as a row, not as a column as
    # it should be
    denominator = np.sqrt(np.sum(x**2, axis=axis, keepdims=True) + eps)
    return (x / denominator).tolist()
