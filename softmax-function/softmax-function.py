import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    Requirements
    Must handle both 1D and 2D NumPy arrays
    Should be vectorized (no loops)
    Must be numerically stable (subtract max before exponentiation)
    Output probabilities must sum to 1 per vector (or per row for 2D)
    Constraints
    Input size ≤ 10⁶ elements
    Only NumPy allowed
    """
    # Convert to array without copying if it's already an ndarray
    x = np.asarray(x)
    
    # 1. Shift values for numerical stability (subtract max)
    # axis=-1 operates on the last dimension (the vector itself, or rows in 2D)
    # keepdims=True ensures the shape aligns for broadcasting:
    #   - 1D: shape (D,) -> max shape (1,)
    #   - 2D: shape (N, D) -> max shape (N, 1)
    x_max = np.max(x, axis=-1, keepdims=True)
    
    # 2. Exponentiate the shifted values
    exp_x = np.exp(x - x_max)
    
    # 3. Compute the sum of exponentials and divide
    # keepdims=True again ensures we can divide (N, D) by (N, 1)
    sum_exp_x = np.sum(exp_x, axis=-1, keepdims=True)
    
    return exp_x / sum_exp_x