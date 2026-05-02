import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Compute the Mean Squared Error between predictions and targets.
    Requirements
    Convert inputs to NumPy arrays
    Ensure shapes match (return None if mismatch)
    Return a single float
    NumPy only, no sklearn
    Constraints
    1 ≤ N ≤ 10,000
    NumPy only
    Time limit: 200ms
    Returns: float MSE
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    if(y_pred.shape != y_true.shape):
        return None

    mse = np.mean((y_pred - y_true)**2)
    return float(mse)

'''
def mean_squared_error(y_pred, y_true):
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    
    if y_pred.shape != y_true.shape: # Kiểm tra khớp toàn bộ hình dạng
        return None
    
    count = y_pred.size # Dùng .size để lấy tổng số phần tử
    total_sum = 0
    
    for i in range(count):
        # Truy cập bằng flat index để an toàn cho cả mảng nhiều chiều
        error = (y_pred.flat[i] - y_true.flat[i])**2
        total_sum += error 
        
    return float(total_sum / count)
'''