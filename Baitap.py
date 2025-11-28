# Nhập đoạn văn từ bàn phím
print("Nhập vào 1 đoạn văn:")
doan = input().lower()  # Chuyển tất cả ký tự trong đoạn văn thành chữ thường để dễ so sánh

# Nhập từ cần đếm trong đoạn văn
print("Nhập từ cần đếm:")
tu = input().lower()  # Chuyển từ cần đếm thành chữ thường để so khớp chính xác

# Tách đoạn văn thành danh sách các từ
tach = doan.split()  # Ví dụ: "Tôi thích học" → ['tôi', 'thích', 'học']

# Đếm số lần xuất hiện của từ cần tìm trong danh sách từ
kq = tach.count(tu)

# In ra kết quả
print("Từ", tu, "xuất hiện:", kq, "lần")


# ------------------ PHẦN 2: ĐẾM KÝ TỰ HOA, THƯỜNG ------------------

def demkt(s):
    x1 = 0  # Biến đếm số ký tự in thường
    x2 = 0  # Biến đếm số ký tự in hoa
    for i in s:  # Duyệt qua từng ký tự trong chuỗi
        if i.isalpha():  # Kiểm tra xem ký tự đó có phải là chữ cái (A-Z hoặc a-z) không
            if i.islower():  # Nếu là chữ thường
                x1 += 1
            elif i.isupper():  # Nếu là chữ hoa
                x2 += 1
    return x1, x2  # Trả về 2 giá trị: số chữ thường và số chữ hoa


# Nhập chuỗi văn bản từ người dùng
s = input("Nhập đoạn văn bản: ")

# Gọi hàm và nhận kết quả
x1, x2 = demkt(s)

# In kết quả
print("Số kí tự in thường là:", x1)
print("Số kí tự in hoa là:", x2)


# ------------------ PHẦN 3: ĐẾM TỔNG SỐ TỪ VÀ KÝ TỰ ------------------

text = s  # Lấy lại chuỗi văn bản đã nhập ở trên

# Tách chuỗi thành danh sách các từ
words = text.split()  # Ví dụ: "Xin chào bạn" → ['Xin', 'chào', 'bạn']

# Đếm số lượng từ
so_tu = len(words)

# Đếm số ký tự không bao gồm khoảng trắng
so_ky_tu_khong_khoang_trang = len(text.replace(" ", ""))

# Đếm số ký tự có bao gồm khoảng trắng
so_ky_tu_co_khoang_trang = len(text)

# In ra kết quả
print("Số từ trong đoạn văn là:", so_tu)
print("Số ký tự không bao gồm khoảng trắng là:", so_ky_tu_khong_khoang_trang)
print("Số ký tự bao gồm khoảng trắng là:", so_ky_tu_co_khoang_trang)
