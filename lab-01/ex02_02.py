# Nhập bán kính từ người dùng và chuyển sang kiểu số thực (float)
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# Tính diện tích theo công thức: S = Pi * r^2
dien_tich = 3.14 * (ban_kinh ** 2)

# In diện tích của hình tròn ra màn hình
print("Diện tích của hình tròn là:", dien_tich)