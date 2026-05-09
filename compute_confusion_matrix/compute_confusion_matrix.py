def compute_confusion_matrix(y_true, y_pred):
    # Khởi tạo các biến đếm
    TP = TN = FP = FN = 0

    # Lặp qua từng cặp giá trị thực tế và dự đoán
    for true_val, pred_val in zip(y_true, y_pred):
        if true_val == 1 and pred_val == 1:
            TP += 1  # Mô hình dự đoán đúng lớp Positive (1)
        elif true_val == 0 and pred_val == 0:
            TN += 1  # Mô hình dự đoán đúng lớp Negative (0)
        elif true_val == 0 and pred_val == 1:
            FP += 1  # Thực tế là 0 nhưng mô hình đoán nhầm là 1
        elif true_val == 1 and pred_val == 0:
            FN += 1  # Thực tế là 1 nhưng mô hình đoán nhầm là 0

    return (TP, TN, FP, FN)


# Dữ liệu đầu vào
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1]

# Chạy thử
ket_qua = compute_confusion_matrix(y_true, y_pred)
print("Kết quả (TP, TN, FP, FN) =", ket_qua)
# Đầu ra: Kết quả (TP, TN, FP, FN) = (3, 2, 0, 1)
