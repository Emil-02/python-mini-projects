import numpy as np
import matplotlib.pyplot as plt
# 1. Membuat rentang nilai x (Aplikasi Mobile)
x = np.linspace(0, 60, 400)
# 2. Persamaan kendala (diubah ke bentuk y =)
# 3x + 2y = 120  => y = (120 - 3x) / 2
y1 = (120 - 3*x) / 2
# x + y = 50     => y = 50 - x
y2 = 50 - x
# 3. Membuat grafik
plt.figure(figsize=(10, 7))
# Plot Garis Kendala dengan warna modifikasi
plt.plot(x, y1, label='3x + 2y = 120 (Tenaga Kerja)', color='blue', linestyle='--')
plt.plot(x, y2, label='x + y = 50 (Kapasitas)', color='green', linestyle='-')
# 4. Menentukan Feasible Region (Area yang diarsir)
y_min = np.minimum(y1, y2)
plt.fill_between(x, y_min, 0, where=(y_min >= 0), color='gold', alpha=0.2, label='Feasible Region')
# 5. Menandai Titik Optimal (Hasil perhitungan: 40, 0)
plt.plot(40, 0, 'ro', markersize=10, label='Titik Optimal (40, 0)')
plt.annotate('Solusi Optimal\n(40, 0)\nZ=20jt', xy=(40, 0), xytext=(45, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
# 6. Pengaturan Tampilan Grafik
plt.xlim(0, 60)
plt.ylim(0, 70)
plt.xlabel('x (Aplikasi Mobile)')
plt.ylabel('y (Aplikasi Web)')
plt.title('Optimasi Keuntungan Startup - Metode Grafik')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
# Tampilkan Grafik
plt.show()