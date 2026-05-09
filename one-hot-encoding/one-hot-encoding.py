import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    Requirements
    Return NumPy array, shape (N, K), dtype float
    Rows sum to 1 (exactly one 1 per row)
    Vectorized index assignment (no Python loops)
    Validate that all labels < num_classes
    Stable for num_classes > max(y)+1 (extra zero columns)
    Constraints
    N ≥ 1, K ≥ 1
    NumPy only; time limit: 300ms
    """
    # Ensure y is a 1D NumPy array of integers
    y_arr = np.asarray(y, dtype=np.int_)
    N = y_arr.size
    
    # Infer num_classes (K) if not provided
    if num_classes is None:
        num_classes = np.max(y_arr) + 1
        
    K = num_classes
        
    # Validate labels
    if np.any(y_arr >= K) or np.any(y_arr < 0):
        raise ValueError("All labels must be >= 0 and < num_classes.")
        
    # Initialize the zero matrix of shape (N, K) with float dtype
    one_hot_matrix = np.zeros((N, K), dtype=float)
    
    # Vectorized assignment: Place a 1.0 at the row index and the label's column index
    one_hot_matrix[np.arange(N), y_arr] = 1.0
    
    return one_hot_matrix