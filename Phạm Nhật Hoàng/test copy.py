import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y1 = x**2
y2 = x**3

with np.errstate(invalid='ignore'): # Tạm thời tắt cảnh báo 'invalid value'
    y3 = np.sqrt(x)

plt.figure()

# Sử dụng LaTeX (trong dấu $...$) để hiển thị công thức toán học đẹp hơn
plt.plot(x, y1, label='$y = x^2$', color='blue')
plt.plot(x, y2, label='$y = x^3$', color='red')
plt.plot(x, y3, label='$y = \sqrt{x}$', color='green') #, linewidth=2.5

# 4. Đặt tiêu đề và nhãn
plt.title('Do thi cac ham so y=x^2, y=x^3, va y=sqrt(x)', fontsize=16)
plt.xlabel('Truc X', fontsize=12)
plt.ylabel('Truc Y', fontsize=12)

# 5. Hiển thị chú giải (legend)
plt.legend(fontsize=12)

# Thêm lưới
#plt.grid(True, linestyle=':', alpha=0.7)

# Thêm đường trục 0 (trục hoành và trục tung)
#plt.axhline(0, color='black', linewidth=0.5)
#plt.axvline(0, color='black', linewidth=0.5)

plt.show()