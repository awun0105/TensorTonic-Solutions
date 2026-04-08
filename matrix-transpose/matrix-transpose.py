import numpy as np

def matrix_transpose(A):
    """
    Chuyển vị ma trận A mà không dùng np.transpose() hoặc .T
    
    Arguments:
    A -- mảng đầu vào (có thể là list hoặc numpy array)
    
    Returns:
    A_T -- mảng numpy đã được chuyển vị
    """
    # Chuyển đầu vào thành numpy array để lấy thông tin shape dễ dàng
    A_array = np.asarray(A)
    
    # Lấy số hàng (m) và số cột (n)
    m, n = A_array.shape
    
    # Tạo một ma trận mới toàn số 0 với shape ngược lại (n, m)
    # Lưu ý: dtype nên được giữ nguyên từ ma trận gốc
    A_T = np.zeros((n, m), dtype=A_array.dtype)
    
    # Duyệt qua từng phần tử và hoán đổi vị trí
    for i in range(m):
        for j in range(n):
            # Phần tử tại (i, j) của ma trận cũ sẽ nằm ở (j, i) của ma trận mới
            A_T[j, i] = A_array[i, j]
            
    return A_T
