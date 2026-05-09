def pad_sequence(seq, max_len):
    # Nếu chuỗi dài hơn hoặc bằng max_len: Cắt bỏ phần thừa ở cuối
    if len(seq) >= max_len:
        return seq[:max_len]

    # Nếu chuỗi ngắn hơn max_len: Bổ sung số 0 vào cuối cho đủ chiều dài
    return seq + [0] * (max_len - len(seq))


# Chạy thử
seq = [15, 23, 4]
max_len = 5
print(pad_sequence(seq, max_len))
# Đầu ra: [15, 23, 4, 0, 0]
