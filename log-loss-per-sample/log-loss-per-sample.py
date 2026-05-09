import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    Requirements
    Clip predicted probabilities to the range [epsilon, 1 - epsilon]
    Compute the loss independently for each sample
    Return a list of loss values preserving the original sample order
    Use natural logarithm (base e)
    Constraints
    1 <= len(y_true) == len(y_pred) <= 10000
    y_true[i] is 0 or 1
    0.0 <= y_pred[i] <= 1.0
    eps = 1e-15
    Time limit: 300 ms
    """
    losses = []
    
    for i in range(len(y_true)):
        y = y_true[i]
        p = y_pred[i]
        
        # Clip predicted probabilities to [eps, 1 - eps]
        p = max(eps, min(1 - eps, p))
        
        # Compute loss: - (y * log(p) + (1 - y) * log(1 - p))
        # Since y is always 0 or 1, we can simplify the logic:
        if y == 1:
            loss = -math.log(p)
        else:
            loss = -math.log(1 - p)
            
        losses.append(loss)
        
    return losses