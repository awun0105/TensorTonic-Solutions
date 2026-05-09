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
    if y_pred.shape != y_true.shape:
        return None

    mse = np.mean((y_pred - y_true) ** 2)
    return float(mse)


"""
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
"""
# Root mean squared error (RMSE)
'''
import numpy as np

def root_mean_squared_error(y_true, y_pred):
    """
    Description: Tính Sai số căn phương trung bình (RMSE).
    Formula: sqrt( mean( (y_true - y_pred)^2 ) )
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape:
        return None

    # Tính MSE trước, sau đó lấy căn bậc hai toàn cục
    mse = np.mean((y_true - y_pred) ** 2)
    rmse = np.sqrt(mse)

    return float(rmse)
'''
# Mean squared log error
'''
import numpy as np

def mean_squared_log_error(y_true, y_pred):
    """
    Description: Tính Sai số bình phương log trung bình (MSLE).
    Requirements: y_true và y_pred không được chứa giá trị âm.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape:
        return None

    # Kiểm tra điều kiện giá trị không âm (tránh lỗi log)
    if np.any(y_true < 0) or np.any(y_pred < 0):
        # Thông thường MSLE không xác định cho số âm
        return None

    # Tính log(1 + y) cho cả hai mảng
    log_true = np.log1p(y_true) # np.log1p(x) tương đương np.log(1 + x) nhưng chính xác hơn
    log_pred = np.log1p(y_pred)

    # Tính MSE trên các giá trị đã log
    msle = np.mean((log_true - log_pred) ** 2)

    return float(msle)
'''
