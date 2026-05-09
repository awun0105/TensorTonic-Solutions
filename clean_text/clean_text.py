import re
import string


def clean_text(text):
    """
    Hàm làm sạch văn bản chuẩn NLP:
    1. Chuyển thường
    2. Xóa dấu câu
    3. Dọn dẹp khoảng trắng (Trùm cuối)
    """
    # Bước 1: Chuyển toàn bộ thành chữ thường
    text = text.lower()

    # Bước 2: Xóa các dấu câu theo yêu cầu (. , ! ?)
    # Nếu muốn xóa TOÀN BỘ dấu câu, hãy thay dòng dưới bằng:
    # text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r"[.,!?]", "", text)

    # Bước 3: Xử lý khoảng trắng (QUAN TRỌNG: Phải để cuối cùng)
    # re.sub(r'\s+', ' ', text): Biến mọi cụm khoảng trắng thừa ở giữa thành 1 dấu cách
    # .strip(): Cắt bỏ khoảng trắng dư ở hai đầu chuỗi
    text = re.sub(r"\s+", " ", text).strip()

    return text


# --- Kiểm tra kết quả ---
input_mau = "   Xin chào! Đây là Kỳ thi AI, Rất vui...   "
print(f"Kết quả: '{clean_text(input_mau)}'")
