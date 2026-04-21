import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    Requirements
    Must work for lists or NumPy arrays
    Must return a float
    Must be vectorized (no Python element loops)
    Must handle 1D arrays only
    Must raise ValueError for mismatched lengths
    """
    if len(x) != len(y):
        raise ValueError 
    x_array = np.asarray(x)
    y_array = np.asarray(y)
    dot_product = np.dot(x_array, y_array)
    return float(dot_product)