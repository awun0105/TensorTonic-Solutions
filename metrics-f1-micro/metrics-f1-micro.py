import numpy as np 
'''
Để tính F1-Micro, chúng ta cần hiểu bản chất của nó: Trong phương pháp "Micro-average", người ta sẽ cộng dồn tất cả các đại lượng True Positives ($TP$), False Positives ($FP$), và False Negatives ($FN$) của tất cả các lớp lại trước, sau đó mới tính $F1$.Tuy nhiên, có một bí mật toán học cực kỳ thú vị: Đối với bài toán Multi-class mà mỗi mẫu chỉ thuộc về một lớp duy nhất, thì $F1$-Micro chính bằng Accuracy (độ chính xác tổng thể).Giải thích tại sao:Bất kỳ khi nào bạn dự đoán sai một mẫu: Bạn vừa tạo ra 1 $FN$ (cho lớp đúng) và vừa tạo ra 1 $FP$ (cho lớp sai).Do đó, tổng $TP$ chính là số lượng mẫu dự đoán đúng.Tổng $FP$ luôn bằng tổng $FN$.Khi $FP = FN$, thì $Precision = Recall = F1 = Accuracy$.
'''
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