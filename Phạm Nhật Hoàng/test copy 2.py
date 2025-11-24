import matplotlib.pyplot as plt
import numpy as np

thang = ['Thang 1', 'Thang 2', 'Thang 3', 'Thang 4', 'Thang 5', 'Thang 6']

doanhthu = [1000, 1200, 1150, 1300, 1450, 1600]

loinhuan = [80, 110, 100, 130, 150, 170]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Thang', fontsize=12)
ax1.set_ylabel('Doanh thu', color='skyblue', fontsize=12)
ax1.bar(thang, doanhthu, color='skyblue', label='Doanh thu')
ax1.tick_params(axis='y', labelcolor='skyblue')

# .twinx() là hàm quan trọng để tạo trục y thứ 2
ax2 = ax1.twinx()
ax2.set_ylabel('Loi nhuan', color='red', fontsize=12)

ax2.plot(thang, loinhuan, color='red', marker='o', linestyle='-', linewidth=2, label='Loi nhuan')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Bieu do Doanh thu va Loi nhuan 6 Thang Dau Nam', fontsize=16)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper left')

plt.tight_layout()

plt.show()