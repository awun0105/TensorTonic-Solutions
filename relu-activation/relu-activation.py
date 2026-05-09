import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    Requirements
    Return result using NumPy (not Python lists)
    Handle scalar, list, and NumPy array inputs
    Fully vectorized (no explicit Python loops)
    Preserve input shape
    Constraints
    Use NumPy only
    Time limit: 200ms; Memory ≤ 64MB
    """
    # Convert input to a numpy array to handle lists/scalars and ensure  vectorization
    x_arr = np.asanyarray(x)
    
    # Element-wise maximum between 0 and the input array
    return np.maximum(0, x_arr)
   