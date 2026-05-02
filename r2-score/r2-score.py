import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    Requirements
    Inputs: equal-length 1D arrays (NumPy arrays or lists convertible to arrays)
    Vectorized (no Python loops)
    Handle the constant-target edge case:
    If all y_true are equal: return 1.0 if y_pred == y_true elementwise,
    else return 0.0
    Return a Python float
    Constraints
    n ≤ 10⁶
    NumPy only
    """
    # Chuyển đổi input sang NumPy array
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # Kiểm tra hình dạng (tương tự yêu cầu bài MSE)
    if y_true.shape != y_pred.shape:
        return None

    # Tính SS_res (Tổng bình phương sai số dư)
    ss_res = np.sum((y_true - y_pred) ** 2)
    
    # Tính SS_tot (Tổng bình phương tổng thể)
    y_mean = np.mean(y_true)
    ss_tot = np.sum((y_true - y_mean) ** 2)
    
    # Xử lý Edge Case: Nếu tất cả y_true bằng nhau (ss_tot == 0)
    if ss_tot == 0:
        # Trả về 1.0 nếu dự đoán khớp hoàn toàn, ngược lại 0.0
        return 1.0 if np.array_equal(y_true, y_pred) else 0.0
    
    # Tính toán công thức R2 Score
    r2 = 1 - (ss_res / ss_tot)
    
    return float(r2)

    
    
