import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    Requirements
    Must work for lists or NumPy arrays
    Must return a float
    Must be vectorized (no Python element loops)
    Constraints
    Time limit: 200 ms, Memory: 64 MB
    NumPy only (no sklearn, scipy)

    """
    x_array = np.asarray(x)
    y_array = np.asarray(y)
    return float(np.sum(np.abs(x_array - y_array)))