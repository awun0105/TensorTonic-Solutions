def word_frequencies(text):
    """
    Hàm đếm tần suất các từ trong văn bản.
    """
    # 1. Chuyển về chữ thường để không phân biệt AI và ai
    text = text.lower()

    # 2. Tách chuỗi thành danh sách các từ (mặc định theo khoảng trắng)
    words = text.split()

    # 3. Đếm tần suất bằng Dictionary
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


# --- Chạy thử với Input mẫu ---
text_input = "AI là AI và dữ liệu là dữ liệu"
result = word_frequencies(text_input)

print(result)
# Output: {'ai': 2, 'là': 2, 'và': 1, 'dữ': 2, 'liệu': 2}
