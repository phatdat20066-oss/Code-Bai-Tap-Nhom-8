import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu mẫu
# 1. Dữ liệu cho biểu đồ đường (Line plot)
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# 2. Dữ liệu cho biểu đồ cột (Bar chart)
# Sử dụng nhãn tiếng Anh (ASCII) để đảm bảo hiển thị đúng
categories = ['Group A', 'Group B', 'Group C', 'Group D']
values = [10, 24, 15, 7]

# 3. Dữ liệu cho biểu đồ tròn (Pie chart)
sizes = [15, 30, 45, 10]
pie_labels = ['Part 1', 'Part 2', 'Part 3', 'Part 4']

# 4. Dữ liệu cho biểu đồ chấm (Scatter plot)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# --- Vẽ 4 biểu đồ trên 1 lưới 2x2 ---
# plt.subplots(nrows, ncols, figsize=(width, height))
# fig là toàn bộ hình ảnh, ax là một mảng 2x2 chứa 4 ô (axes)
fig, ax = plt.subplots(2, 2) 

# Ô 1 (Hàng 0, Cột 0): Biểu đồ đường
ax[0, 0].plot(x_line, y_line, color='blue')
ax[0, 0].set_title('Bieu do Duong')
ax[0, 0].set_xlabel('Truc X')
ax[0, 0].set_ylabel('Truc Y')

# Ô 2 (Hàng 0, Cột 1): Biểu đồ cột
ax[0, 1].bar(categories, values, color='skyblue')
ax[0, 1].set_title('Bieu do Cot')
ax[0, 1].set_xlabel('Nhom')
ax[0, 1].set_ylabel('Gia tri')

# Ô 3 (Hàng 1, Cột 0): Biểu đồ tròn
# autopct='%1.1f%%' để hiển thị phần trăm
ax[1, 0].pie(sizes, labels=pie_labels, autopct='%1.1f%%', startangle=90)
ax[1, 0].set_title('Bieu do Tron')
ax[1, 0].axis('equal')  # Đảm bảo biểu đồ tròn là hình tròn

# Ô 4 (Hàng 1, Cột 1): Biểu đồ chấm
ax[1, 1].scatter(x_scatter, y_scatter, alpha=0.6, color='red')
ax[1, 1].set_title('Bieu do Cham')
ax[1, 1].set_xlabel('Gia tri X')
ax[1, 1].set_ylabel('Gia tri Y')

# Tự động điều chỉnh khoảng cách giữa các biểu đồ con cho đẹp
plt.tight_layout()

plt.show()