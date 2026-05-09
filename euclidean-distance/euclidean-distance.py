import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    Requirements
    Must work for lists or NumPy arrays
    Must return a float
    Must be vectorized (no Python element loops)
    Constraints
    Time limit: 200 ms, Memory: 64 MB
    NumPy only (no sklearn, scipy)
    """
   # asarray avoids copying if x or y are already numpy arrays
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Standard vectorized L2 norm calculation
    # return float(np.linalg.norm(x - y))
    return float(np.sqrt(np.sum((x - y) ** 2)))