import numpy as np


def classification_metrics(y_true, y_pred, pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Return dict with float values.
    """
    TP = sum((t == pos_label and p == pos_label) for t, p in zip(y_true, y_pred))
    FP = sum((t == pos_label and p != pos_label) for t, p in zip(y_true, y_pred))
    TN = sum((t != pos_label and p != pos_label) for t, p in zip(y_true, y_pred))
    FN = sum((t == pos_label and p != pos_label) for t, p in zip(y_true, y_pred))
    epsilon = 1e-7
    accuracy = (TP + TN) / (TP + FP + TN + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = (2 * precision * recall) / (precision + recall + epsilon)
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1_score": float(f1),
    }


# numpy


def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' (currently implemented for binary logic).
    Return dict with float values.
    """
    # 1. Ép kiểu về numpy array (tối ưu bộ nhớ với asarray)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Kiểm tra lỗi độ dài mảng
    if y_true.shape != y_pred.shape:
        raise ValueError("Độ dài của y_true và y_pred phải bằng nhau.")

    # 2. Tính toán các thành phần cơ bản (TP, FP, FN, TN)
    # TP: True Positive, FP: False Positive, FN: False Negative, TN: True Negative
    TP = np.sum((y_true == pos_label) & (y_pred == pos_label))
    FP = np.sum((y_true != pos_label) & (y_pred == pos_label))
    FN = np.sum((y_true == pos_label) & (y_pred != pos_label))
    TN = np.sum((y_true != pos_label) & (y_pred != pos_label))

    # 3. Tính toán các chỉ số
    # Thêm một số cực nhỏ (epsilon) để tránh lỗi chia cho 0
    epsilon = 1e-7

    # Accuracy: Tỷ lệ dự đoán đúng trên tổng số mẫu
    accuracy = np.mean(y_true == y_pred)

    # Precision: Trong những ca dự đoán là Positive, bao nhiêu ca đúng?
    precision = TP / (TP + FP + epsilon)

    # Recall: Trong những ca thực tế là Positive, tìm ra được bao nhiêu ca?
    recall = TP / (TP + FN + epsilon)

    # F1-score: Trung bình điều hòa giữa Precision và Recall
    f1 = 2 * (precision * recall) / (precision + recall + epsilon)

    # 4. Trả về kết quả dưới dạng dictionary
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
    }


# --- Ví dụ sử dụng ---
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 1, 1, 0, 0]

results = classification_metrics(y_true, y_pred, pos_label=1)
print(results)
