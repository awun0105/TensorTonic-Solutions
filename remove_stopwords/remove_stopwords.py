def remove_stopwords(text, stop_words):
    """
    Hàm loại bỏ từ dừng ra khỏi câu văn.
    """
    # 1. Chuyển danh sách stop_words về chữ thường để so sánh dễ dàng
    # Sử dụng set() để tăng tốc độ tìm kiếm (lookup speed)
    stop_words_set = set(word.lower() for word in stop_words)

    # 2. Tách chuỗi văn bản thành danh sách các từ
    # .split() mặc định sẽ xử lý luôn các khoảng trắng dư thừa
    words = text.split()

    # 3. Lọc: Chỉ giữ lại những từ mà bản viết thường của nó KHÔNG nằm trong stop_words_set
    filtered_words = [w for w in words if w.lower() not in stop_words_set]

    # 4. Nối các từ còn lại bằng một khoảng trắng
    return " ".join(filtered_words)


# --- Chạy thử với Input mẫu ---
text_input = "Học machine learning rất khó nhưng thú vị"
stop_words_list = ["rất", "nhưng"]

result = remove_stopwords(text_input, stop_words_list)
print(f"Output: '{result}'")
