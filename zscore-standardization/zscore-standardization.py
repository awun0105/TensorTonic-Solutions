import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/(std+eps). If 2D and axis=0, per column.
    Return np.ndarray (float).
    Requirements
    Handle 1D and 2D arrays
    Vectorized; avoid divide-by-zero (use eps)
    Return np.ndarray (float)
    Constraints
    Up to 10⁶ elements
    NumPy only
    """
    X_arr = np.asarray(X, dtype=float)
    
    # Xử lý axis cho mảng 1D hoặc 2D
    actual_axis = 0 if X_arr.ndim == 1 else axis
    
    mean = np.mean(X_arr, axis=actual_axis, keepdims=True)
    std = np.std(X_arr, axis=actual_axis, keepdims=True)
    
    # Thay vì np.where, hãy cộng trực tiếp eps vào std theo đúng ý đồ của test case
    X_standardized = (X_arr - mean) / (std + eps)
    
    return X_standardized