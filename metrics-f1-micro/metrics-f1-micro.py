import numpy as np 

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
    # 1. Chuyển đổi sang NumPy array
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # 2. Kiểm tra tính tương thích
    if y_true.shape != y_pred.shape:
        raise ValueError("Shapes of y_true and y_pred must match.")
    
    # Nếu mảng rỗng, F1 thường được định nghĩa là 0.0 hoặc tùy quy ước
    if y_true.size == 0:
        return 0.0

    # 3. Tính toán Micro-F1 (Tương đương Accuracy)
    # Tổng True Positives trên tất cả các lớp chính là số lượng dự đoán đúng
    true_positives = np.sum(y_true == y_pred)
    
    # F1-micro = TP_total / (TP_total + 0.5 * (FP_total + FN_total))
    # Vì FP_total = FN_total = số lượng dự đoán sai
    # F1-micro = dự đoán đúng / tổng số mẫu
    f1_micro_val = true_positives / y_true.size
    
    # 4. Trả về kiểu Python float
    return float(f1_micro_val)

    # --- Kiểm chứng ---
if __name__ == "__main__":
    # Ví dụ với 3 lớp (0, 1, 2)
    y_t = [0, 1, 2, 0, 1, 2]
    y_p = [0, 2, 2, 0, 0, 1]
    
    print(f"F1 Micro: {f1_micro(y_t, y_p)}")