import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    Requirements
    Input: 1D NumPy arrays of equal length or vectors
    Output: scalar float
    Must be fully vectorized (no loops)
    Handle zero vectors gracefully (return 0 if either norm is 0)
    """
    a_array = np.asarray(a)
    b_array = np.asarray(b)
    if len(a_array) != len(b_array):
        raise ValueError
    norm_a = np.linalg.norm(a_array)
    norm_b = np.linalg.norm(b_array)
    if norm_a == 0 or norm_b == 0:
        return 0
    dot_product = np.dot(a_array, b_array)
    cosine_similarity = dot_product / (norm_a*norm_b)
    return float(cosine_similarity)
    