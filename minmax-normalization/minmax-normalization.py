import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    Requirements
    Accept 1D or 2D NumPy arrays
    Vectorized; no Python loops
    Avoid divide-by-zero when max==min (use eps)
    Return np.ndarray (float)
    Constraints
    Up to 10⁶ elements
    NumPy only
    """
    # Convert input to a float numpy array 
    X_arr = np.asarray(X, dtype=float)
    
    # Calculate min and max along the specified axis. 
    # keepdims=True is crucial: it maintains the dimensions so NumPy 
    # knows how to broadcast the arithmetic across rows or columns.
    X_min = np.min(X_arr, axis=axis, keepdims=True)
    X_max = np.max(X_arr, axis=axis, keepdims=True)
    
    # Calculate the range (denominator)
    X_range = X_max - X_min
    
    # Prevent division by zero where max == min by substituting with eps
    X_range = np.where(X_range == 0, eps, X_range)
    
    # Apply the Min-Max scaling formula
    X_scaled = (X_arr - X_min) / X_range
    
    return X_scaled