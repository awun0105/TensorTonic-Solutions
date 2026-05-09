def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    Requirements
    Handle up to 10⁵ items
    Integer labels assumed to be in 0..K-1 (K inferred from data)
    Return a Python float (not NumPy scalar)
    Constraints
    len(y_true) == len(y_pred)
    No external ML libraries allowed.
    """
    if not y_true:
        return 0.0
    
    n = len(y_true)
    true_positives = 0
    
    # Iterate once through the data: O(N) complexity
    for i in range(n):
        if y_true[i] == y_pred[i]:
            true_positives += 1
            
    # Micro F1 = (2 * TP) / (2 * TP + FP + FN)
    # In multi-class: FP + FN = 2 * (Total Samples - TP)
    # Result simplifies to: TP / Total Samples
    return float(true_positives / n)